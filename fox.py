import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
import re 



st.set_page_config(page_title="Fox 40 News", layout="wide")

st.title('News articles that are happening now')
st.write("These are news articles that have been shared by Fox 40, telling stories about what is happening in the world." )

data = pd.read_csv('fox_news_data.csv') 

# Dropdown for first letter filtering
first_letters = sorted(data['First Letter'].unique())  
selected_first_letter = st.selectbox('Select First Letter:', ['All'] + list(first_letters))

# Slider for article length
min_length = int(data['Article'].apply(len).min())
max_length = int(data['Article'].apply(len).max())
article_length = st.slider('Article Length', min_value=min_length, max_value=max_length, value=min_length)

# Filter data based on selected first letter
if selected_first_letter != 'All':
    filtered_data = data[data['First Letter'] == selected_first_letter]
else:
    filtered_data = data.copy()

# Apply length filter after filtering by first letter
filtered_data = filtered_data[filtered_data['Article'].apply(len) <= article_length]

st.dataframe(filtered_data, hide_index=True, 
         column_config={"Article Link": st.column_config.LinkColumn(display_text="Link")})
