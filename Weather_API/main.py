import streamlit as st
import plotly.express as px
st.header('Weather Forecast for Next Days')

place = st.text_input("Place:")
days = st.slider('Forecast Days', min_value=1, max_value=5,
                 help= 'Select number of forecasted days')
option = st.selectbox("Select data to view", 
                      ('Temperature','Sky'))

st.subheader(f'Temperature for the next {days} days in place {place}')


dates = ['2022-25-10','2022-26-10','2022-27-10']
temperature = [9, 10, 5]
figure = px.line(x= dates, y= temperature, 
                 labels={'x':'Dates','y':'Temperature (C)'})
st.plotly_chart(figure)
