# airtable_logger.py

import os
import requests

# Environment variables
AIRTABLE_BASE_ID = os.getenv("AIRTABLE_BASE_ID")
AIRTABLE_API_KEY = os.getenv("AIRTABLE_API_KEY")

AIRTABLE_BASE_URL = f"https://api.airtable.com/v0/{AIRTABLE_BASE_ID}"
HEADERS = {
    "Authorization": f"Bearer {AIRTABLE_API_KEY}",
    "Content-Type": "application/json"
}

# Mapping lowercase module keys to Airtable table names
MODULE_TABLE_MAP = {
    "products": "PRODUCTS",
    "distributors": "DISTRIBUTOR",
    "maternal": "MATERNAL_HEALTH",
    "training": "TRAINING"
}

def log_to_airtable(module_key, data):
    """
    Log data to the appropriate Airtable table for the given module.

    Args:
        module_key (str): One of 'products', 'distributors', 'maternal', 'training'
        data (dict): Field values to log to Airtable
    """
    table_name = MODULE_TABLE_MAP.get(module_key.lower())
    if not table_name:
        print(f"[ERROR] Unknown module key: {module_key}")
        return

    url = f"{AIRTABLE_BASE_URL}/{table_name}"
    payload = { "fields": data }

    try:
        response = requests.post(url, json=payload, headers=HEADERS)
        if response.status_code >= 400:
            print(f"[Airtable ERROR] {response.status_code}: {response.text}")
        else:
            print(f"[Airtable SUCCESS] Logged to {table_name}")
    except Exception as e:
        print(f"[Airtable EXCEPTION] {e}")
