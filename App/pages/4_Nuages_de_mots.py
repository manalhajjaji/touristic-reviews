import streamlit as st
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("../Data/Real and synthetic/pokhara_reviews_final_COMPLETE.csv")

st.header("Nuages de mots")

col1, col2 = st.columns(2)

with col1:
    st.subheader("Avis RÉELS")
    real_text = " ".join(df[df['source']=='real']['review_clean'].dropna())
    wc_real = WordCloud(width=600, height=400, background_color='white', colormap='Reds').generate(real_text)
    plt.figure(figsize=(10,6))
    plt.imshow(wc_real, interpolation='bilinear')
    plt.axis('off')
    st.pyplot(plt)

with col2:
    st.subheader("Avis SYNTHÉTIQUES Groq")
    synth_text = " ".join(df[df['source']=='synthetic_groq']['review_clean'].dropna())
    wc_synth = WordCloud(width=600, height=400, background_color='white', colormap='Greens').generate(synth_text)
    plt.figure(figsize=(10,6))
    plt.imshow(wc_synth, interpolation='bilinear')
    plt.axis('off')
    st.pyplot(plt)