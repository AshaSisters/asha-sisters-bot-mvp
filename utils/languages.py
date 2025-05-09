
# utils/languages.py
"""
Multilingual support for Asha Sisters WhatsApp bot
Supports English (en), Shona (sn), and Ndebele (nd)
"""

# Core translations dictionary
_translations = {
    'en': {
        # Greetings
        'Welcome to Asha Sisters 👭': 'Welcome to Asha Sisters 👭',
        'Choose Language': 'Choose Language',
        
        # Main Menu
        'MAIN MENU': 'MAIN MENU',
        '1. PRODUCTS': '1. PRODUCTS',
        '2. TRAINING': '2. TRAINING',
        '3. DISTRIBUTOR': '3. DISTRIBUTOR',
        '4. MATERNAL_HEALTH': '4. MATERNAL_HEALTH',
        
        # Common Responses
        'Invalid choice. Please select 1-4.': 'Invalid choice. Please select 1-4.',
        'Please specify "male" or "female".': 'Please specify "male" or "female".',
        'Please enter a valid age (number).': 'Please enter a valid age (number).',
        
        # Products
        'Solar lamps provide clean, affordable lighting': 'Solar lamps provide clean, affordable lighting',
        
        # Maternal Health
        'Are you pregnant or a young girl seeking tips?': 'Are you pregnant or a young girl seeking tips?',
    },
    'sn': {
        # Greetings
        'Welcome to Asha Sisters 👭': 'Kugamuchirwa kuAsha Sisters 👭',
        'Choose Language': 'Sarudza Mutauro',
        
        # Main Menu
        'MAIN MENU': 'MENU HURU',
        '1. PRODUCTS': '1. ZVIGADZIRWA',
        '2. TRAINING': '2. KUDZIDZISWA',
        '3. DISTRIBUTOR': '3. MUGOVERI',
        '4. MATERNAL_HEALTH': '4. HUTANO HWEMADZIMAI',
        
        # Common Responses
        'Invalid choice. Please select 1-4.': 'Sarudzo isiriyo. Sarudza 1-4.',
        'Please specify "male" or "female".': 'Taura kuti "murume" kana "mukadzi".',
        'Please enter a valid age (number).': 'Pinda zera chairo (nhamba).',
        
        # Products
        'Solar lamps provide clean, affordable lighting': 'Mwenje wezuva unopa chiedza chakachena uye chinodhura zvishoma',
        
        # Maternal Health
        'Are you pregnant or a young girl seeking tips?': 'Une nhumbu here kana musikana ari kutsvaga mazano?',
    },
    'nd': {
        # Greetings
        'Welcome to Asha Sisters 👭': 'Siyakwamukela ku-Asha Sisters 👭',
        'Choose Language': 'Khetha ulimi',
        
        # Main Menu
        'MAIN MENU': 'IMENU EYINKULU',
        '1. PRODUCTS': '1. IZIMKHIQIZO',
        '2. TRAINING': '2. UQEQESHO',
        '3. DISTRIBUTOR': '3. UMSABALALISI',
        '4. MATERNAL_HEALTH': '4. IMPILO YABESIFAZANE',
        
        # Common Responses
        'Invalid choice. Please select 1-4.': 'Ukukhetha okungekho lula. Khetha 1-4.',
        'Please specify "male" or "female".': 'Cacisa ukuthi "owesilisa" noma "owesifazane".',
        'Please enter a valid age (number).': 'Faka iminyaka yakwaziwayo (inombolo).',
        
        # Products
        'Solar lamps provide clean, affordable lighting': 'Izibane zelanga zinikeza ukukhanya okuhlanzekileyo',
        
        # Maternal Health
        'Are you pregnant or a young girl seeking tips?': 'Ukhulelwe yini noma uyintombazane esafufusa efuna amathiphu?',
    }
}

def translate(text, lang='en'):
    """
    Translate text to the specified language
    :param text: Text to translate
    :param lang: Target language code ('en', 'sn', 'nd')
    :return: Translated text or original if translation not found
    """
    lang = lang.lower()
    if lang not in _translations:
        lang = 'en'
    return _translations[lang].get(text, text)

def detect_language(text):
    """
    Simple language detection based on keywords
    :param text: Input text to analyze
    :return: Language code ('en', 'sn', or 'nd')
    """
    text_lower = text.lower()
    shona_keywords = ['ndinoda', 'mhoro', 'zvakanaka']
    ndebele_keywords = ['sawubona', 'yebo', 'kuhle']
    
    if any(word in text_lower for word in shona_keywords):
        return 'sn'
    elif any(word in text_lower for word in ndebele_keywords):
        return 'nd'
    return 'en'

# Export both functions and translations as requested
languages = {
    'translate': translate,
    'detect_language': detect_language,
    'translations': _translations
}