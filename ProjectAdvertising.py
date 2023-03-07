import streamlit as st
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

st.write("""
# Advertising to Sales Prediction App
by Linear Regression
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

df_train = pd.read_csv('Advertising.csv')

X_train = df_train[['TV', 'Radio', 'Newspaper']]
y_train = df_train['Sales']

reg = LinearRegression()
reg.fit(X_train, y_train)

X_test = df[['TV', 'Radio', 'Newspaper']]
y_pred = reg.predict(X_test)

st.subheader('Prediction')
st.write(y_pred)
