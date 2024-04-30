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

# Checkbox for article length
small_checkbox = st.checkbox("Small (<= 30,000 characters)")
medium_checkbox = st.checkbox("Medium (30,000 - 60,000 characters)")
large_checkbox = st.checkbox("Large (> 60,000 characters)")


# Filter data based on selected first letter
if selected_first_letter != 'All':
    filtered_data = data[data['First Letter'] == selected_first_letter]
else:
    filtered_data = data.copy()

# Apply length filter based on checkboxes
if small_checkbox:
    filtered_data = filtered_data[filtered_data['Article'].apply(len) <= 10000]
if medium_checkbox:
    filtered_data = filtered_data[(filtered_data['Article'].apply(len) > 10000) & (filtered_data['Article'].apply(len) <= 40000)]
if large_checkbox:
    filtered_data = filtered_data[filtered_data['Article'].apply(len) > 40000]


st.dataframe(filtered_data, hide_index=True, 
         column_config={"Article Link": st.column_config.LinkColumn(display_text="Link")})
