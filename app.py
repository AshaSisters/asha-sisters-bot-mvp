import os
from datetime import datetime
from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from utils.languages import translate  # Updated import
from utils.airtable_logger import log_to_airtable

app = Flask(__name__)

sessions = {}

# Module handlers
from modules.maternal_health import handle_maternal_flow
from modules.training import handle_training_flow
from modules.products import handle_product_flow
from modules.distributor import handle_distributor_flow


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
        update_ses