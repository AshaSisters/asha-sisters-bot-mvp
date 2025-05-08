
# Asha Sisters Bot MVP

Welcome to the **Asha Sisters Bot MVP** repository! This project is a multilingual WhatsApp bot developed to empower women and youth entrepreneurs. The bot provides access to products, training resources, maternal health tips, and distributor opportunities, and is designed to help users achieve greater access to healthcare, business opportunities, and products.

## Table of Contents

- [Introduction](#introduction)
- [Project Features](#project-features)
- [Technologies Used](#technologies-used)
- [Installation and Setup](#installation-and-setup)
- [User Journey](#user-journey)
- [Phase 1 Modules](#phase-1-modules)
- [Phase 2: Future Enhancements](#phase-2-future-enhancements)
- [Contributing](#contributing)

## Introduction

Asha Sisters is dedicated to supporting women entrepreneurs by giving them access to affordable products, educational resources, and health tips through a WhatsApp bot interface. This project aims to enable positive social impact by empowering women and improving maternal health.

## Project Features

- **Multilingual Support**: English, Shona, and IsiNdebele.
- **Four Main Modules**:
  1. **Product Access (PUE)**: Provides information on solar products, payment plans, and purchasing.
  2. **Entrepreneurial Training**: Offers information on solar technical training and entrepreneurial skills.
  3. **Maternal Health Tips**: Provides weekly maternal and newborn care tips to pregnant women and adolescents.
  4. **Distributor Network**: Facilitates the application process for becoming a distributor and joining the network.

## Technologies Used

- **Python**: Flask framework for the web app backend.
- **Twilio**: For handling WhatsApp messaging functionality.
- **Google Sheets**: For logging user data and interactions.
- **Airtable**: For managing referral and sales data.
- **Flask**: Lightweight web framework for the server-side logic.
- **GitHub**: For version control and project hosting.

## Installation and Setup

### Requirements

- Python 3.8+
- Flask
- Twilio API
- Airtable API
- Google Cloud project for Sheets API access

### Setup Instructions

1. Clone the repository:

    ```bash
    git clone https://github.com/AshaSisters/asha-sisters-bot-mvp.git
    cd asha-sisters-bot-mvp
    ```

2. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Set up environment variables for Twilio, Airtable, Google Sheets, and other necessary keys.

4. Run the Flask app:

    ```bash
    python app.py
    ```

## User Journey

1. **Language Selection**: Users select their preferred language (English, Shona, IsiNdebele).
2. **Role Selection**: Users choose whether they are a woman in business, youth entrepreneur, or referring a sister.
3. **Age and Gender**: Users are prompted to enter their age and gender to tailor content.
4. **Access to Modules**: Based on the user's role and selection, they gain access to the four modules:
   - Products
   - Training
   - Maternal Health
   - Distributor Network


## Phase 1 Modules

### 1. Product Access (PUE)
Users can learn about solar products, payment plans, and apply for discounts. The module also offers educational content for promoting solar products.
### 2. Entrepreneurial Training
This module targets women entrepreneurs, guiding them through entrepreneurial skills and solar technical training. Users are asked to provide their location, education level, and funding status.
### 3. Maternal Health Tips
A key feature of the bot is to offer health tips to pregnant women and adolescent girls. The bot provides weekly health tips and encourages clinic visits for pregnant women. Users can earn a 20% discount code for solar products if they provide proof of their clinic visit.
### 4. Distributor Network
Users interested in becoming distributors can apply through this module. It collects personal details and interests to match applicants with the right distributor opportunities.

## Phase 2: Future Enhancements

### 1. **PAYG (Pay-As-You-Go) Integration**
We plan to integrate PAYG solutions, allowing users to access solar products with flexible payment options. This phase will also include a system for tracking PAYG payments and progress.
### 2. **Blockchain Integration for Carbon Credits**
To further enhance the sustainability and impact of the products, we will integrate blockchain technology to allow users to track their contributions to carbon credit generation.
### 3. **USSD Support**
Expanding the accessibility of the bot to users without smartphones, USSD functionality will allow those with basic mobile phones to interact with the system.
### 4. **Expanded Modules**
The bot will expand with more educational content, resources, and enhanced customer support features.


🚀 Join Us – We’re Open to Partners

We’re building an inclusive, scalable platform to empower women and girls through access to clean energy, digital tools, and economic opportunity. If you're a:

Funder interested in scalable gender-equity innovation
Nonprofit or NGO working in health, energy access, or youth empowerment
Technical partner supporting AI, digital public goods, or localization
Community organizer or grassroots network uplifting African women

We’d love to hear from you. Let's build this open, woman-led ecosystem toge
Please feel free to open issues and submit pull requests. Ensure that your code follows the project's coding guidelines, and write tests for any new features or bug fixes.

---

For any questions or feedback, reach out to the Asha Sisters team at (ovproductss@gmail.com).

