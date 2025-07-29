import streamlit as st
import pandas as pd
import pickle
from sklearn.preprocessing import LabelEncoder

st.title("Résultat de la prédiction de risque")

st.sidebar.header("Caractéristiques du client")

def client_caract_entree():
    
    Credit_History = st.sidebar.selectbox('Historique de crédit', [0, 1, 2, 3, 4])
    Age = st.sidebar.slider('Age', 18, 75, 30)
    Gender = st.sidebar.selectbox('Genre', ['female', 'male'])
    Job = st.sidebar.selectbox('Emploi', [0, 1, 2, 3])
    Housing = st.sidebar.selectbox('Type de logement', ('own', 'rent', 'free'))
    Saving_accounts = st.sidebar.selectbox('Compte épargne', ('little', 'quite rich', 'rich', 'moderate'))
    CreditAmount = st.sidebar.slider('Montant du crédit', 250, 20000, 1000)
    Duration = st.sidebar.slider('Durée du crédit (mois)', 4, 72, 24)
    Purpose = st.sidebar.selectbox('Objet du crédit', ('car','domestic appliances','education','furniture/equipment','radio/TV'	,'repairs',	'vacation/others'))

    data = {
        'Credit History': Credit_History,
        'Age': Age,
        'Gender': Gender,
        'Job': Job,
        'Housing': Housing,
        'Saving accounts': Saving_accounts,
        'Credit amount': CreditAmount,
        'Duration': Duration,
        'Purpose': Purpose
    }
    return pd.DataFrame(data, index=[0])

input_df = client_caract_entree()

df = pd.read_csv('Credit.csv')

# Remplacer les valeurs manquantes de df avec par le mode
for col in df.columns:
    if df[col].isna().any():# Si on trouve un vrai dans la colonne booléenne des valeurs manquantes de la colonne col de df, (c'est-à-l'emplacement d'une valeur manquante)
        df[col] = df[col].fillna(df[col].mode()[0])# On remplace toutes les valeurs manquantes de col(d[col]) par le mode

data_client_input = df.drop(columns=['Risk'])

data_input= pd.concat([input_df, data_client_input], axis=0)

st.write(data_input[:1])

# Encodage des colonnes catégoriellles
var_cat = data_input.select_dtypes('object').columns
data_input= pd.get_dummies(data_input, columns =  var_cat, drop_first = True)


# Modele
model = pickle.load(open('risk_prediction.pkl', 'rb'))

prediction = model.predict(data_input[:1])[0]

st.subheader("Résultat de la prévision")
if st.button("Tester"):
    if prediction == 1 :
        st.success("Risque faible")
    else :
        st.error("Risque élevé")
            
