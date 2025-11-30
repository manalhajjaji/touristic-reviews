import streamlit as st
import pandas as pd
import plotly.express as px

df = pd.read_csv("../Data/Real and synthetic/pokhara_reviews_final_COMPLETE.csv")

st.header("Statistiques Générales")

col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Total avis", len(df))
with col2:
    st.metric("Avis réels", len(df[df['source']=='real']))
with col3:
    st.metric("Avis synthétiques (Groq)", len(df[df['source']=='synthetic_groq']))

st.markdown("### Répartition globale des sentiments (RoBERTa - modèle le plus fiable)")

fig = px.pie(
    df['sentiment_roberta'].value_counts(),
    values='count', names=df['sentiment_roberta'].value_counts().index,
    color_discrete_sequence=['#2ECC71', '#95A5A6', '#E74C3C'],
    title="Répartition globale (tous les 5963 avis)"
)
st.plotly_chart(fig, use_container_width=True)