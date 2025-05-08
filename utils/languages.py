
# Base translations
translations = {
    'en': {
        'Welcome to Asha Sisters 👭': 'Welcome to Asha Sisters 👭',
        'Choose Language': 'Choose Language',
        # Add all English phrases here
    },
    'sn': {
        'Welcome to Asha Sisters 👭': 'Kugamuchirwa kuAsha Sisters 👭',
        'Choose Language': 'Sarudza Mutauro',
        # Add all Shona translations here
    },
    'nd': {
        'Welcome to Asha Sisters 👭': 'Siyakwamukela ku-Asha Sisters 👭',
        'Choose Language': 'Khetha ulimi',
        # Add all Ndebele translations here
    }
}

# Product-specific translations (extend as needed)
product_translations = {
    'solar lamp': {
        'en': 'Solar lamps provide clean, affordable lighting',
        'sn': 'Mwenje wezuva unopa chiedza chakachena uye chinodhura zvishoma',
        'nd': 'Izibane zelanga zinikeza ukukhanya okuhlanzekileyo'
    },
    # Add other product translations
}

def translate(text, target_lang='en', context=None):
    """
    Translate text to target language
    :param text: Text to translate
    :param target_lang: Target language code ('en', 'sn', 'nd')
    :param context: Optional context for product-specific translations
    """
    if target_lang not in ['en', 'sn', 'nd']:
        target_lang = 'en'
    
    # First check product translations if context is provided
    if context == 'product' and text.lower() in product_translations:
        return product_translations[text.lower()].get(target_lang, text)
    
    # Then check general translations
    lang_dict = translations.get(target_lang, {})
    return lang_dict.get(text, text)

def detect_language(text):
    """Simple language detection based on keywords"""
    shona_keywords = ['ndinoda', 'mhoro', 'zvakanaka']
    ndebele_keywords = ['sawubona', 'yebo', 'kuhle']
    
    if any(word in text.lower() for word in shona_keywords):
        return 'sn'
    elif any(word in text.lower() for word in ndebele_keywords):
        return 'nd'
    return 'en'

def get_all_translations(key):
    """Get all language versions of a key"""
    return {
        'en': translations['en'].get(key, key),
        'sn': translations['sn'].get(key, key),
        'nd': translations['nd'].get(key, key)
    }