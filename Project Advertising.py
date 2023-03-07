import streamlit as st
import pandas as pd
import numpy as np
from sklearn import datasets
from sklearn.ensemble import linearregression


st.write("""
# Advertising to Sales Prediction App
""")

st.sidebar.header('User Input Parameters')

def user_input_features():
    TV = st.sidebar.slider('TV', 0, 200, 54)
    Radio = st.sidebar.slider('Radio', 0, 100, 30)
    Newspaper = st.sidebar.slider('Newspaper', 0, 100, 20)
    data = {'TV': TV,
            'Radio': Radio,
            'Newspaper': Newspaper,}
    features = pd.DataFrame(data, index=[0])
    return features

df = user_input_features()

st.subheader('User Input parameters')
st.write(df)

#url = 'https://raw.githubusercontent.com/livetomuch/liveto/main/Advertising.csv'
#Advert = pd.read_csv(url)
df = pd.read_csv('Advertising.csv')

X = df.drop('Sales',axis = 1)
Y = df.Sales

clf = RandomForestClassifier()
clf.fit(X, Y)

prediction = clf.predict(df)
prediction_proba = clf.predict_proba(df)

st.subheader('Prediction')
st.write(prediction)

st.subheader('Prediction Probability')
st.write(prediction_proba)
