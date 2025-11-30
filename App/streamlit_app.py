# app/streamlit_app.py
import streamlit as st
st.set_page_config(
    page_title="Analyse de Sentiments - Pokhara",
    page_icon="⛰️",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.title("⛰️ Analyse des Sentiments des Touristes à Pokhara")
st.markdown("**Projet IDSCC 3ème année • ENSA Oujda • Décembre 2025**")
st.sidebar.success("Navigation dans les pages →")