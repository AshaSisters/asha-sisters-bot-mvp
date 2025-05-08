from datetime import datetime
from flask import request
from session import get_session, update_session
from airtable_logger import log_to_airtable
from languages import translate
from sales import log_sale  # For sales tracking

def handle_distributor_flow(user_input, session_id, lang):
    session = get_session(session_id)
    phone_number = session.get("phone_number", "")  # Default empty string if not set

    # Resume referral if interrupted
    if "referring" not in session:
        update_session(session_id, "referring", False)
    elif session["referring"] and session.get("awaiting") not in ["sister_name", "sister_number"]:
        update_session(session_id, "awaiting", "sister_name")

    if "awaiting" not in session or session["awaiting"] is None:
        update_session(session_id, "awaiting", "interest")

    # Step 1: Capture interest area
    if session["awaiting"] == "interest":
        update_session(session_id, "distributor_interest", user_input)
        update_session(session_id, "awaiting", "location")
        return translate("Where are you located? (Village/Town)", lang)

    # Step 2: Capture location
    elif session["awaiting"] == "location":
        update_session(session_id, "distributor_location", user_input)
        update_session(session_id, "awaiting", "experience")
        return translate("How many years of sales experience do you have?", lang)

    # Step 3: Capture experience
    elif session["awaiting"] == "experience":
        try:
            experience = int(user_input.strip())
            update_session(session_id, "experience_years", experience)
            update_session(session_id, "awaiting", "phone")
            return translate("Please provide your WhatsApp number.", lang)
        except ValueError:
            return translate("Please enter a number (e.g. 2).", lang)

    # Step 4: Validate phone
    elif session["awaiting"] == "phone":
        phone = _normalize_zim_number(user_input.strip())
        update_session(session_id, "distributor_phone", phone)
        update_session(session_id, "awaiting", "referral")
        return translate("Would you like to refer another sister distributor? (YES/NO)", lang)

    # Step 5: Handle referral
    elif session["awaiting"] == "referral":
        answer = user_input.strip().lower()
        if answer in ["yes", "yebo", "hongu"]:  # EN/ND/SN
            update_session(session_id, "referring", True)
            update_session(session_id, "awaiting", "sister_name")
            return translate("Enter sister's full name:", lang)
        else:
            return _finalize_distributor(session_id, lang, phone_number)

    # Step 6: Capture sister's name
    elif session["awaiting"] == "sister_name":
        update_session(session_id, "sister_name", user_input)
        update_session(session_id, "awaiting", "sister_number")
        return translate("Enter sister's WhatsApp number:", lang)

    # Step 7: Finalize referral
    elif session["awaiting"] == "sister_number":
        sister_phone = _normalize_zim_number(user_input.strip())
        update_session(session_id, "sister_number", sister_phone)
        return _finalize_distributor(session_id, lang, phone_number, is_referral=True)

    # Fallback
    else:
        return translate("Sorry, something went wrong in the Distributor module. Please type MENU to restart.", lang)

def _finalize_distributor(session_id, lang, phone_number, is_referral=False):
    session = get_session(session_id)

    record = {
        "Timestamp": datetime.now().isoformat(),
        "Phone": phone_number,
        "Language": lang,
        "Interest": session.get("distributor_interest"),
        "Location": session.get("distributor_location"),
        "Experience": session.get("experience_years", 0),
        "Type": "distributor"
    }

    if is_referral:
        record.update({
            "Referred_Sister": session.get("sister_name"),
            "Referred_Phone": session.get("sister_number"),
            "Referral_Status": "pending"
        })

        log_sale(
            product="distributor_network",
            quantity=1,
            buyer_phone=session.get("sister_number"),
            location=session.get("distributor_location"),
            customer_type="potential_distributor"
        )

    # Log to Airtable
    log_to_airtable("Distributors", record)

    # Log sales opportunity
    log_sale(
        product="distribution_opportunity",
        quantity=1,
        buyer_phone=phone_number,
        location=session.get("distributor_location"),
        customer_type="verified_distributor"
    )

    # Clear session keys
    update_session(session_id, "awaiting", None)
    for key in [
        "distributor_interest", "distributor_location", "experience_years",
        "distributor_phone", "sister_name", "sister_number", "referring"
    ]:
        update_session(session_id, key, None)

    if is_referral:
        return translate(
            "Thank you! We've registered you and will contact "
            f"{session.get('sister_name')} about joining.",
            lang
        )
    return translate(
        "Registration complete! Our team will contact you within 48 hours.",
        lang
    )

def _normalize_zim_number(number):
    number = number.strip()
    if number.startswith("+263"):
        return number
    elif number.startswith("263"):
        return f"+{number}"
    elif number.startswith("0"):
        return f"+263{number[1:]}"
    return f"+263{number[-9:]}"
