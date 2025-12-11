
# pages/2_Statistiques_Générales.py
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# ====================== CHARGEMENT DES DONNÉES ======================
df = pd.read_csv("../Data/Real and synthetic/pokhara_reviews_final_COMPLETE.csv")

# Création d'une colonne lisible
df['source_clean'] = df['source'].map({'real': 'Réel', 'synthetic_groq': 'Synthétique (Groq)'})

st.header("Statistiques Générales & Aperçu du Dataset")

# ====================== LIGNE 1 – 4 MÉTRIQUES ======================
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.metric("Total avis", f"{len(df):,}")
with col2:
    st.metric("Avis réels", f"{len(df[df['source']=='real']):,}")
with col3:
    st.metric("Avis synthétiques (Groq)", f"{len(df[df['source']=='synthetic_groq']):,}")
with col4:
    st.metric("Longueur moyenne", f"{df['review_length_words_clean'].mean():.0f} mots")

st.markdown("---")

# ====================== LIGNE 2 – DEUX CAMEMBERTS CÔTE À CÔTE (CORRIGÉ) ======================
st.subheader("Répartition des sentiments selon RoBERTa")

col1, col2 = st.columns(2)

# Couleurs identiques pour les deux graphiques → Positif vert, Neutre gris, Négatif rouge
colors = ['#2ECC71', '#95A5A6', '#E74C3C']  # vert, gris, rouge

with col1:
    real_counts = df[df['source']=='real']['sentiment_roberta'].value_counts()
    fig1 = go.Figure(data=[go.Pie(
        labels=real_counts.index,
        values=real_counts.values,
        hole=0.45,
        marker_colors=colors,
        textinfo='label+percent',
        textposition='inside'
    )])
    fig1.update_layout(title="Avis RÉELS (963)", title_x=0.5)
    st.plotly_chart(fig1, use_container_width=True)

with col2:
    synth_counts = df[df['source']=='synthetic_groq']['sentiment_roberta'].value_counts()
    fig2 = go.Figure(data=[go.Pie(
        labels=synth_counts.index,
        values=synth_counts.values,
        hole=0.45,
        marker_colors=colors,
        textinfo='label+percent',
        textposition='inside'
    )])
    fig2.update_layout(title="Avis SYNTHÉTIQUES Groq (5 000)", title_x=0.5)
    st.plotly_chart(fig2, use_container_width=True)

st.markdown("---")

# ====================== LIGNE 3 – BOXPLOT + BARRE EMOJIS ======================
st.subheader("Caractéristiques textuelles")

col1, col2 = st.columns(2)

with col1:
    fig_box = px.box(
        df, x='source_clean', y='review_length_words_clean',
        color='source_clean',
        color_discrete_sequence=['#E74C3C', '#2ECC71'],
        title="Longueur des avis (en mots)"
    )
    fig_box.update_layout(showlegend=False, xaxis_title="", yaxis_title="Nombre de mots")
    st.plotly_chart(fig_box, use_container_width=True)

with col2:
    emoji_rate = (df.groupby('source_clean')['has_emoji'].mean() * 100).round(1)
    fig_emoji = go.Figure(go.Bar(
        x=emoji_rate.index,
        y=emoji_rate.values,
        text=emoji_rate.astype(str) + ' %',
        textposition='outside',
        marker_color=['#E74C3C', '#2ECC71']
    ))
    fig_emoji.update_layout(title="Taux d'utilisation d'émojis", yaxis_title="Pourcentage", yaxis_range=[0, 100])
    st.plotly_chart(fig_emoji, use_container_width=True)

st.markdown("---")

# ====================== LIGNE 4 – TOP 10 MOTS ======================
st.subheader("Top 10 mots les plus fréquents")

col1, col2 = st.columns(2)

with col1:
    real_top = pd.Series(' '.join(df[df['source']=='real']['review_clean'].dropna()).lower().split()).value_counts().head(10)
    fig_real = px.bar(y=real_top.index, x=real_top.values, orientation='h',
                      title="Avis RÉELS", color_discrete_sequence=['#E74C3C'])
    fig_real.update_layout(yaxis_autorange="reversed", showlegend=False, height=400)
    st.plotly_chart(fig_real, use_container_width=True)

with col2:
    synth_top = pd.Series(' '.join(df[df['source']=='synthetic_groq']['review_clean'].dropna()).lower().split()).value_counts().head(10)
    fig_synth = px.bar(y=synth_top.index, x=synth_top.values, orientation='h',
                       title="Avis SYNTHÉTIQUES", color_discrete_sequence=['#2ECC71'])
    fig_synth.update_layout(yaxis_autorange="reversed", showlegend=False, height=400)
    st.plotly_chart(fig_synth, use_container_width=True)

# ====================== FIN – ACCORD ENTRE MODÈLES ======================
st.markdown("---")
st.subheader("Fiabilité des modèles")
accord = (df['sentiment_vader'] == df['sentiment_roberta']).mean()
st.success(f"**{accord:.1%}** des avis ont le même résultat entre VADER et RoBERTa")

# Mini tableau croisé
cross = pd.crosstab(df['sentiment_vader'], df['sentiment_roberta'], margins=False)
st.dataframe(cross.style.background_gradient(cmap="Greens"))

#st.caption("Toutes les visualisations sont générées en temps réel • Projet réalisé par [Ton Nom] • Décembre 2025")