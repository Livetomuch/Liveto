import streamlit as st
import pandas as pd
from sklearn.ensemble import RandomForestClassifier

url = 'https://raw.githubusercontent.com/livetomuch/liveto/main/Advertising.csv'
Advert = pd.read_csv(url)
st.write("""
# Advertising to Sales Prediction App
""")

st.sidebar.header('User Input Parameters')
