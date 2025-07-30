# Credit_risk
# 💳 Projet de prédiction du Risque de Crédit (Pour débutant)
# 💼 Évaluation du risque client via une interface interactive

Ce projet vise à développer un outil capable d’estimer en temps réel le *risque de défaut de paiement d’un client* à partir de ses caractéristiques personnelles et financières. L'application permet une utilisation simple et rapide, notamment pour les *analystes de crédit* ou les * chargés de clientèle bancaire, dans le cadre de la ** prise de décision sur l’octroi d’un crédit *.

---

## 🎯 Objectif principal

- Construire un modèle fiable de *classification binaire* (bon / mauvais payeur).
- Fournir une *interface Web simple et interactive* permettant de tester différents profils client et de visualiser le résultat de la prédiction.
- Rendre le modèle *exploitable* par des non-spécialistes grâce à une application web légère avec *Streamlit*.

---

## 🛠 Technologies et outils utilisés

### 🧑‍💻 Langage :
- Python : Le langage principal pour la data science et le déploiement

### ⚙ Environnement & logiciels :
- Jupyter Notebook : exploration des données, prétraitement, modélisation
- Streamlit : développement de l’application web interactive

### 📚 Bibliothèques Python :
- *Analyse et manipulation de données* :
  - pandas : manipulation de tableaux de données
  - numpy : opérations numériques
- *Visualisation* :
  - matplotlib, seaborn : graphiques statistiques
- *Modélisation & machine learning* :
  - scikit-learn : création, évaluation et exportation du modèle
- *Web app & UI* :
  - streamlit : interface utilisateur interactive

### 📂 Autres fichiers importés :
- risk_prediction.pkl : modèle de machine learning enregistré
- Credit.csv : jeu de données prétraité pour la prédiction
- main.py : fonctions de nettoyage ou transformation

---

## 🧩 Étapes de conception

1. *Chargement et analyse des données*
   - Nettoyage, transformation des variables catégorielles
   - Visualisation de la distribution des classes
2. *Prétraitement des données*
   - Normalisation, encodage, gestion des valeurs déséquilibrées
3. *Modélisation*
   - Entraînement d’un modèle (ex. : régression logistique)
   - Évaluation (accuracy)
   - Export du modèle avec joblib
4. *Développement de l’application*
   - Interface utilisateur Streamlit
   - Chargement du modèle et des données
   - Formulaire interactif + affichage des résultats
5. *Déploiement local (ou en ligne si souhaité)*

---

## 🗂 Structure du projet
