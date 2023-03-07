import streamlit as st
import pandas as pd
from sklearn.ensemble import RandomForestClassifier

Advert = pd.read_csv("https://github.com/Livetomuch/Liveto/blob/a6c8556261e3252bccf1c98c6c18b6dcd6956e98/Advertising.csv")
st.write("""
# Advertising to Sales Prediction App
""")

st.sidebar.header('User Input Parameters')
