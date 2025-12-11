# Analyse des Sentiments des Touristes à Pokhara (Népal)

**Projet de module – IDSCC 3ème année Cycle Ingénieur**  
**ENSA Oujda – Année Universitaire 2025-2026**

- **Module** : Internet of Things (IoT)
- **Date** :  Décembre 2025


---

##  Objectif du projet

Développer un système complet d'**analyse de sentiments** sur les avis touristiques de **Pokhara** à partir de **5 963 avis** :

- 963 avis réels
- 5 000 avis synthétiques générés via **Groq** (diversité contrôlée : positif, neutre, négatif + emojis)

### Modèles NLP utilisés

- **VADER** (règles + lexique)
- **RoBERTa** (Transformer – `cardiffnlp/twitter-roberta-base-sentiment-latest`)

---

##  Points forts du projet

- Comparaison inédite **réel vs synthétique** (biais des LLM quantifié)
- Pipeline ETL complet exécuté dans le **Cloud**
- Dashboard interactif riche (7 pages, +25 visualisations)
- Déploiement public sur **Streamlit Community Cloud**

🌐 **Dashboard en ligne** : [https://pokhara-sentiment-analysis.streamlit.app](https://pokhara-sentiment-analysis.streamlit.app)

---

##  Structure du projet

```
TOURISTIC-REVIEWS/
├── App/                  → Dashboard Streamlit (7 pages)
│   ├── assets/           → Image de Pokhara
│   └── pages/            → Pages du dashboard
├── Data/                 → Données brutes et finales
├── requirements.txt      → Dépendances (pandas, plotly, etc.)
└── README.md             → Ce fichier
```

---

##  Installation & exécution en local

### 1. Cloner le projet

```bash
git clone https://github.com/ton-pseudo/TOURISTIC-REVIEWS.git
cd TOURISTIC-REVIEWS
```

### 2. Installer les dépendances

```bash
pip install -r requirements.txt
```

### 3. Lancer le dashboard

```bash
streamlit run App/streamlit_app.py
```

Le dashboard s'ouvre automatiquement dans votre navigateur.

---

##  Déploiement Cloud

L'application est déployée en permanence sur :  
🔗 [https://manalhajjaji-touristic-reviews-appstreamlit-app-k4nc4t.streamlit.app/](https://manalhajjaji-touristic-reviews-appstreamlit-app-k4nc4t.streamlit.app/)

Pipeline ETL complet exécuté dans le Cloud (Streamlit Community Cloud).

### Conformité au cahier des charges

-  Maîtrise du NLP (pré-traitement, VADER, Hugging Face Transformers)
-  Pipeline ETL dans un environnement Cloud
-  Dashboard interactif
-  Code source public sur GitHub

---

##  Technologies utilisées

- **Python** – pandas – NLTK – Hugging Face Transformers
- **Plotly** – WordCloud – Streamlit
- **Groq** (génération des 5 000 avis synthétiques)
- **Streamlit Community Cloud** (hébergement)

---

##  Auteur

**[Manal Hajjaji]**  
Étudiante IDSCC 3ème année – ENSA Oujda  
Décembre 2025


---

##  Licence

Ce projet est réalisé dans un cadre académique.