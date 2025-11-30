import streamlit as st
import pandas as pd

df = pd.read_csv("../Data/Real and synthetic/pokhara_reviews_final_COMPLETE.csv")

st.header("Exemples d’avis & Divergences VADER / RoBERTa")

div = df[df['sentiment_vader'] != df['sentiment_roberta']]

st.markdown(f"**{len(div)} avis** où VADER et RoBERTa divergent → cas très intéressants")
exemple = div.sample(5, random_state=42)

for i, row in exemple.iterrows():
    st.markdown(f"**Source** : {row['source_clean']}")
    st.write(f"**VADER** → {row['sentiment_vader']} | **RoBERTa** → {row['sentiment_roberta']}")
    st.code(row['review_clean'][:500] + "...", language=None)
    st.markdown("---")