from utils.languages import translate
from utils.airtable_logger import log_to_airtable

PREGNANCY_TIPS = {
    "english": [
        "1. Start prenatal care early to ensure a healthy pregnancy.",
        "2. Eat a balanced diet rich in iron, calcium, and folic acid.",
        "3. Drink plenty of clean water daily.",
        "4. Avoid alcohol, smoking, and drugs.",
        "5. Take your prenatal vitamins as advised.",
        "6. Get plenty of rest and sleep.",
        "7. Attend all your clinic check-ups.",
        "8. Wash hands regularly to prevent infections.",
        "9. Stay active with light exercise like walking.",
        "10. Avoid lifting heavy objects.",
        "11. Report any unusual pain, bleeding, or fever to a clinic.",
        "12. Sleep on your side to improve blood flow.",
        "13. Avoid unprescribed medicines.",
        "14. Talk to your baby and bond.",
        "15. Wear comfortable clothes and shoes.",
        "16. Track baby movements daily after 28 weeks.",
        "17. Have a birth plan and know your delivery options.",
        "18. Learn danger signs in pregnancy.",
        "19. Keep your home environment smoke-free.",
        "20. Save emergency contacts and transport options.",
        "21. Breastfeeding is best—learn early.",
        "22. Prepare supplies for baby and yourself.",
        "23. Eat small, frequent meals.",
        "24. Manage stress with breathing and rest.",
        "25. Protect yourself from malaria with treated nets.",
        "26. Get tested for HIV and other infections.",
        "27. Inform clinic of any chronic conditions.",
        "28. Avoid raw meat and unpasteurized milk.",
        "29. Learn about safe labor and delivery.",
        "30. Make sure your tetanus shots are up to date.",
        "31. Don’t miss clinic appointments.",
        "32. Learn newborn care early.",
        "33. Encourage your partner to be involved.",
        "34. Watch for swelling in feet, hands, or face.",
        "35. Stay positive and ask for help when needed.",
        "36. Learn about postpartum care.",
        "37. Take care of your mental health.",
        "38. Practice safe sex during pregnancy.",
        "39. Know your blood type and complications.",
        "40. You're not alone—support is available."
    ],
    "shona": [
        "1. Tanga kurapwa kwepamuviri nekukurumidza kuti uve nehutano hwakanaka.",
        "2. Idya chikafu chine zvicherwa zvinodiwa nemuviri, senge iron, calcium, uye folic acid.",
        "3. Nwa mvura yakachena zuva nezuva.",
        "4. Dzivisa doro, kuputa, uye kushandisa zvinodhaka.",
        "5. Tora mavitamini epamuviri sezvakakurudzirwa nachiremba.",
        "6. Zorora zvakakwana uye urare zvakanaka.",
        "7. Pinda michero yako yese yekuongororwa kukiriniki.",
        "8. Geza maoko nguva dzose kudzivirira hutachiona.",
        "9. Ramba uchifamba zvishoma nezvishoma kusimbaradza muviri.",
        "10. Dzivisa kutakura zvinorema.",
        "11. Taura nezve chero marwadzo, kubuda ropa, kana kupisa kwemuviri kukiriniki.",
        "12. Rara ndakarara parutivi kuti ropa rifambe zvakanaka.",
        "13. Usatore mishonga isina kutaurwa nachiremba.",
        "14. Taura nemwana wako mukati uye hukama naye.",
        "15. Pfeka zvipfeko nemabhutsu zvakasununguka.",
        "16. Cherekedza kufamba kwemwana wako zuva nezuva mushure memavhiki makumi maviri nemasere.",
        "17. Gadzira hurongwa hwekusununguka uye uzive nzira dzekusununguka.",
        "18. Dzidza zviratidzo zvine njodzi pamuviri.",
        "19. Chengetedza imba yako isina utsi hwefodya.",
        "20. Chengetedza nhare dzekufonera paitika emergency uye nzira dzekufambisa.",
        "21. Kuyamwisa ndiko kunaka—dzidza izvi nekukurumidza.",
        "22. Gadzirira zvinhu zvaunoda nemwana wako.",
        "23. Idya kudya kudiki, kakawanda pazuva.",
        "24. Dzikamisa kushushikana nekufema zvakanaka uye kuzorora.",
        "25. Dzivirira malaria nemambure akarapwa nemishonga.",
        "26. Ita bvunzo dzeHIV nedzimwe hutachiona.",
        "27. Zivisa kiriniki nezve chero chirwere chaunenge uine.",
        "28. Dzivisa nyama isina kubikwa nemukaka usina kubikwa.",
        "29. Dzidza nezvekusununguka kwakachengeteka.",
        "30. Ita shure kuti majekiseni ako e tetanus akakwana.",
        "31. Usapotsa kuongororwa kwako kukiriniki.",
        "32. Dzidza kutarisira mwana achangozvarwa nekukurumidza.",
        "33. Kurudzira murume wako kuti akubatsire.",
        "34. Tarisa kuzvimba kwetsoka, maoko, kana kumeso.",
        "35. Ramba uine tariro uye kumbira rubatsiro kana uchida.",
        "36. Dzidza nezvekuzorora mushure mekusununguka.",
        "37. Tarisira hutano hwako hwepfungwa.",
        "38. Ita bonde rakachengeteka panguva yepamuviri.",
        "39. Ziva rudzi rweropa rwako nematambudziko anogona kuitika.",
        "40. Hausi wega—rubatsiro rwuripo."
    ],
    "ndebele": [
        "1. Qala ukunakekelwa ngaphambi kokubeletha ukuze ube nemitha elungile.",
        "2. Yidla ukudla okunempilo okunamandla e-iron, calcium, ne-folic acid.",
        "3. Phuza amanzi amsulwa nsuku zonke.",
        "4. Gwema utshwala, ukubhema, nezidakamizwa.",
        "5. Thatha amavithamini wakunikelwe ngudokotela.",
        "6. Phumula ngokwanele bese ulala kahle.",
        "7. Hlola zonke izinsuku zakho zokuhlolwa emtholampilo.",
        "8. Geza izandla njalo ukuze ugweme ukutheleleka.",
        "9. Hlala usebenza ngokuhamba okuncane ukuze uqinise umzimba.",
        "10. Gwema ukuphatha izinto ezisindayo.",
        "11. Bika kunoma yikuphi ukubuhlungu, ukuphalaza igazi, noma umkhuhlizo emtholampilo.",
        "12. Lalela ngasohlangothini ukuze igazi lihambe kahle.",
        "13. Gwema ukusebenzisa imithi engaphelanga ngudokotela.",
        "14. Khuluma nengane yakho ngaphakathi bese ubuhlobana nayo.",
        "15. Gqoka izingubo nezicathulo ezikhululekile.",
        "16. Qaphela ukunyakaza kwengane yakho nsuku zonke ngemuva kwamasonto angama-28.",
        "17. Lungiselela uhlelo lokubeletha futhi wazi izindlela zokubeletha.",
        "18. Funda izimpawu eziyingozi ngesikhathi sokukhulelwa.",
        "19. Gcina ikhaya lakho lingenabuthi likasikilidi.",
        "20. Gcina izinombolo zokuxhumana ngezimo eziphuthumayo nezindlela zokuhamba.",
        "21. Ukuncelisa kuyinto enhle—funda lokhu ngokushesha.",
        "22. Lungiselela izinto ozodinga ngengane yakho.",
        "23. Yidla ukudla okuncane, kaningi ngosuku.",
        "24. Lawula ukucindezeleka ngokuphefumula kahle nokuphumula.",
        "25. Zivikele ku-malaria ngamalambu anemithi.",
        "26. Zivumelele ukuhlolwa kwe-HIV nezinye izifo.",
        "27. Yazisa umtholampilo nganoma yisiphi isifo osinayo.",
        "28. Gwema inyama engagayiwe nobisi olungapasturizanga.",
        "29. Funda ngokubeletha okuphephile.",
        "30. Qinisekisa ukuthi imijovo yakho ye-tetanus isebenza.",
        "31. Ungaphuthelwa izinsuku zakho zokuhlolwa emtholampilo.",
        "32. Funda ukunakekela ingane esanda kuzalwa ngokushesha.",
        "33. Khuthaza umlingani wakho ukuba akusize.",
        "34. Qaphela ukuvuvukala kwezinyawo, izandla, noma ubuso.",
        "35. Hlala unethemba bese ucelo usizo uma udinga.",
        "36. Funda ngokuziphatha ngemuva kokubeletha.",
        "37. Nakekela impilo yakho yengqondo.",
        "38. Yenza ucansi oluphephile ngesikhathi sokukhulelwa.",
        "39. Yazi uhlobo lwegazi lakho nezingqinamba ezingenzeka.",
        "40. Awuwedwa—usizo lukhona."
    ]
}

ADOLESCENT_TIPS = {
    "english": [
        "1. Learn about your body and reproductive health.",
        "2. Ask trusted adults or health workers questions.",
        "3. Eat a healthy diet every day.",
        "4. Stay in school and focus on your goals.",
        "5. Avoid drugs, alcohol, and smoking.",
        "6. Build strong friendships and self-esteem.",
        "7. Delay sexual activity until you're ready.",
        "8. Understand the risks of early pregnancy.",
        "9. Use pads or cloth safely during periods.",
        "10. Keep your body clean and hygienic.",
        "11. Speak up if someone touches you inappropriately.",
        "12. Report abuse or violence immediately.",
        "13. Say no to peer pressure.",
        "14. Learn about HIV and how to protect yourself.",
        "15. Get vaccinated and visit clinics regularly.",
        "16. Avoid unsafe places when alone.",
        "17. Spend time with positive role models.",
        "18. Practice self-care and confidence.",
        "19. Know your rights and protect them.",
        "20. Join youth or girls’ clubs for support.",
        "21. Respect your body and others.",
        "22. Know signs of emotional stress and get help.",
        "23. Practice saying 'no' clearly and confidently.",
        "24. Avoid sharing personal photos online.",
        "25. Read books and learn new skills.",
        "26. Help with chores and learn responsibility.",
        "27. Protect your future—make wise choices.",
        "28. Talk openly with your guardians.",
        "29. Stay away from abusive relationships.",
        "30. Learn about menstruation and track it.",
        "31. Build your talent—art, sports, music.",
        "32. Understand consent in all relationships.",
        "33. Share feelings with trusted friends.",
        "34. Plan for your future career.",
        "35. Know where to get condoms and health help.",
        "36. Avoid sugar daddies or unsafe offers.",
        "37. Take care of your mental health.",
        "38. Respect others' privacy and space.",
        "39. Believe in yourself—you're important.",
        "40. You deserve love, safety, and dignity."
    ],
    "shona": [
        "1. Dzidza nezve muviri wako nehutano hwekubereka.",
        "2. Bvunza vanhu vakuru kana vashandi vehutano mibvunzo.",
        "3. Idya chikafu chine hutano zuva nezuva.",
        "4. Ramba uchidzidza uye wakanangisa nezvinangwa zvako.",
        "5. Dzivisa zvinodhaka, doro, uye kusvuta.",
        "6. Vaka hushamwari hwakasimba uye kuzviremekedza.",
        "7. Nonoka kuita zvepabonde kusvikira wagadzirira.",
        "8. Nzwisisa njodzi dzekukurumidza kubata pamuviri.",
        "9. Shandisa mapadhi kana machira akachena panguva yekuenda kumwedzi.",
        "10. Chengetedza muviri wako wakachena.",
        "11. Taura kana mumwe munhu akakubata zvisina kufanira.",
        "12. Mhan'ara kushungurudzwa kana mhirizhonga nekukurumidza.",
        "13. Rambira kudzvinyirirwa nevezera rako.",
        "14. Dzidza nezveHIV uye nzira dzekuzvidzivirira.",
        "15. Ita majekiseni uye shanyira zvipatara nguva dzose.",
        "16. Dzivisa nzvimbo dzisina kuchengeteka kana uri wega.",
        "17. Shanyira vanhu vanokufambira mberi.",
        "18. Dzidzira kuzvitarisira uye kuzvivimba.",
        "19. Ziva kodzero dzako uye dzidzivirire.",
        "20. Joinha makirabu evadiki kana evasikana kuti uwane rubatsiro.",
        "21. Remekedza muviri wako nevamwe.",
        "22. Ziva zviratidzo zvekushushikana uye tsvaga rubatsiro.",
        "23. Dzidzira kutaura 'kwete' zvakajeka uye nechivimbo.",
        "24. Dzivisa kugovera mifananidzo yako painternet.",
        "25. Verenga mabhuku uye dzidza hunyanzvi hutsva.",
        "26. Batira pamabasa epamba uye dzidza kuva nemutoro.",
        "27. Dzivirira ramangwana rako—ita sarudzo dzakangwara.",
        "28. Taura pachena nevachengeti vako.",
        "29. Dzivisa hukama hune chisimba.",
        "30. Dzidza nezvekuenda kumwedzi uye uzvinoteedzere.",
        "31. Vaka tarenda rako—unyanzvi, mitambo, mimhanzi.",
        "32. Nzwisisa mvumo muhukama hwese.",
        "33. Goverana manzwiro neshamwari dzakavimbika.",
        "34. Ronga nezvebasa rako remangwana.",
        "35. Ziva nzvimbo dzekuwana makondomu nerubatsiro rwehutano.",
        "36. Dzivisa vana baba kana zvinopihwa zvisina kuchengeteka.",
        "37. Chengetedza hutano hwako hwepfungwa.",
        "38. Remekedza kuvanzika uye nzvimbo yevamwe.",
        "39. Zvitenda—iwe wakakosha.",
        "40. Unokodzera rudo, kuchengeteka, uye chiremera."
    ],
    "ndebele": [
        "1. Funda ngomzimba wakho kanye nempilo yezocansi.",
        "2. Buza abantu abadala abathembekile noma abasebenzi bezempilo imibuzo.",
        "3. Yidla ukudla okunempilo nsuku zonke.",
        "4. Hlala esikoleni bese ugxila emagujini akho.",
        "5. Gwema izidakamizwa, utshwala, nokubhema.",
        "6. Yakha ubungane obuqinile kanye nokuzethemba.",
        "7. Liba ucansi kuze kube yilapho usukulungele.",
        "8. Qonda izingozi zokukhulelwa kusengomuntu esemncane.",
        "9. Sebenzisa ama-pad noma indwangu ngokuphepha ngesikhathi sokuthomba.",
        "10. Gcina umzimba wakho uhlanzekile.",
        "11. Khuluma uma omunye umuntu ekuthinta ngendlela engafanele.",
        "12. Bika ukuhlukunyezwa noma udlame ngokushesha.",
        "13. Yithi 'cha' ekucindezelweni yabantu abangani bakho.",
        "14. Funda nge-HIV nezindlela zokuzivikela.",
        "15. Thola imijovo bese uvakashela imitholampilo njalo.",
        "16. Gwema izindawo ezingaphephile uma ungedwa.",
        "17. Chitha isikhathi nabantu abakuthuthukisayo.",
        "18. Ziqeqeshe ukuzinakekela nokuzithemba.",
        "19. Yazi amalungelo akho bese uwavikela.",
        "20. Joyina amakilabhu entsha noma abantwana besifazane ukuze uthole ukusekelwa.",
        "21. Hlonipha umzimba wakho nabanye.",
        "22. Yazi izimpawu zokucindezeleka kwemizwa bese uthola usizo.",
        "23. Ziqeqeshe ukuthi 'cha' ngokucacile nangokuzethemba.",
        "24. Gwema ukwabelana ngezithombe zakho ku-inthanethi.",
        "25. Funda izincwadi bese ufunda amakhono amasha.",
        "26. Siza emisebenzini yasekhaya bese ufunda ukuba nomthwalo.",
        "27. Vikela ikusasa lakho—yenza izinqumo eziqondayo.",
        "28. Khuluma ngokukhululekile nabagcini bakho.",
        "29. Gwema ubudlelwano obunolaka.",
        "30. Funda ngokuthomba bese ulandelela.",
        "31. Yakha ithalenta lakho—ubuciko, imidlalo, umculo.",
        "32. Qonda imvumo kubo bonke ubudlelwano.",
        "33. Yabelana ngemizwa nabangane abathembekile.",
        "34. Hlela ngomsebenzi wakho wesikhathi esizayo.",
        "35. Yazi lapho ungathola khona amakhondomu nolusizo lwezempilo.",
        "36. Gwema ama-sugar daddy noma izintengo ezingaphephile.",
        "37. Nakekela impilo yakho yengqondo.",
        "38. Hlonipha ubumfihlo nendawo yabanye.",
        "39. Zikholwe—ubalulekile.",
        "40. Ufanelwe uthando, ukuphepha, nodumo."
    ]
}

def get_maternal_tip(index, lang="english", adolescent=False):
    tips = ADOLESCENT_TIPS if adolescent else PREGNANCY_TIPS
    lang = lang.lower()
    if lang not in tips:
        lang = "english"
    if 0 <= index < 40:
        return tips[lang][index]
    return translate("No more tips available.", lang)

def handle_maternal_flow(user_input, session, lang="english", attachment_url=None):
    step = session.get("maternal_step", 0)
    adolescent = session.get("adolescent", False)

    if step == 0:
        session["maternal_step"] = 1
        return translate("Are you pregnant or a young girl seeking tips? Reply '1' for pregnant or '2' for young girl.", lang)

    elif step == 1:
        if user_input == "1":
            session["adolescent"] = False
        elif user_input == "2":
            session["adolescent"] = True
        else:
            return translate("Please reply with '1' for pregnant or '2' for young girl.", lang)
        session["maternal_step"] = 2
        return translate("Would you like to receive weekly health tips for 40 weeks? Reply YES or NO.", lang)

    elif step == 2:
        if user_input.strip().lower() not in ["yes", "no"]:
            return translate("Please reply YES or NO.", lang)
        if user_input.strip().lower() == "yes":
            session["maternal_tip_index"] = 0
            session["maternal_step"] = 3
            session["subscribed_to_tips"] = True
            log_to_airtable("Maternal Health", {
                "User Phone": session.get("phone_number"),
                "Category": "Pregnant" if not session.get("adolescent") else "Adolescent",
                "Opted for Tips": "Yes",
                "Language": lang
            })
            return get_maternal_tip(0, lang, adolescent=session["adolescent"])
        else:
            session["maternal_step"] = 5
            return translate("Would you like to visit a clinic during your pregnancy? Reply YES or NO.", lang)

    elif step == 3:
        index = session.get("maternal_tip_index", 0) + 1
        if index >= 40:
            session["maternal_step"] = 5
            return translate("That was the last tip. Would you like to visit a clinic? Reply YES or NO.", lang)
        session["maternal_tip_index"] = index
        return get_maternal_tip(index, lang, adolescent=session.get("adolescent"))

    elif step == 5:
        if user_input.strip().lower() == "yes":
            session["maternal_step"] = 6
            session["clinic_commitment"] = True
            log_to_airtable("Maternal Health", {
                "User Phone": session.get("phone_number"),
                "Category": "Pregnant" if not session.get("adolescent") else "Adolescent",
                "Committed to Clinic": "Yes",
                "Language": lang
            })
            return translate("Thank you! You qualify for a 20% discount on PUEs. Please upload a photo of your clinic book with a stamp.", lang)
        elif user_input.strip().lower() == "no":
            session["maternal_step"] = 99
            return translate("Thank you for using the maternal health module. You can come back anytime.", lang)
        else:
            return translate("Please reply YES or NO.", lang)

    elif step == 6:
        if attachment_url:
            log_to_airtable("Maternal Health", {
                "User Phone": session.get("phone_number"),
                "Clinic Book Photo": [{"url": attachment_url}],  # Airtable attachment field
                "Photo Verified": "Pending"  # For manual review
            })
            session["maternal_step"] = 99
            return translate("Thank you! Your clinic book photo has been received. A nurse will verify it within 24 hours.", lang)
        else:
            return translate("Please upload your clinic book photo to confirm your visit.", lang)

    else:
        return translate("Thank you. Type MENU to return to main options.", lang)