import os
import streamlit as st
from dotenv import load_dotenv

# 1. On tente le local (.env)
load_dotenv()
# --- RÉCUPÉRATION SÉCURISÉE DE LA CLÉ ---
api_key = os.getenv("GROQ_API_KEY")

# On utilise un bloc try/except pour éviter que l'app disparaisse
try:
    if not api_key and "GROQ_API_KEY" in st.secrets:
        api_key = st.secrets["GROQ_API_KEY"]
except Exception:
    # Si les secrets ne sont pas configurés sur Streamlit Cloud, on ne crash pas
    api_key = None

# 2. Configuration
st.set_page_config(page_title="MoMoFr", page_icon="🤖", layout="centered")

# --- STYLE CSS AVANCÉ (PRO, CLASSE, PREMIUM) ---
st.markdown("""
<style>
    /* 1. FOND DE PAGE LÉGER POUR LE CONTRASTE */
    .stApp {
        background-color: #f8f9fa; /* Gris très clair pour faire ressortir les bulles blanches */
    }

    /* 2. FIXER L'ENTÊTE EN HAUT (PRO) */
    .stAppHeader { display: none; } /* Cache le header Streamlit */
    
    .fixed-header {
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        background-color: white; /* Fond blanc pur pour l'entête */
        z-index: 1000;
        padding: 25px 0;
        border-bottom: 1px solid #ececf1; /* Bordure fine et claire */
        text-align: center;
        box-shadow: 0 4px 12px rgba(0,0,0,0.03); /* Ombre portée très subtile */
    }

    .momo-title {
        font-family: 'Inter', sans-serif;
        font-size: 42px !important;
        font-weight: 900 !important;
        text-transform: uppercase;
        letter-spacing: 1px;
        margin: 0;
        color: #1a1a1a;
    }

    .france-line {
        height: 4px;
        width: 140px;
        margin: 10px auto;
        background: linear-gradient(to right, #0055A4 33%, #f0f2f6 33%, #f0f2f6 66%, #EF4135 66%);
        border-radius: 2px;
    }

    /* 3. STYLE DES BULLES DE CHAT (ENCADREMENT CLASSE) */
    .stChatMessage {
        background-color: white !important; /* Bulles blanches */
        border: 1px solid #ececf1 !important; /* Bordure fine et pro */
        border-radius: 16px !important; /* Arrondis modernes */
        margin-bottom: 12px !important; /* Espace entre les messages */
        padding: 18px !important; /* Aération interne */
        box-shadow: 0 2px 5px rgba(0,0,0,0.015) !important; /* Ombre de carte légère */
    }

    /* Style spécifique pour les messages de l'utilisateur (optionnel) */
    [data-testid="stChatMessage"] {
        border-color: #f0f2f6 !important;
    }

    /* 4. AJUSTEMENT DE L'ESPACE DE CHAT (POUR L'ENTÊTE FIGÉE) */
    .chat-container {
        margin-top: 190px; /* Espace compensatoire pour l'entête fixed */
        margin-bottom: 90px; /* Espace pour la barre de saisie */
    }

    /* Style de la barre de saisie */
    .stChatInputContainer {
        border-color: rgba(0, 85, 164, 0.3) !important; /* Bordure discrète */
        background-color: white !important;
    }
</style>
""", unsafe_allow_html=True)

# --- ENTÊTE IMMOBILE ET STYLISÉE (HEADER) ---
st.markdown("""
<div class="fixed-header">
    <h1 class="momo-title">MOMOFR</h1>
    <div class="france-line"></div>
    <p style="color: #6e6e80; margin: 6px 0 0 0; font-size: 1.1rem; font-style: italic;">
        Je suis ravie d'échanger avec vous ! 
    </p>
</div>
<div style="height: 180px;"></div> """, unsafe_allow_html=True)


# --- ZONE DE RÉPONSES (DÉROULANTE ET ENCADRÉE PROPREMENT) ---
# Tout ce qui est ici va défiler sous l'entête
chat_placeholder = st.container()

with chat_placeholder:
    # Initialisation de l'historique dans la session
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Affichage des messages encadrés proprement
    for m in st.session_state.messages:
        with st.chat_message(m["role"]):
            st.markdown(m["content"])


# --- LOGIQUE DU CHAT ---
if api_key:
    try:
        from langchain_groq import ChatGroq

        # Modèle Llama 3.1 réactif
        llm = ChatGroq(
            temperature=0.7,
            groq_api_key=api_key,
            model_name="llama-3.1-8b-instant"
        )

        # BARRE DE SAISIE (Fixée en bas par nature dans Streamlit)
        if prompt := st.chat_input("Dites-moi tout..."):
            # 1. Ajouter le message utilisateur à l'historique
            st.session_state.messages.append({"role": "user", "content": prompt})
            with chat_placeholder:
                with st.chat_message("user"):
                    st.markdown(prompt)

            # 2. Générer la réponse de MoMoFr
            with chat_placeholder:
                with st.chat_message("assistant"):
                    with st.spinner("MoMoFr écrit sa réponse..."):
                        try:
                            # Requête au modèle
                            response = llm.invoke(prompt)
                            answer = response.content
                            
                            # Affichage de la réponse
                            st.markdown(answer)
                            st.session_state.messages.append({"role": "assistant", "content": answer})
                        
                        except Exception as e:
                            st.error(f"❌ Oups, petit souci : {e}")

            # On force le rafraîchissement pour que les messages s'affichent instantanément
            st.rerun()

    except Exception as e:
        st.error(f"⚠️ Erreur système : {e}")

# --- BARRE LATÉRALE ---
with st.sidebar:
    st.title("⚙️ Options")
    st.caption("Gérez votre conversation ici.")
    if st.button("🗑️ Effacer la conversation"):
        st.session_state.messages = []
        st.rerun()