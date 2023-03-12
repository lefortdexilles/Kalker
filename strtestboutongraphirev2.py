import pickle
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
import requests
import plotly_express as ptx
import streamlit as st
import streamlit_authenticator as stauth
from streamlit_lottie import st_lottie

st.set_page_config(page_title="Graphique pluriannuel ire", layout="wide")

noms = ("PG", "AN", "Moi")
identifs = ("Pascale G", "Axel N", "Ego")

file_path = Path(__file__).parent / "hash-dutruc.pkl"
with file_path.open("rb") as file:
    hashed_passwords = pickle.load(file)

authenticator = stauth.Authenticate(noms, identifs, hashed_passwords, "tableau", "abcdef", cookie_expiry_days=4)

names, authentication_status, usernames = authenticator.login("Login", "main")

if authentication_status== False:
    st.error("identifiants incorrects")

if authentication_status== None:
    st.warning("Entrez vos codes svp")

if authentication_status== True:

    def load_lottieurl(url):
        r = requests.get(url)
        if r.status_code != 200:
            return None
        return r.json()

    lottie_coding = load_lottieurl("https://assets10.lottiefiles.com/packages/lf20_kwfcur7f.json")

    st_lottie(lottie_coding, height=300, key="coding")

    df = pd.read_excel('Panda10.xlsx')

    st.sidebar.header('Entrer le nom du pays')
    p_select = st.sidebar.selectbox("Pays:", ('AFGHANISTAN',	'AFRIQUE DU SUD (Johannesburg, Pretoria)',	'ALBANIE',	'ALGERIE (autres villes)',	'ALLEMAGNE (autres villes)',	'ANDORRE',	'ANGOLA',	'ANTIGUA-ET-BARBUDA',	'ARABIE SAOUDITE',	'ARGENTINE',	'ARMENIE',	'AUSTRALIE (Sydney)',	'AUTRICHE',	'AZERBAIDJAN',	'BAHREIN',	'BANGLADESH',	'BARBADE',	'BELGIQUE',	'BELIZE',	'BENIN',	'BHOUTAN',	'BIELORUSSIE',	'BIRMANIE',	'BOLIVIE',	'BOSNIE-HERZEGOVINE',	'BOTSWANA',	'BRESIL (Brasilia)',	'BRUNEI',	'BULGARIE',	'BURKINA FASO',	'BURUNDI',	'CAMBODGE',	'CAMEROUN (autres villes)',	'CANADA (Ottawa)',	'CAP-VERT',	'CHILI',	'CHINE (Pékin)',	'CHYPRE',	'COLOMBIE',	'COMORES',	'CONGO',	'CONGO RDC',	'COREE DU SUD',	'COSTA RICA',	'COTE D IVOIRE',	'CROATIE',	'CUBA',	'DANEMARK',	'DJIBOUTI', 'DOMINIQUE',	'EGYPTE',	'EMIRATS ARABES UNIS (Abu-Dhabi)',	'EQUATEUR',	'ERYTHREE',	'ESPAGNE',	'ESTONIE',	'ETATS-UNIS (Washington, Norfolk)',	'ETHIOPIE',	'FIDJI',	'FINLANDE',	'GABON',	'GAMBIE',	'GEORGIE',	'GHANA',	'GRECE',	'GRENADE',	'GUATEMALA',	'GUINEE',	'GUINEE EQUATORIALE',	'GUINEE-BISSAO',	'GUYANA',	'HAITI',	'HONDURAS',	'HONGRIE',	'INDE (New Delhi, Calcutta)',	'INDONESIE',	'IRAK (autres villes)',	'IRAN',	'IRLANDE',	'ISLANDE',	'ISRAEL',	'ITALIE (autres villes)',
        'JAMAIQUE',	'JAPON (Tokyo)',	'JERUSALEM',	'JORDANIE',	'KAZAKHSTAN',	'KENYA',	'KIRGHIZSTAN',	'KOSOVO',	'KOWEIT',	'LAOS',	'LESOTHO',	'LETTONIE',	'LIBAN', 'LIBERIA',	'LIBYE',	'LITUANIE',	'LUXEMBOURG',	'MACEDOINE',	'MADAGASCAR',	'MALAISIE',	'MALAWI',	'MALDIVES',	'MALI',	'MALTE',	'MAROC (autres villes)',	'MAURICE',	'MAURITANIE',	'MEXIQUE',	'MOLDAVIE',	'MONACO',	'MONGOLIE',	'MONTENEGRO',	'MOZAMBIQUE',	'NAMIBIE',	'NEPAL',	'NICARAGUA',	'NIGER',	'NIGERIA',	'NORVEGE (autres villes)',
        'NOUVELLE-ZELANDE',	'OMAN',	'OUGANDA',	'OUZBEKISTAN', 'PAKISTAN (Karachi)',	'PANAMA',	'PAPOUASIE-NOUVELLE-GUINEE',	'PARAGUAY',	'PAYS-BAS',	'PEROU',	'PHILIPPINES',	'POLOGNE',	'PORTUGAL',	'QATAR',	'REPUBLIQUE CENTRAFRICAINE',	'REPUBLIQUE DOMINICAINE',	'REPUBLIQUE TCHEQUE',	'ROUMANIE',	'ROYAUME-UNI (Londres)',	'RUSSIE (Moscou)',	'RWANDA',	'SAINT-CHRISTOPHE-ET-NIEVES',	'SAINTE-LUCIE',	'SAINT-VINCENT-ET-LES GRENADINES',	'SALVADOR',	'SAO TOME-ET-PRINCIPE',	'SENEGAL',	'SERBIE',	'SEYCHELLES',	'SIERRA LEONE',	'SINGAPOUR',	'SLOVAQUIE',	'SLOVENIE',	'SOMALIE',	'SOUDAN',	'SOUDAN DU SUD',	'SRI LANKA',	'SUEDE',	'SUISSE (autres villes)',
        'SURINAME',	'SWAZILAND',	'SYRIE',	'TADJIKISTAN',	'TAÏWAN',	'TANZANIE',	'TCHAD',	'THAILANDE',	'TIMOR ORIENTAL',	'TOGO',	'TRINITE-ET-TOBAGO',	'TUNISIE',	'TURKMENISTAN',	'TURQUIE (Ankara)',	'UKRAINE',	'URUGUAY',	'VANUATU',	'VENEZUELA',	'VIETNAM', 'YEMEN',	'ZAMBIE',	'ZIMBABWE'
    ))

    new_df=df[df.Country==p_select]  


    st.text('ire (base 100) en janvier 2009')
    new_df.iloc[0,1]
    st.text('ire en janvier 2023')
    new_df.iloc[0,6]

    new_df=df[df.Country==p_select]  

    graph = ptx.line(x = [2009,2012,2015,2018,2020,2023],
                    y =  [new_df.iloc[0,1],
    new_df.iloc[0,2],
    new_df.iloc[0,3],
    new_df.iloc[0,4],
    new_df.iloc[0,5],
    new_df.iloc[0,6]
    ], title="ire par année", labels={"x":"années","y":"Montants"})

    st.plotly_chart(graph)

authenticator.logout("Logout", "sidebar")
st.sidebar.title(f"Welcome {noms}")