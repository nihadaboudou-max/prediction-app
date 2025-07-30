import streamlit as st
import pandas as pd
from io import BytesIO

st.title("🎈 My new app")

# Configuration du dashboard
st.set_page_config(
    page_title="Dashboard de Prédiction",
    page_icon="📊",
    layout="centered"
)

st.title("Prédiction intelligente à partir de CSV")
st.markdown("Téléversez votre fichier CSV, et obtenez une **analyse prédictive intelligente** ")

st.sidebar.title("Paramètres")
st.sidebar.info("Ce tableau de bord vous permet d'analyser vos données automatiquement.")

col1, col2 = st.columns(2)

with col1:
   importer_file = st.file_uploader("Importer un fichier", type="csv")

with col2:
   sep= st.selectbox("Séparateur : Choisissez un séparateur adapter à votre fichier*", options=["-- Sélectionner --","," , ";" , "/" , "|" , "\t"])
if sep == "-- Sélectionner --":
    st.warning("Selectionner un séparateur")
     
if importer_file:
    try:
        #lecture du fichier reçu
        df = pd.read_csv(importer_file,sep=sep)

        st.success("Fichier chargé avec succès !")
        st.subheader("Aperçu des données")
        st.dataframe(df.head())

        # Prédiction des billets 
        st.subheader("Traitement des données")
        df["Prediction"] = df.select_dtypes(include="int64").sum(axis=1)

        st.success("Prédictions ajoutées à vos données !")

        # Télécharger le nouveau fichier CSV
        sortie_file = BytesIO()
        df.to_csv(sortie_file, index=False)
        sortie_file.seek(0)

        st.download_button(
            label="Télécharger les résultats",
            data=sortie_file,
            file_name="resultats_prediction.csv",
            mime="text/csv"
            
        )

    except Exception as e:
        st.error(f"Erreur lors de l'analyse du fichier : {e}")

else:
    st.warning("Veuillez téléverser un fichier CSV.")
