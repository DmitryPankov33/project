import streamlit as st
import pandas as pd
import plotly.express as px

df = pd.read_csv(r'C:\Users\dmitr\web_app_project\project\vehicles_us.csv')

st.header('Choose your car!')

st.caption('red:[Choose your parameters here]')

price_range=st.slider(
    "What is your price range?",
    value=(500,34600)
)
actual_range=list(range(price_range[0],price_range[1]+1))

hungry_car = st.checkbox('Only hungry cars')

if hungry_car:
    filtered_data=df[df.price.isin(actual_range)]
    filtered_data=filtered_data[df.odometer<=80000]
else:
    filtered_data=df[df.price.isin(actual_range)]

st.write('Here are the options with the split by price and odometer readings')

fig = px.scatter(filtered_data,x='price', y='odometer', title='Price vs Odometer Readings')
st.plotly_chart(fig)

st.write('Distribution of model years of the cars')
fig2 = px.histogram(filtered_data,x='model_year', title='Histogram of model year')
st.plotly_chart(fig2)
