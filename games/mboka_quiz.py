# mboka_quiz.py
# 🇨🇩 DRC Quiz — 100 Questions (easy → hard)
from dataclasses import dataclass
from typing import List, Dict, Tuple, Optional

# -------------------- DATA MODEL --------------------
@dataclass
class QItem:
    q: str
    opts: List[str]
    ans: str
    expl: str
    links: Optional[List[str]] = None  # optional "learn more" links

# -------------------- QUESTION BANK --------------------
SECTIONS: Dict[str, Dict[str, object]] = {
    "A": {"title": "Geography & Nature (20)", "questions": [
        QItem("Where is the DRC located?", ["West Africa","Central Africa","North Africa","Southern Africa"], "Central Africa",
              "The DRC sits in the heart of Africa and is the continent’s second-largest country by area.",
              ["https://www.britannica.com/place/Democratic-Republic-of-the-Congo"]),
        QItem("What is the capital city of the DRC?", ["Lubumbashi","Goma","Kinshasa","Kisangani"], "Kinshasa",
              "Kinshasa lies on the Congo River, opposite Brazzaville (Republic of the Congo).",
              ["https://www.britannica.com/place/Kinshasa"]),
        QItem("What is the DRC’s coastline length on the Atlantic?", ["~15 km","~40 km","~120 km","No coastline"], "~40 km",
              "A short coast near Muanda gives limited access to the Atlantic Ocean.",
              ["https://www.britannica.com/place/Democratic-Republic-of-the-Congo"]),
        QItem("How many countries border the DRC?", ["7","8","9","10"], "9",
              "It borders Angola, Zambia, Tanzania, Burundi, Rwanda, Uganda, South Sudan, the Central African Republic, and the Republic of the Congo.",
              ["https://www.worldatlas.com/articles/what-countries-border-the-democratic-republic-of-the-congo.html"]),
        QItem("What is the main river crossing the country?", ["Nile","Congo","Niger","Zambezi"], "Congo",
              "The Congo River has the world’s second-largest discharge after the Amazon.",
              ["https://en.wikipedia.org/wiki/Congo_River"]),
        QItem("Which large lake borders the DRC and Rwanda?", ["Lake Victoria","Lake Kivu","Lake Albert","Lake Edward"], "Lake Kivu",
              "Lake Kivu is known for its methane gas reserves and borders Goma/Gisenyi.",
              ["https://en.wikipedia.org/wiki/Lake_Kivu"]),
        QItem("Which lake is Africa’s deepest, also bordering DRC?", ["Lake Tanganyika","Lake Malawi","Lake Albert","Lake Turkana"], "Lake Tanganyika",
              "Lake Tanganyika is the world’s second-deepest freshwater lake.",
              ["https://en.wikipedia.org/wiki/Lake_Tanganyika"]),
        QItem("Which lake lies in the northeast of the country?", ["Lake Victoria","Lake Edward","Lake Albert","Lake Mweru"], "Lake Albert",
              "Lake Albert is shared with Uganda in the Albertine Rift.",
              ["https://en.wikipedia.org/wiki/Lake_Albert"]),
        QItem("What is the highest peak in the DRC?", ["Mt. Nyiragongo","Mt. Mikeno","Mt. Stanley","Mt. Karisimbi"], "Mount Stanley",
              "Mount Stanley in the Rwenzori exceeds 5,100 m (shared with Uganda).",
              ["https://en.wikipedia.org/wiki/Mount_Stanley"]),
        QItem("Which active volcano near Goma erupted in 2002 and 2021?", ["Kilimanjaro","Nyamuragira","Nyiragongo","Meru"], "Nyiragongo",
              "Mount Nyiragongo is notorious for a large, fluid lava lake and fast lava flows.",
              ["https://en.wikipedia.org/wiki/Mount_Nyiragongo"]),
        QItem("What type of climate dominates most of the DRC?", ["Arid","Mediterranean","Equatorial tropical","Temperate"], "Equatorial tropical",
              "Hot/humid conditions with substantial rainfall across much of the country.",
              ["https://www.climatestotravel.com/climate/congo-kinshasa"]),
        QItem("What rainforest covers most of the DRC?", ["Miombo","Guinean forest","Congo Basin","Sahelian belt"], "Congo Basin",
              "The Congo Basin is the world’s second-largest tropical rainforest after the Amazon.",
              ["https://www.worldwildlife.org/places/congo-basin"]),
        QItem("Which endangered ape is only found in the DRC?", ["Gorilla","Bonobo","Chimpanzee","Golden monkey"], "Bonobo",
              "The bonobo (Pan paniscus) is endemic to the DRC south of the Congo River.",
              ["https://en.wikipedia.org/wiki/Bonobo"]),
        QItem("Which animal is called the “forest giraffe”?", ["Okapi","Bongo","Sitatunga","Kudu"], "Okapi",
              "The okapi is endemic to the Ituri Forest and is a national symbol.",
              ["https://en.wikipedia.org/wiki/Okapi"]),
        QItem("Africa’s oldest national park in the DRC is…", ["Serengeti","Virunga","Kahuzi-Biéga","Garamba"], "Virunga",
              "Founded in 1925, Virunga protects mountain gorillas and diverse ecosystems.",
              ["https://whc.unesco.org/en/list/63/"]),
        QItem("Major Congo River rapid/falls near Kinshasa?", ["Boyoma","Murchison","Inga (Livingstone)","Victoria"], "Inga (Livingstone)",
              "The Inga site underpins mega-hydropower proposals.",
              ["https://en.wikipedia.org/wiki/Inga_Dams"]),
        QItem("The Congo River crosses the Equator how many times?", ["0","1","2","3"], "2",
              "It is unusual among world rivers for this double crossing.",
              ["https://en.wikipedia.org/wiki/Congo_River"]),
        QItem("UNESCO site famous for eastern lowland gorillas?", ["Kahuzi-Biéga","Garamba","Salonga","Okapi Wildlife Reserve"], "Kahuzi-Biéga",
              "Kahuzi-Biéga is known for Grauer’s (eastern lowland) gorillas.",
              ["https://whc.unesco.org/en/list/137/"]),
        QItem("Copper-cobalt mining is concentrated mainly in which current provinces?", ["Ituri & Tshopo","Lualaba & Haut-Katanga","Kongo Central & Kwilu","Mai-Ndombe & Équateur"], "Lualaba & Haut-Katanga",
              "These provinces (from the 2015 découpage) host the Copperbelt.",
              ["https://en.wikipedia.org/wiki/Haut-Katanga_Province","https://en.wikipedia.org/wiki/Lualaba_Province"]),
        QItem("The DRC’s size compared to Western Europe?", ["Much smaller","Roughly equal","Slightly larger","Half as big"], "Roughly equal",
              "Its vast area is comparable to Western Europe.",
              ["https://www.britannica.com/place/Democratic-Republic-of-the-Congo"]),
    ]},
    "B": {"title": "History & Politics (20)", "questions": [
        QItem("The DRC’s name from 1971–1997 was…", ["Congo-Brazzaville","Zaire","Belgian Congo","Congo Free State"], "Zaire",
              "Mobutu Sese Seko renamed the country Zaire in 1971.",
              ["https://en.wikipedia.org/wiki/Zaire"]),
        QItem("First Prime Minister in 1960?", ["Joseph Kasa-Vubu","Patrice Lumumba","Moïse Tshombe","Cyrille Adoula"], "Patrice Lumumba",
              "Lumumba was a central independence figure and orator.",
              ["https://history.state.gov/milestones/1961-1968/congo-decolonization"]),
        QItem("King who owned the Congo as a personal colony?", ["Leopold I","Leopold II","Baudouin","Albert I"], "Leopold II",
              "The Congo Free State (1885–1908) was his private domain.",
              ["https://www.britannica.com/place/Congo-Free-State"]),
        QItem("Congo Free State became Belgian Congo in…", ["1898","1908","1918","1928"], "1908",
              "After global outrage over atrocities, Belgium annexed it.",
              ["https://www.britannica.com/place/Belgian-Congo"]),
        QItem("Dictator ruling ~30 years (1965–1997)?", ["Mobutu","Kabila Sr.","Kasavubu","Kabila Jr."], "Mobutu",
              "Mobutu Sese Seko centralized power and wealth.",
              ["https://www.britannica.com/biography/Mobutu-Sese-Seko"]),
        QItem("Who took power after Mobutu in 1997?", ["Bemba","Kabila Sr.","Kabila Jr.","Tshisekedi"], "Kabila Sr.",
              "Laurent-Désiré Kabila ousted Mobutu; assassinated in 2001.",
              ["https://www.britannica.com/biography/Laurent-Desire-Kabila"]),
        QItem("Who succeeded Laurent-Désiré Kabila in 2001?", ["Bemba","Tshisekedi","Mobutu","Joseph Kabila"], "Joseph Kabila",
              "He remained in office until 2019.",
              ["https://www.britannica.com/biography/Joseph-Kabila"]),
        QItem("Current president (as of 2025)?", ["Joseph Kabila","Félix Tshisekedi","Moïse Katumbi","Jean-Pierre Bemba"], "Félix Tshisekedi",
              "Inaugurated in 2019; re-elected in 2023/24.",
              ["https://www.britannica.com/biography/Felix-Tshisekedi"]),
        QItem("When did the Second Congo War start?", ["1996","1997","1998","1999"], "1998",
              "The conflict involved many neighboring states.",
              ["https://www.britannica.com/event/Second-Congo-War"]),
        QItem("Second Congo War officially ended in…", ["2001","2002","2003","2006"], "2003",
              "Among the deadliest conflicts since WWII.",
              ["https://www.britannica.com/event/Second-Congo-War"]),
        QItem("Long-standing UN peacekeeping mission acronym?", ["UNAMIR","MONUC/MONUSCO","MINUSMA","UNMISS"], "MONUC/MONUSCO",
              "One of the UN’s largest missions historically.",
              ["https://monusco.unmissions.org/en"]),
        QItem("Province that tried to secede in 1960?", ["Kasaï-Oriental","Lualaba","Équateur","Katanga (historic)"], "Katanga (historic)",
              "The secession was by historic Katanga; its area is now largely Lualaba & Haut-Katanga."),
        QItem("Who gave the fiery 1960 Independence speech?", ["Kasa-Vubu","Lumumba","Tshombe","Mobutu"], "Lumumba",
              "Lumumba directly criticized colonial rule on June 30, 1960.",
              ["https://www.marxists.org/subject/africa/lumumba/1960/06/independence.htm"]),
        QItem("Which superpower backed Mobutu?", ["USSR","USA","China","Cuba"], "USA",
              "He was a Cold War ally against communism.",
              ["https://history.state.gov/countries/congo-drc"]),
        QItem("‘Authenticité’ under Mobutu meant…", ["Privatization","Africanization","Federalism","Isolationism"], "Africanization",
              "Renaming places/people and promoting local culture.",
              ["https://en.wikipedia.org/wiki/Authenticit%C3%A9_(Zaire)"]),
        QItem("Explorer linked to Leopoldville’s founding?", ["David Livingstone","Henry Morton Stanley","John Speke","Richard Burton"], "Henry Morton Stanley",
              "He worked on behalf of Leopold II.",
              ["https://www.britannica.com/biography/Henry-Morton-Stanley"]),
        QItem("Rebel leader who became PM after 2003 accords?", ["Bemba","Nkunda","Ntaganda","Rubenga"], "Bemba",
              "Jean-Pierre Bemba later faced ICC proceedings.",
              ["https://www.icc-cpi.int/drc/bemba"]),
        QItem("Capital across the river from Kinshasa?", ["Brazzaville","Libreville","Luanda","Yaoundé"], "Brazzaville",
              "They are the world’s closest capital pair across a river.",
              ["https://earthobservatory.nasa.gov/images/4329/kinshasa-and-brazzaville"]),
        QItem("June 30 is celebrated as…", ["Martyrs’ Day","Unity Day","Independence Day","Heroes’ Day"], "Independence Day",
              "Marks independence from Belgium in 1960.",
              ["https://history.state.gov/milestones/1961-1968/congo-decolonization"]),
        QItem("DRC’s Cold War role in short?", ["Non-aligned","Eastern Bloc","Western-leaning ally","Isolationist"], "Western-leaning ally",
              "A strategic partner and resource supplier to the West."),
    ]},
    "C": {"title": "Culture & Society (20)", "questions": [
        QItem("Official language of the DRC?", ["English","Portuguese","French","Kikongo"], "French",
              "French is used in government, education, and media."),
        QItem("How many national languages?", ["3","4","5","6"], "4",
              "Lingala, Swahili, Kikongo/Kituba, and Tshiluba."),
        QItem("Most used national language in Kinshasa?", ["Swahili","Lingala","Kikongo","Tshiluba"], "Lingala",
              "Lingala is also associated with music and the military."),
        QItem("Dominant national language in the east?", ["Swahili","Lingala","Kikongo","Tshiluba"], "Swahili",
              "Spoken widely in Goma, Bukavu, and the eastern corridor."),
        QItem("Who’s often called the King of Congolese rumba?", ["Papa Wemba","Franco Luambo","Koffi Olomidé","Fally Ipupa"], "Papa Wemba",
              "He globalized Congolese rumba and was a fashion icon."),
        QItem("Modern star blending rumba/Afro sounds?", ["Youssou N’Dour","Diamond Platnumz","Fally Ipupa","Burna Boy"], "Fally Ipupa",
              "One of Africa’s most prominent pop artists."),
        QItem("Major religion?", ["Islam","Christianity","Hinduism","Traditional only"], "Christianity",
              "Catholic and Protestant communities are large."),
        QItem("The Sapeurs movement is about…", ["Dance","Cuisine","Fashion","Politics"], "Fashion",
              "Dandies in elegant suits expressing style and identity."),
        QItem("Dance linked to Congolese rumba/soukous?", ["Kizomba","Ndombolo","Azonto","Mapouka"], "Ndombolo",
              "A fast, energetic dance offshoot of soukous."),
        QItem("Bright patterned cloth commonly worn?", ["Kente","Ankara/Pagne","Shweshwe","Batik"], "Ankara/Pagne",
              "Colorful prints widely used across the DRC."),
        QItem("Most popular sport?", ["Basketball","Athletics","Football (soccer)","Volleyball"], "Football (soccer)",
              "The national team is nicknamed the Leopards."),
        QItem("First AFCON title year (as Congo-Kinshasa)?", ["1965","1968","1972","1974"], "1968",
              "They won again in 1974 as Zaire."),
        QItem("Other popular combat sport?", ["Judo","Boxing","Taekwondo","Karate"], "Boxing",
              "The country has produced notable boxers."),
        QItem("Traditional beliefs still present include…", ["Animism","Buddhism","Jainism","Shinto"], "Animism",
              "Ancestral and nature-based faiths remain influential."),
        QItem("Cultural/music capital of the DRC?", ["Goma","Lubumbashi","Kinshasa","Kisangani"], "Kinshasa",
              "A hub for art, style, and sound."),
        QItem("Urban art style with bright city scenes?", ["Realism","Popular painting","Cubism","Impressionism"], "Popular painting",
              "Narrative, colorful, and often humorous scenes."),
        QItem("Congolese painter famed internationally?", ["Chéri Samba","El Anatsui","Ibrahim El-Salahi","Moke"], "Chéri Samba",
              "Known for text-rich narrative works."),
        QItem("Not a Congolese author of note:", ["Sony Labou Tansi","V.Y. Mudimbe","Ferdinand Oyono","Pius Ngandu"], "Ferdinand Oyono",
              "Oyono is Cameroonian; the others are Congolese."),
        QItem("Diaspora best known abroad for…", ["Mining","Fashion & music","Agriculture","Shipbuilding"], "Fashion & music",
              "The diaspora has a strong cultural footprint in Europe."),
        QItem("2010s dance craze from Congo?", ["Azonto","Shaku Shaku","Ndombolo","Makossa"], "Ndombolo",
              "Exploded across Africa and beyond."),
    ]},
    "D": {"title": "Economy & Resources (20)", "questions": [
        QItem("The DRC’s most valuable mineral export:", ["Lithium","Cobalt","Nickel","Bauxite"], "Cobalt",
              "Cobalt is critical for modern batteries and EVs."),
        QItem("Metal heavily mined in which provinces?", ["Nord-Ubangi & Mongala","Ituri & Tshopo","Lualaba & Haut-Katanga","Tanganyika & Haut-Lomami"], "Lualaba & Haut-Katanga",
              "These southern provinces host the Copperbelt."),
        QItem("Tantalum ore used in electronics:", ["Coltan","Beryl","Cassiterite","Galena"], "Coltan",
              "Columbite-tantalite is used to produce tantalum capacitors."),
        QItem("Historically the diamond hub city is Mbuji-Mayi, in which current province?", ["Kasaï-Oriental","Kasaï-Central","Sankuru","Lomami"], "Kasaï-Oriental",
              "Mbuji-Mayi is in Kasaï-Oriental post-2015 split."),
        QItem("Share of world cobalt from the DRC (approx.):", ["<20%","~35%","~50%",">60%"], ">60%",
              "The DRC is by far the top producer globally."),
        QItem("Main agricultural staple:", ["Wheat","Cassava","Rice","Sorghum"], "Cassava",
              "Processed into fufu, chikwanga, and pondu."),
        QItem("Other key export crops:", ["Tea & cotton","Coffee & cocoa","Soy & barley","Millet & rye"], "Coffee & cocoa",
              "Especially from the eastern highlands."),
        QItem("Hydropower mega-site near Kinshasa:", ["Kariba","Cahora Bassa","Inga","Aswan"], "Inga",
              "The Inga site has massive hydro potential."),
        QItem("Major barrier to growth:", ["High latitude","Political instability & corruption","Cold winters","Small population"], "Political instability & corruption",
              "Despite resources, poverty persists."),
        QItem("GDP standing in Africa (rough):", ["Top 5","Top 10","Top 20","Bottom 10"], "Top 10",
              "Large resource base but low per-capita income."),
        QItem("Institutions often aiding the DRC:", ["NATO","ASEAN","IMF/World Bank","OPEC"], "IMF/World Bank",
              "Through loans, programs, and technical support."),
        QItem("Sector employing most people:", ["Mining","Manufacturing","Services","Agriculture"], "Agriculture",
              "Primarily subsistence livelihoods."),
        QItem("Problem tied to minerals in the east:", ["Overfishing","Conflict financing","Desertification","Hurricanes"], "Conflict financing",
              "‘Conflict minerals’ trade has funded armed groups."),
        QItem("Main Atlantic port city:", ["Muanda","Matadi","Boma","Banana"], "Matadi",
              "Key seaport on the Congo River near the coast."),
        QItem("WWII-era strategic mineral:", ["Uranium","Tungsten","Manganese","Chromite"], "Uranium",
              "Shinkolobwe mine supplied uranium for the Manhattan Project."),
        QItem("Growing renewable besides hydro:", ["Geothermal","Solar","Tidal","Offshore wind"], "Solar",
              "Off-grid solar is expanding."),
        QItem("Currency often used alongside CDF:", ["Euro","Pound","US Dollar","Yen"], "US Dollar",
              "Common for large urban transactions."),
        QItem("Province richest in industrial diamonds (regionally speaking):", ["Ituri","Kasaï-Oriental","Kivu","Équateur"], "Kasaï-Oriental",
              "Kasaï region remains a key diamond area."),
        QItem("Mining capital city:", ["Goma","Kisangani","Lubumbashi","Mbandaka"], "Lubumbashi",
              "Economic hub of the southern mining belt."),
        QItem("Employment situation overall:", ["Low unemployment","Near full employment","High underemployment","Seasonal only"], "High underemployment",
              "Informal work dominates the economy."),
    ]},
    "E": {"title": "Food, Fun & Facts (20)", "questions": [
        QItem("Fufu is made from…", ["Cassava/plantain/maize","Wheat","Rice","Millet"], "Cassava/plantain/maize",
              "Staple dough eaten with stews and sauces."),
        QItem("Saka saka (pondu) is…", ["Rice pilaf","Cassava leaves stew","Goat barbecue","Fried beans"], "Cassava leaves stew",
              "Cassava leaves cooked with palm oil; often fish or peanuts added."),
        QItem("Moambe chicken is…", ["Chicken in tomato","Chicken in peanut sauce","Chicken in yogurt","Chicken in coconut"], "Chicken in peanut sauce",
              "Peanut/palm base; a national favorite."),
        QItem("Palm wine is…", ["Distilled sugarcane","Fermented palm sap","Grapes","Corn mash"], "Fermented palm sap",
              "Traditional beverage across Central Africa."),
        QItem("Common street sweet:", ["Pastéis","Beignets","Baklava","Churros"], "Beignets",
              "Yeasted or quick doughnuts, often with sugar."),
        QItem("Most common stew protein:", ["Beef","Fish","Chicken","Pork"], "Fish",
              "Abundant freshwater fish from rivers/lakes."),
        QItem("Chikwanga is…", ["Cassava bread wrapped in leaves","Spicy rice","Millet flatbread","Plantain porridge"], "Cassava bread wrapped in leaves",
              "Fermented cassava loaf; travel-friendly staple."),
        QItem("Greens often with peanut sauce:", ["Kale/Spinach/Amaranth","Lettuce","Cabbage","Celery"], "Kale/Spinach/Amaranth",
              "Nutty sauces pair well with leafy greens."),
        QItem("Fried plantains are called…", ["Ndolé","Makemba","Alloco","Matoke"], "Makemba",
              "Popular snack/side across the country."),
        QItem("City famed for grilled goat (mbuzi) street food?", ["Goma","Lubumbashi","Kinshasa","Kikwit"], "Kinshasa",
              "An urban favorite, especially at night spots."),
        QItem("National football team nickname:", ["The Eagles","The Lions","The Leopards","The Panthers"], "The Leopards",
              "AFCON champions in 1968 and 1974 (as Zaire)."),
        QItem("AFCON title as Zaire (second time):", ["1968","1970","1972","1974"], "1974",
              "The same year Zaire played in the World Cup."),
        QItem("Zaire’s FIFA World Cup appearance:", ["1966","1970","1974","1978"], "1974",
              "The tournament was hosted by West Germany."),
        QItem("‘Rumble in the Jungle’ opponent of Ali:", ["Frazier","Foreman","Liston","Norton"], "Foreman",
              "Iconic 1974 fight took place in Kinshasa."),
        QItem("City that hosted ‘Rumble in the Jungle’:", ["Kinshasa","Lubumbashi","Kisangani","Mbuji-Mayi"], "Kinshasa",
              "The bout was at the 20 Mai Stadium."),
        QItem("Traditional thumb piano name:", ["Kora","Balafon","Likembe (mbira)","Ngoni"], "Likembe (mbira)",
              "A lamellophone used across the region."),
        QItem("Mobutu-era formalwear for men:", ["Dashiki","Abacost","Boubou","Safari suit"], "Abacost",
              "‘À bas le costume’ — national style without a tie."),
        QItem("UNESCO site protecting bonobos:", ["Garamba","Salonga","Virunga","Okapi Reserve"], "Salonga",
              "Africa’s largest tropical rainforest reserve."),
        QItem("Closest capital city to Kinshasa:", ["Libreville","Brazzaville","Luanda","Yaoundé"], "Brazzaville",
              "They face each other across the river."),
        QItem("Phrase for the resources-poverty paradox:", ["Resource miracle","Green growth","Rich country, poor people","Dutch disease"], "Rich country, poor people",
              "Vast wealth but low living standards due to governance challenges."),
    ]},
}

# -------------------- IMAGES (PNG/JPG only; Streamlit can display these) --------------------
IMAGES: Dict[Tuple[str, int], str] = {
    ("A", 0): "https://upload.wikimedia.org/wikipedia/commons/2/2b/DR_Congo_in_Africa_%28claimed%29_%28compact%29_%28%2Ball_claims%29.png",
    ("A", 4): "https://upload.wikimedia.org/wikipedia/commons/5/5b/Congo_River_meanders.jpg",
    ("A", 14): "https://upload.wikimedia.org/wikipedia/commons/7/71/Mountain_gorilla_in_Virunga.jpg",
    ("B", 1): "https://upload.wikimedia.org/wikipedia/commons/2/2a/Patrice_Lumumba%2C_square.jpg",
    ("D", 0): "https://upload.wikimedia.org/wikipedia/commons/7/7b/Cobalt_chunk.jpg",
    ("E", 2): "https://upload.wikimedia.org/wikipedia/commons/6/60/Poulet_moambe.jpg",
}

# -------------------- CLI MODE --------------------
def _ask_block_cli(block_key: str):
    block: List[QItem] = SECTIONS[block_key]["questions"]  # type: ignore
    score = 0
    for idx, qi in enumerate(block, 1):
        print(f"\n[{block_key}] Q{idx}. {qi.q}")
        for i, o in enumerate(qi.opts, 1):
            print(f"  {i}. {o}")
        g = input("Answer (1-4): ").strip()
        ok = g.isdigit() and 1 <= int(g) <= len(qi.opts) and qi.opts[int(g)-1] == qi.ans
        chosen = qi.opts[int(g)-1] if g.isdigit() and 1 <= int(g) <= len(qi.opts) else None
        if ok:
            print("✅ Correct!")
            score += 1
        else:
            print(f"❌ Wrong. Answer: {qi.ans}")
        print(f"ℹ️  {qi.expl}")
        if qi.links:
            print("   Learn more:", ", ".join(qi.links))
    print(f"\nSection {block_key} score: {score}/{len(block)}")
    return score

def play_cli():
    print("🇨🇩 DRC Quiz — CLI")
    keys = list(SECTIONS.keys())
    for k in keys:
        print(f"{k}: {SECTIONS[k]['title']}")  # type: ignore
    pick = input(f"Choose a section ({'/'.join(keys)} or ALL): ").strip().upper()
    total = 0; count = 0
    if pick == "ALL":
        for k in keys:
            print(f"\n=== Section {k}: {SECTIONS[k]['title']} ===")  # type: ignore
            total += _ask_block_cli(k)
            count += len(SECTIONS[k]["questions"])  # type: ignore
        print(f"\nTOTAL: {total}/{count}")
    elif pick in SECTIONS:
        print(f"\n=== Section {pick}: {SECTIONS[pick]['title']} ===")  # type: ignore
        total += _ask_block_cli(pick)
        count += len(SECTIONS[pick]["questions"])  # type: ignore
        print(f"\nTOTAL: {total}/{count}")
    else:
        print("No such section.")

# -------------------- STREAMLIT MODE --------------------
def render_st(st):
    st.header("🇨🇩 DRC Quiz — MCQ")

    # init state
    if "sec_key" not in st.session_state:
        st.session_state.sec_key = "A"
        st.session_state.idx = 0
        st.session_state.score = 0

    # section selector
    sec_key = st.selectbox(
        "Pick a section",
        options=list(SECTIONS.keys()) + ["ALL"],
        format_func=lambda k: k if k=="ALL" else f"{k}: {SECTIONS[k]['title']}",  # type: ignore
        index=(list(SECTIONS.keys()).index(st.session_state.get("sec_key","A"))
               if st.session_state.get("sec_key","A") in SECTIONS else len(SECTIONS))
    )

    # handle change
    if sec_key != st.session_state.sec_key:
        st.session_state.sec_key = sec_key
        st.session_state.idx = 0
        st.session_state.score = 0
        st.rerun()

    # make the question stream
    if sec_key == "ALL":
        stream: List[Tuple[str, int, QItem]] = []
        for k in SECTIONS:
            stream.extend([(k, i, qi) for i, qi in enumerate(SECTIONS[k]["questions"])])  # type: ignore
    else:
        stream = [(sec_key, i, qi) for i, qi in enumerate(SECTIONS[sec_key]["questions"])]  # type: ignore

    i = st.session_state.idx
    if i < len(stream):
        k, j, qi = stream[i]
        st.subheader(f"{'ALL ' if sec_key=='ALL' else ''}Q{i+1} — Section {k}: {qi.q}")

        # ALWAYS show image if we have one (no toggle)
        img_url = IMAGES.get((k, j))
        if img_url:
            try:
                st.image(img_url, use_container_width=True)
            except Exception:
                st.info("Image unavailable. (Use PNG/JPG, not SVG.)")

        choice = st.radio("Options", qi.opts, key=f"q_{i}")
        col1, col2 = st.columns(2)
        if col1.button("Submit", key=f"submit_{i}"):
            if choice == qi.ans:
                st.session_state.score += 1
                st.success("✅ Correct!")
            else:
                st.error(f"❌ Wrong. Correct answer: {qi.ans}")
            with st.expander("Why? (Explanation)"):
                st.write(qi.expl)
                if qi.links:
                    st.markdown("**Learn more:**")
                    for u in qi.links:
                        st.markdown(f"- [{u}]({u})")
            st.session_state.idx += 1
            st.rerun()

        if col2.button("Skip", key=f"skip_{i}"):
            st.info(f"Skipped. Correct answer: {qi.ans}")
            with st.expander("Why? (Explanation)"):
                st.write(qi.expl)
                if qi.links:
                    st.markdown("**Learn more:**")
                    for u in qi.links:
                        st.markdown(f"- [{u}]({u})")
            st.session_state.idx += 1
            st.rerun()

        st.progress((i+1) / len(stream))
        st.caption(f"Score so far: {st.session_state.score}/{i}")
    else:
        st.success(f"Finished! Final Score: {st.session_state.score}/{len(stream)}")
        if st.button("Restart"):
            st.session_state.idx = 0
            st.session_state.score = 0
            st.rerun()
