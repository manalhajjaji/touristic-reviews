
import streamlit as st
from PIL import Image
import os

st.set_page_config(page_title="Pokhara Sentiment Analysis", page_icon="⛰️", layout="wide")


image_path = "../app/assets/pokhara.webp"          


if os.path.exists(image_path):
    image = Image.open(image_path)

    # === IMAGE PLEIN ÉCRAN (nouvelle méthode sans warning) ===
    st.image(image, use_container_width=True)   # ← CORRIGÉ : use_container_width

    # === TITRE MAGNIFIQUE PAR-DESSUS L'IMAGE ===
    st.markdown("""
    <div style="position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%);
                background-color: rgba(0,0,0,0.65); padding: 25px 40px; border-radius: 20px;
                text-align: center; box-shadow: 0 8px 32px rgba(0,0,0,0.6);">
        <h1 style="color: white; margin:0; font-size: 3.5rem; text-shadow: 2px 2px 8px black;">
            Analyse des Sentiments<br>des Touristes à Pokhara
        </h1>
        <h3 style="color: #4ECDC4; margin:10px 0 0 0; font-weight: 300;">
            Projet IDSCC 3ème année • ENSA Oujda • 2025-2026
        </h3>
    </div>
    """, unsafe_allow_html=True)

else:
    st.error(f"Image non trouvée ! Chemin attendu : {image_path}")
    st.info("Place ton image dans app/assets/pokhara.jpg")

# === CONTENU EN DESSOUS DE L'IMAGE ===
st.markdown("<br><br><br><br><br><br><br><br><br><br>", unsafe_allow_html=True)  # espace

st.markdown("""
## Objectif du projet
Développer un système complet d’**analyse de sentiments** sur les avis touristiques de **Pokhara (Népal)**  
à partir de **5 963 avis** :  
- **963 avis réels** collectés  
- **5 000 avis synthétiques** générés via Groq (diversité contrôlée)

## Points forts du projet
- Comparaison unique **réel vs synthétique** (biais des LLM analysé)
- Deux modèles NLP : **VADER** + **RoBERTa (Transformer)**
- Dashboard interactif déployé dans le **Cloud** (Streamlit Community)
- Analyse approfondie : **statistiques, comparaisons, exemples, divergences**

""")

st.success("Utilise le menu à gauche pour explorer les résultats !")