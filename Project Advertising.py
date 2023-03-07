import streamlit as st
import pandas as pd
import numpy as np
from sklearn import datasets
from sklearn.ensemble import RandomForestClassifier


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
Advert = pd.read_csv('Advertising2 (1).csv')

Advert['Sales'] = pd.cut(Advert['Sales'], bins=[0, 30, 60, 90, 120], labels=['0-30', '30-60', '60-90', '90-120'])

X = Advert.drop('Sales',axis = 1)
Y = Advert['Sales']

clf = RandomForestClassifier()
clf.fit(X, Y)

prediction = clf.predict(df)
prediction_proba = clf.predict_proba(df)

st.subheader('Class labels and their corresponding index number')
st.subheader('Class labels')
st.write(['0-30', '30-60', '60-90', '90-120'])

st.subheader('Prediction')
st.write(prediction)

st.subheader('Prediction Probability')
st.write(prediction_proba)
