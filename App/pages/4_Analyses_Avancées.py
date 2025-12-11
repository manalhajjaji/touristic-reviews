

# pages/4_Analyses_Avancées.py
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import numpy as np
from collections import Counter
import re

df = pd.read_csv("Data/Real and synthetic/pokhara_reviews_final_COMPLETE.csv")
df['source_clean'] = df['source'].map({'real': 'Réel', 'synthetic_groq': 'Synthétique'})

st.header("Analyses Avancées & Insights Uniques")
#st.markdown("Visualisations")

# ====================== 1. ÉVOLUTION DU SCORE DE CONFIANCE ======================
st.subheader("1. Score de confiance moyen de RoBERTa")
conf = df.groupby(['source_clean', 'sentiment_roberta'])['confidence_roberta'].mean().round(3)
conf = conf.unstack().fillna(0)
fig = px.bar(conf, barmode='group', color_discrete_sequence=['#27AE60', '#95A5A6', '#E74C3C'],
             title="RoBERTa est beaucoup plus confiant sur les avis positifs ")
st.plotly_chart(fig, use_container_width=True)

# ====================== 2. TOP 10 ADJECTIFS PAR SENTIMENT (RÉELS UNIQUEMENT) ======================
st.subheader("2. Quels adjectifs utilisent vraiment les touristes ? (avis réels)")
from collections import Counter
import re

def extract_adjectives(text):
    words = re.findall(r'\b\w+\b', text.lower())
    adj = ['beautiful','amazing','wonderful','great','nice','stunning','peaceful','awesome','fantastic','lovely',
            'bad','expensive','dirty','crowded','disappointing','poor','terrible','overrated']
    return [w for w in words if w in adj]

real_adj = df[df['source']=='real']['review_clean'].dropna().apply(extract_adjectives)
top_adj = pd.Series(Counter([item for sublist in real_adj for item in sublist])).sort_values(ascending=False).head(10)

fig = px.bar(x=top_adj.values, y=top_adj.index, orientation='h',
             title="Top 10 adjectifs dans les avis réels", color_discrete_sequence=['#E74C3C'])
fig.update_layout(yaxis_autorange="reversed")
st.plotly_chart(fig, use_container_width=True)

# ====================== 3. SENTIMENT MOYEN SELON LA LONGUEUR (CORRIGÉ) ======================
st.subheader("3. Les avis courts sont-ils plus extrêmes ?")
bins = [0, 20, 50, 100, 200, 1000]
labels = ['<20 mots', '20-50', '50-100', '100-200', '>200 mots']
df['length_bin'] = pd.cut(df['review_length_words_clean'], bins=bins, labels=labels)

# On recrée le score numérique proprement
df['score_numeric'] = df['sentiment_roberta'].map({'Positif': 1, 'Neutre': 0, 'Négatif': -1})

mean_by_len = df.groupby(['length_bin', 'source_clean'], observed=True)['score_numeric'].mean().unstack()

fig = px.line(mean_by_len, markers=True, color_discrete_sequence=['#E74C3C', '#2ECC71'],
              title="Plus l'avis est long → plus le sentiment devient nuancé (surtout chez les synthétiques)")
fig.update_yaxes(range=[-0.3, 1.1], title="Score moyen (1=Positif, -1=Négatif)")
st.plotly_chart(fig, use_container_width=True)

# ====================== 4. TAUX D'EMOJIS PAR SENTIMENT ======================
st.subheader("4. Les emojis sont-ils corrélés au sentiment ?")
emoji_by_sent = df.groupby(['sentiment_roberta', 'source_clean'])['has_emoji'].mean()*100
emoji_by_sent = emoji_by_sent.unstack()
fig = px.bar(emoji_by_sent, barmode='group', title="Les avis positifs contiennent 3× plus d'emojis (surtout chez les vrais touristes)")
st.plotly_chart(fig, use_container_width=True)

# ====================== 5. NUAGE DE POINTS : LONGUEUR vs SCORE DE CONFIANCE ======================
st.subheader("5. Longueur vs Confiance de RoBERTa")
fig = px.scatter(df.sample(2000), x='review_length_words_clean', y='confidence_roberta',
                 color='source_clean', opacity=0.6,
                 color_discrete_sequence=['#E74C3C','#2ECC71'],
                 title="RoBERTa est plus confiant sur les avis courts et positifs")
fig.update_xaxes(range=[0, 400])
st.plotly_chart(fig, use_container_width=True)

# ====================== 6. TOP 10 MOTS LES PLUS "TYPIQUES" DE CHAQUE SOURCE ======================
st.subheader("6. Mots les plus caractéristiques de chaque source")
real_text = " ".join(df[df['source']=='real']['review_clean'].dropna())
synth_text = " ".join(df[df['source']=='synthetic_groq']['review_clean'].dropna())

real_words = Counter(re.findall(r'\b[a-zA-Z]{4,}\b', real_text.lower())).most_common(15)
synth_words = Counter(re.findall(r'\b[a-zA-Z]{4,}\b', synth_text.lower())).most_common(15)

col1, col2 = st.columns(2)
with col1:
    st.write("**Mots typiques des avis RÉELS**")
    st.dataframe(pd.DataFrame(real_words, columns=['Mot', 'Fréquence']).set_index('Mot'))
with col2:
    st.write("**Mots typiques des avis SYNTHÉTIQUES**")
    st.dataframe(pd.DataFrame(synth_words, columns=['Mot', 'Fréquence']).set_index('Mot'))
#st.plotly_chart(fig, use_container_width=True)

# ====================== 8. CONCLUSION FINALE ======================
