import streamlit as st
import pandas as pd

# Read the CSV file into a pandas DataFrame
url = 'https://raw.githubusercontent.com/livetomuch/liveto/main/Advertising.csv'
df = pd.read_csv(url)

# Display the data in Streamlit using st.write()
st.write(df)
