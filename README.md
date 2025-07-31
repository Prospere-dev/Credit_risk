# Credit_risk
# 💳 Projet de prédiction du Risque de Crédit (Pour débutant)
# 💼 Évaluation du risque client via une interface interactive

Ce projet vise à développer un outil capable d’estimer en temps réel le *risque de défaut de paiement d’un client* à partir de ses caractéristiques personnelles et financières. L'application permet une utilisation simple et rapide, notamment pour les *analystes de crédit* ou les *chargés de clientèle bancaire*, dans le cadre de la *prise de décision sur l’octroi d’un crédit*.

---

## 🎯 Objectif principal

- Construire un modèle fiable de *classification binaire* (bon payeur = Risque faible / mauvais payeur = Risque élevé).
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
   - Analyse du fond et de la forme du tableau de données
   - Analyse des valeurs manquantes et des variables
   - Analyse (visualisation) graphique de la relation entre les variables
2. *Prétraitement des données*
   - Normalisation(Standarisation), encodage, gestion des valeurs déséquilibrées
3. *Modélisation*
   - Entraînement d’un modèle 
   - Évaluation (accuracy,cross_val_score)
   - Export du modèle avec Pickle
4. *Développement de l’application*
   - Interface utilisateur Streamlit
   - Chargement du modèle et des données
   - Formulaire interactif + affichage des résultats
5. *Déploiement local (ou en ligne si souhaité)*

---
## 🗂 Structure du projet

Project/
│
├── Web application/             # Dossier contenant l'application Streamlit
│   ├── main.py                  # Script principal de l'application
│   ├── requirements.txt         # Dépendances Python nécessaires à l'application
│   ├── data.csv                 # Données utilisées pour l'interface utilisateur
│   ├── model.pkl                # Modèle de machine learning pré-entraîné
│
├── notebook.ipynb               # Notebook Jupyter : exploration et entraînement du modèle
├── README.md                    # Documentation du projet

---

## 🚀 Lancement de l'application Streamlit (localement)

> Ouvre un terminal et suis ces étapes :


1. Cloner le projet (ou naviguer dans le dossier)

Entrer dans le terminal (de préférence celui d'Anaconda ou autres)
```
git clone https://github.com/Prospere-dev/Credit_risk.git 
```
Puis entrer
```
cd Credit_risk\Projet de prédiction du risque de crédit\Application web de prédiction du risque de crédit
```
2. Installer les dépendances (Streamlit,Pandas,Scikit_learn,Seaborn,Matplotlib) si vous ne les avez pas (aussi disponible sur Jupiter note book d'anaconda)
```
pip install -r requirements.txt
```
3. Lancer l’application
```
streamlit run main.py
```
