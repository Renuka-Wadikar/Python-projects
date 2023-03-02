import streamlit as st
import plotly.express as px
from backend import get_data

st.header('Weather Forecast for Next Days')

place = st.text_input("Place:")
days = st.slider('Forecast Days', min_value=1, max_value=5,
                 help= 'Select number of forecasted days')
option = st.selectbox("Select data to view", 
                      ('Temperature','Sky'))
try:
    if place:
        st.subheader(f'Temperature for the next {days} days in place {place}')

        #Get temperature/sky data
        data = get_data(place,days)

        if option == 'Temperature':
            
            temperatres = [dict['main']['temp'] / 10 for dict in data]
            dates = [dict['dt_txt'] for dict in data] 
            figure = px.line(x= dates, y= temperatres, 
                            labels={'x':'Dates','y':'Temperature (C)'})
            st.plotly_chart(figure)

        if option =='Sky':
            images = {'Clear': 'images/clear.png','Clouds': 'images/cloud.png',
                    'Rain': 'images/rain.png','Snow': 'images/snow.png',}
            sky_conditions = [dict['weather'][0]['main'] for dict in data]
            filepaths = [images[condition] for condition in sky_conditions]
            st.image(filepaths,width=115)
except KeyError:
    st.write('City does not exit')

