import streamlit as st
from PIL import Image

with st.expander('Start Camera'):
    #start the camera
    user_image = st.camera_input('Camera')

if user_image:
    #Create a pillow image
    img = Image.open(user_image)
    
    #Convert image into grayscale
    gray_img = img.convert('L')
    
    #render the grayscale image on local server
    st.image(gray_img)