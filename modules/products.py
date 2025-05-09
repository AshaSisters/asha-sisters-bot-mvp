
from datetime import datetime
from flask import request
from utils.session import get_session, update_session
from utils.airtable_logger import log_to_airtable
from utils.languages import translate

# Product descriptions including cold storage
products = {
    "solar lamp": {
        "en": "Solar lamps provide clean, affordable lighting for homes and small businesses. They reduce reliance on kerosene, improving indoor air quality and cutting carbon emissions.",
        "sn": "Mwenje wezuva unopa chiedza chakasviba uye chinodhura zvakaderera kumisha nemabhizinesi madiki.",
        "nd": "Izibane zelanga zinikeza ukukhanya okuhlanzekileyo kwezimuli lamabhizimusi amancane."
    },
    "clean cookstove": {
        "en": "Clean cookstoves use less fuel and produce less smoke, improving health and reducing deforestation.",
        "sn": "Mabiko akachena anoshandisa mafuta mashoma uye anoburitsa utsi hushoma, zvichibatsira hutano.",
        "nd": "Izitofu ezihlanzekileyo zisebenzisa uphethiloli omncane futhi zithumele intuthu encane."
    },
    "water purifier": {
        "en": "Water purifiers ensure safe drinking water, reducing waterborne diseases in the community.",
        "sn": "Midziyo yekuchenesa mvura inovimbisa mvura yakachena yekunwa, ichideredza zvirwere zvinokonzerwa nemvura.",
        "nd": "Izihlanzi zamanzi ziqinisekisa amanzi ahlanzekileyo okuphuza, kunciphisa izifo zamanzi."
    },
    "solar cold storage": {
        "en": "Solar-powered cold storage preserves perishable goods, reducing food waste and increasing farmer incomes.",
        "sn": "Mafriji ane zuva anochengetedza zvinhu zvinokurumidza kuora, zvichideredza kuraswa kwechikafu.",
        "nd": "Izitoki ezipholile zelanga zigcina ukudla okushayizana, zinciphise ukungabi lutho."
    },
    "solar irrigation": {
        "en": "Solar irrigation systems enable efficient watering of crops using clean energy, boosting food security.",
        "sn": "Masisitimu ekudiridza ezuva anobatsira kurima nekuchengetedza simba.",
        "nd": "Izinhlelo zokunisela zelanga zisebenzisa amandla ahlanzekileyo ukunisela izilimo."
    }
}

def handle_product_flow(user_input, session_id, lang):
    session = get_session(session_id)
    phone_number = session.get("phone") or session.get("phone_number")

    # Initialize flow
    if "product_step" not in session:
        update_session(session_id, "product_step", "choose_product")
        options = "\n".join([f"- {p.title()}" for p in products.keys()])
        return translate("Please choose a product:\n" + options, lang)

    step = session.get("product_step")

    # Product selection
    if step == "choose_product":
        product = user_input.lower().strip()
        if product not in products:
            return translate("Invalid choice. Please select from the list.", lang)
        update_session(session_id, "selected_product", product)
        update_session(session_id, "product_step", "payment_plan")
        description = products[product].get(lang, products[product]["en"])
        return translate(
            f"{product.title()} selected.\n{description}\n\nPayment options: Weekly or Monthly?",
            lang
        )

    elif step == "payment_plan":
        plan = user_input.lower().strip()
        if plan not in ["weekly", "monthly"]:
            return translate("Please choose Weekly or Monthly.", lang)
        update_session(session_id, "payment_plan", plan)
        update_session(session_id, "product_step", "use_case")
        return translate("Is this for personal or business use?", lang)

    elif step == "use_case":
        use = user_input.lower().strip()
        if use not in ["personal", "business"]:
            return translate("Please reply 'personal' or 'business'.", lang)
        update_session(session_id, "business_type", use)
        update_session(session_id, "product_step", "quantity")
        return translate("How many units do you need?", lang)

    elif step == "quantity":
        try:
            quantity = int(user_input)
            if quantity <= 0:
                raise ValueError
            update_session(session_id, "quantity", quantity)
            update_session(session_id, "product_step", "name")
            return translate("Please enter your full name.", lang)
        except ValueError:
            return translate("Please enter a valid number greater than 0.", lang)

    elif step == "name":
        update_session(session_id, "name", user_input)
        update_session(session_id, "product_step", "phone")
        return translate("Please enter your phone number.", lang)

    elif step == "phone":
        update_session(session_id, "phone", user_input)
        update_session(session_id, "product_step", "location")
        return translate("Please enter your location (village/town).", lang)

    elif step == "location":
        update_session(session_id, "location", user_input)
        update_session(session_id, "product_step", "youth_owned")
        return translate("Is this youth-owned? (Yes/No)", lang)

    elif step == "youth_owned":
        update_session(session_id, "youth_owned", user_input)
        update_session(session_id, "product_step", "woman_owned")
        return translate("Is this woman-owned? (Yes/No)", lang)

    elif step == "woman_owned":
        update_session(session_id, "woman_owned", user_input)
        update_session(session_id, "product_step", None)

        product = session.get("selected_product")
        quantity = session.get("quantity", 1)

        # Log to Airtable (use uppercase to match Airtable base)
        log_to_airtable("PRODUCTS", {
            "Timestamp": datetime.now().isoformat(),
            "Phone": phone_number,
            "Product": product,
            "Quantity": quantity,
            "Business Type": session.get("business_type"),
            "Location": session.get("location"),
            "Youth Owned": session.get("youth_owned"),
            "Woman Owned": session.get("woman_owned")
        })

        # Log to SALES table or analytics module
        log_sale(
            product=product,
            quantity=quantity,
            buyer_phone=phone_number,
            location=session.get("location"),
            customer_type=session.get("business_type", "personal")
        )

        return translate(
            f"Thank you! We've recorded your order for {quantity} {product}(s). Our agent will contact you soon.",
            lang
        )

    else:
        return translate("An error occurred. Please type MENU to restart.", lang)
