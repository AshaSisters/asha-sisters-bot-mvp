from datetime import datetime
from flask import request
from utils.session import get_session, update_session
from utils.airtable_logger import log_to_airtable
from utils.languages import translate
from sales import log_sale  # New import for Phase 2 prep

def handle_training_flow(user_input, session_id, lang):
    session = get_session(session_id)
    phone_number = session.get("phone_number", "")  # Default empty string

    # Initialize flow
    if "training_step" not in session:
        update_session(session_id, "training_step", "intro")
        return translate(
            "Welcome to Asha Sisters Training!\n"
            "1. Register\n2. Refer Sister\n3. Course Info", 
            lang
        )

    step = session.get("training_step")

    # Step 1: Registration choice
    if step == "intro":
        choice = user_input.strip().lower()
        if choice in ["1", "register", "yes", "ndinoda", "yebo"]:
            update_session(session_id, "training_type", "self")
            update_session(session_id, "training_step", "location")
            return translate("Enter your location (District/Village):", lang)
        elif choice in ["2", "refer", "refera", "ncoma"]:
            update_session(session_id, "training_type", "referral")
            update_session(session_id, "training_step", "sister_name")
            return translate("Enter sister's full name:", lang)
        elif choice in ["3", "info", "details"]:
            return translate(
                "Courses:\n- Solar Installation\n- Business Skills\n"
                "Reply 1 to register or 2 to refer someone.",
                lang
            )
        else:
            return translate("Invalid choice. Reply 1, 2 or 3.", lang)

    # Step 2: Location capture
    elif step == "location":
        update_session(session_id, "location", user_input)
        update_session(session_id, "training_step", "education")
        return translate(
            "Education level:\n1. Primary\n2. Secondary\n3. Tertiary\n4. Other", 
            lang
        )

    # Step 3: Education level
    elif step == "education":
        edu_map = {"1": "Primary", "2": "Secondary", "3": "Tertiary", "4": "Other"}
        if user_input.strip() not in edu_map:
            return translate("Invalid option. Reply 1-4.", lang)
        update_session(session_id, "education_level", edu_map[user_input.strip()])
        update_session(session_id, "training_step", "experience")
        return translate("Years of work experience (number):", lang)

    # Step 4: Work experience
    elif step == "experience":
        try:
            exp = int(user_input)
            update_session(session_id, "experience_years", exp)
            update_session(session_id, "training_step", "course")
            return translate(
                "Preferred course:\n1. Solar\n2. Business\n3. Both", 
                lang
            )
        except ValueError:
            return translate("Please enter a number (e.g. 2).", lang)

    # Step 5: Course selection
    elif step == "course":
        course_map = {"1": "Solar", "2": "Business", "3": "Both"}
        if user_input.strip() not in course_map:
            return translate("Invalid choice. Reply 1-3.", lang)
        update_session(session_id, "preferred_course", course_map[user_input.strip()])
        update_session(session_id, "training_step", "funding")
        return translate(
            "Funding option:\n1. Self-fund\n2. Scholarship\n3. Installments", 
            lang
        )

    # Step 6: Funding option
    elif step == "funding":
        fund_map = {"1": "Self", "2": "Scholarship", "3": "Installments"}
        if user_input.strip() not in fund_map:
            return translate("Invalid option. Reply 1-3.", lang)
        update_session(session_id, "funding_option", fund_map[user_input.strip()])
        update_session(session_id, "training_step", "phone")
        return translate("Enter WhatsApp number for confirmation:", lang)

    # Step 7: Finalize registration
    elif step == "phone":
        phone = user_input.strip()
        if not phone.startswith("+"):
            phone = f"+263{phone.lstrip('0')}"  # Zimbabwe format example
        
        # Log to Airtable
        log_to_airtable("Training", {
            "Timestamp": datetime.now().isoformat(),
            "Phone": phone,
            "Language": lang,
            "Course": session.get("preferred_course"),
            "Location": session.get("location"),
            "Education": session.get("education_level"),
            "Experience": session.get("experience_years"),
            "Funding": session.get("funding_option"),
            "Type": "direct"  # For Phase 2 segmentation
        })

        # Phase 2 prep - log as potential sale
        log_sale(
            product="training_program",
            quantity=1,
            buyer_phone=phone,
            location=session.get("location"),
            customer_type="potential_student"
        )

        update_session(session_id, "training_step", None)
        return translate(
            "✅ Registered! We'll contact you within 48hrs.\n"
            "Next steps:\n1. Schedule interview\n2. Payment confirmation", 
            lang
        )

    # Referral Steps
    elif step == "sister_name":
        update_session(session_id, "sister_name", user_input)
        update_session(session_id, "training_step", "sister_phone")
        return translate("Enter sister's WhatsApp number:", lang)

    elif step == "sister_phone":
        sister_phone = user_input.strip()
        if not sister_phone.startswith("+"):
            sister_phone = f"+263{sister_phone.lstrip('0')}"

        # Log referrer
        log_to_airtable("Training", {
            "Timestamp": datetime.now().isoformat(),
            "Phone": phone_number,
            "Referred_Name": session.get("sister_name"),
            "Referred_Phone": sister_phone,
            "Type": "referral"
        })

        # Log referral as potential student
        log_sale(
            product="training_program",
            quantity=1,
            buyer_phone=sister_phone,
            location=session.get("location", "Unknown"),
            customer_type="referred_student"
        )

        update_session(session_id, "training_step", None)
        return translate(
            f"✅ We'll contact {session.get('sister_name')} about training!\n"
            "You qualify for referral bonuses after she completes registration.",
            lang
        )

    # Error handling
    else:
        return translate("System error. Please type MENU to restart.", lang)