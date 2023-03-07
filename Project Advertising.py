import streamlit as st
import pandas as pd
from sklearn.ensemble import RandomForestClassifier

Advert = pd.read_csv("Advertising.csv")
st.write("""
# Advertising to Sales Prediction App
""")

st.sidebar.header('User Input Parameters')
