import streamlit
import pandas as pd

streamlit.title('My Parents New Healthy Diner')

streamlit.header('Breakfast Favorites')
streamlit.text('🥣 Omega 3 & blueberry Oatmeal')
streamlit.text('Greek yogurt')
streamlit.text('Chia seeds')
streamlit.text('High protein chia pudding recipe')

streamlit.header('Build Your Own Fruit Smoothie')
my_fruit_list = pd.read_csv('https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt')
streamlit.multiselect("Pick Some fruits:", list(my_fruit_list.index))
streamlit.dataframe(my_fruit_list)
