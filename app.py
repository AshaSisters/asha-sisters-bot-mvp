import os
from datetime import datetime
from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from utils.languages import langauages
from utils.airtable_logger import log_to_airtable

# Module handlers
from modules.maternal_health import handle_maternal_flow
from modules.training import handle_training_flow
from modules.products import handle_product_flow
from modules.distributor import handle_distributor_flow

app = Flask(__name__)
sessions = {}

def get_session(session_id):
    return sessions.setdefault(session_id, {})

def update_session(session_id, key, value):
    sessions.setdefault(session_id, {})[key] = value

def handle_language_selection(user_input, session_id):
    lang_map = {'1': 'en', '2': 'sn', '3': 'nd'}
    choice = user_input.strip()
    if choice in lang_map:
        lang = lang_map[choice]
        update_session(session_id, 'language', lang)
        return True, lang
    return False, None

def handle_gender_age(user_input, session_id, lang):
    session = get_session(session_id)
    if 'gender' not in session:
        gender = user_input.strip().lower()
        if gender not in ['male', 'female']:
            return translate("Please specify 'male' or 'female'.", lang)
        update_session(session_id, 'gender', gender)
        return translate("What is your age?", lang)
    else:
        try:
            age = int(user_input.strip())
            update_session(session_id, 'age', age)
            if session.get('gender') == 'male' and age > 35:
                update_session(session_id, 'referring', True)
                return translate("Please write a sister's name and contact details.", lang)
            elif age < 18:
                update_session(session_id, 'adolescent', True)
                return handle_maternal_flow('2', session, lang)
            else:
                return show_main_menu(lang)
        except ValueError:
            return translate("Please enter a valid age (number).", lang)

def show_main_menu(lang):
    options = [
        "1. PRODUCTS",
        "2. TRAINING",
        "3. DISTRIBUTOR",
        "4. MATERNAL_HEALTH"
    ]
    return translate("MAIN MENU\n", lang) + "\n".join([translate(opt, lang) for opt in options])

def handle_main_menu(user_input, session_id, lang):
    menu_map = {
        '1': handle_product_flow,
        '2': handle_training_flow,
        '3': handle_distributor_flow,
        '4': handle_maternal_flow
    }
    choice = user_input.strip().lower()
    if choice in menu_map:
        update_session(session_id, 'current_module', choice)
        session = get_session(session_id)
        return menu_map[choice](user_input, session, lang)
    else:
        return translate("Invalid choice. Please select 1-4.", lang)

def process_referral(user_input, session_id, lang):
    session = get_session(session_id)
    if 'sister_name' not in session:
        update_session(session_id, 'sister_name', user_input)
        return translate("Please enter sister's phone number.", lang)
    else:
        update_session(session_id, 'sister_phone', user_input)
        log_to_airtable("REFERRALS", {
            "Timestamp": datetime.now().isoformat(),
            "Referrer": session.get('phone_number'),
            "Sister Name": session.get('sister_name'),
            "Sister Phone": session.get('sister_phone'),
            "Language": lang
        })
        return translate("Thank you for choosing Asha Sister, moving from Hope to Impact!", lang)

@app.route('/webhook', methods=['POST'])
def webhook():
    incoming_msg = request.values.get('Body', '').strip()
    sender = request.values.get('From', '')
    media_url = request.values.get('MediaUrl0', None)

    resp = MessagingResponse()
    msg = resp.message()

    session_id = sender
    session = get_session(session_id)
    lang = session.get('language', 'en')

    if 'language' not in session:
        if incoming_msg.lower() in ['asha', 'hallo', 'hello', 'halo']:
            msg.body(
                "Welcome to Asha Sisters 👭\nChoose Language:\n1. English\n2. Shona\n3. IsiNdebele\n\n🛡️ Your data is secure. "
                "We collect minimal personal information to provide better services for women's health, energy, and opportunity. "
                "Your data will never be shared with third parties without your consent.\n\nTo continue, type 1, 2 or 3."
            )
        else:
            success, lang_code = handle_language_selection(incoming_msg, session_id)
            if success:
                update_session(session_id, 'role_select', True)
                msg.body(translate("Are you:\n1. Woman in Business\n2. Youth Entrepreneur\n3. Referring A Sister", lang_code))
            else:
                msg.body("Invalid choice. Please select 1, 2 or 3.")
        return str(resp)

    elif incoming_msg.strip().lower() == 'privacy':
        msg.body("Here’s our full privacy policy: \n\nWe take your privacy seriously. All information provided to Asha Sisters is securely stored "
                 "and only used for the purpose of offering services in health, business, and empowerment. We do not share any data with third parties "
                 "without your express permission. If you have any questions, feel free to ask.")
        return str(resp)

    elif session.get('role_select', False):
        role_choice = incoming_msg.strip()
        if role_choice == '1':
            session.pop('role_select', None)
            msg.body(show_main_menu(lang))
        elif role_choice == '2':
            session.pop('role_select', None)
            msg.body(translate("Please tell us your gender (male/female):", lang))
        elif role_choice == '3':
            session.pop('role_select', None)
            update_session(session_id, 'referring', True)
            msg.body(translate("Please write a sister's name and contact details.", lang))
        else:
            msg.body(translate("Invalid choice. Please enter 1, 2 or 3.", lang))
        return str(resp)

    elif 'gender' not in session or ('gender' in session and 'age' not in session):
        msg.body(handle_gender_age(incoming_msg, session_id, lang))
        return str(resp)

    elif session.get('referring', False):
        msg.body(process_referral(incoming_msg, session_id, lang))
        return str(resp)

    elif 'current_module' in session:
        module = session['current_module']
        if module == '1':
            response = handle_product_flow(incoming_msg, session_id, lang)
        elif module == '2':
            response = handle_training_flow(incoming_msg, session_id, lang)
        elif module == '3':
            response = handle_distributor_flow(incoming_msg, session_id, lang)
        elif module == '4':
            response = handle_maternal_flow(incoming_msg, session, lang, media_url)

        log_to_airtable("INCOMING_MESSAGES", {
            "Timestamp": datetime.now().isoformat(),
            "Sender": sender,
            "Message": incoming_msg,
            "Media": media_url,
            "Language": lang,
            "Module": module
        })

        if response.strip().lower().endswith("thank you") or "menu" in response.strip().lower():
            update_session(session_id, 'current_module', None)

        msg.body(response)
        return str(resp)

    else:
        msg.body(handle_main_menu(incoming_msg, session_id, lang))

    return str(resp)

if __name__ == '__main__':
    app.run(debug=True)
