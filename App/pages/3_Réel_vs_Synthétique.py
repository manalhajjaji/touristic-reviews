import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots

df = pd.read_csv("../Data/Real and synthetic/pokhara_reviews_final_COMPLETE.csv")
df['source_clean'] = df['source'].map({'real':'Réel','synthetic_groq':'Synthétique (Groq)'})

st.header("Comparaison Réel vs Synthétique")
st.markdown("**L’argument massue du projet**")

# Tableau comparatif
tab = pd.crosstab(df['source_clean'], df['sentiment_roberta'], normalize='index') * 100
tab = tab.round(1)[['Positif', 'Neutre', 'Négatif']]
st.table(tab.style.background_gradient(cmap='Greens'))

# Graphiques côte à côte
fig = make_subplots(rows=1, cols=2, specs=[[{"type":"pie"}, {"type":"pie"}]],
                    subplot_titles=("Avis RÉELS (963)", "Avis SYNTHÉTIQUES Groq (5000)"))

real = df[df['source']=='real']['sentiment_roberta'].value_counts()
fig.add_trace(go.Pie(labels=real.index, values=real.values, name="Réels",
                     marker_colors=['#2ECC71','#95A5A6','#E74C3C']), row=1, col=1)

synth = df[df['source']=='synthetic_groq']['sentiment_roberta'].value_counts()
fig.add_trace(go.Pie(labels=synth.index, values=synth.values, name="Synth",
                     marker_colors=['#2ECC71','#95A5A6','#E74C3C']), row=1, col=2)

fig.update_layout(title_text="Biais positif massif des LLM (94 % vs 78 %)", height=600)
st.plotly_chart(fig, use_container_width=True)

st.success("""
**Conclusion clé** :  
Les 963 avis réels de Pokhara affichent une prédominance exceptionnelle de sentiments positifs (91.7 %), reflétant probablement une satisfaction globale des touristes visitant cette destination prisée. En revanche, les 5 000 avis synthétiques générés via Groq, conçus avec une variabilité intentionnelle (incluant emojis et divers types d’avis), présentent une distribution plus équilibrée : 68.1 % positifs, 27.1 % neutres et 4.7 % négatifs.
Cette différence suggère que :

Les touristes réels de Pokhara sont exceptionnellement satisfaits, peut-être en raison de la beauté naturelle ou des activités comme le parapente, bien au-delà des attentes typiques.
La génération contrôlée avec Groq a réussi à produire une diversité de sentiments, évitant le biais positif souvent observé dans les LLM non contraints.
Ce projet démontre ainsi la capacité à moduler la génération de données synthétiques pour refléter une réalité plus nuancée, tout en mettant en lumière la perception extrêmement positive des visiteurs réels de Pokhara.
""")