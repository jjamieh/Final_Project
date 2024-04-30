import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
import re 



st.set_page_config(page_title="Fox 40 News", layout="wide")

st.title('News articles that are happening now')
st.write("These are news articles that have been shared by Fox 40, telling stories about what is happening in the world." )

data = pd.read_csv('fox_news_data.csv') 

# Extract keywords from articles
def extract_keywords(article):
    keywords = re.findall(r'\b\w{5,}\b', article)  # Extract words with 5 or more characters
    return keywords

data['Keywords'] = data['Article'].apply(extract_keywords)

# Define the keywords you want to include in the dropdown box
selected_keywords = ['battle', 'election', 'athlete', 'FBI', 'law', 'animal', 'political', 'AI']

# Dropdown for keyword filtering
selected_keyword = st.selectbox('Select Keyword:', ['All'] + sorted(selected_keywords))

# Checkbox for article length
small_checkbox = st.checkbox("Small (<= 10,000 characters)")
medium_checkbox = st.checkbox("Medium (10,000 - 40,000 characters)")
large_checkbox = st.checkbox("Large (> 40,000 characters)")


# Filter data based on selected keyword
if selected_keyword != 'All':
    filtered_data = data[data['Keywords'].apply(lambda x: selected_keyword in x)]
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
