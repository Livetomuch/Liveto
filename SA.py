import streamlit as st
import pandas as pd

url = 'https://raw.githubusercontent.com/livetomuch/liveto/main/Advertising.csv'
df = pd.read_csv(url)

st.write(df)
