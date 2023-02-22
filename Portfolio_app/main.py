import streamlit as st
import pandas

st.set_page_config(layout='wide')
col1, col2 = st.columns(2)

with col1:
    st.image('images/photo.jpg')

with col2:
    st.title("Renuka Wadikar")
    content = """Hi, I am Renuka! I am a aspiring python programmer and python enthusiast.
    I graduated in 2020 with BE in Computer Science.I love to learn things  by expermeting with the code.
    This website is showcase of various aaplication buil by me , while learning the language.
    Hope you enjoy the website!!!"""
    st.info(content)
    
col3,empty_col,col4 = st.columns([1.5,0.5,1.5])

df = pandas.read_csv('data.csv', sep=';')

with col3:
    for index,row in df[:10].iterrows():
        st.header(row['title'])
        st.write(row['description'])
        st.image("images/" + row['image'])
        st.write(f"[Source code]({row['url']})")

with col4:
    for index,row in df[10:].iterrows():
        st.header(row['title']) 
        st.write(row['description'])
        st.image("images/" + row['image'])
        st.write(f"[Source code]({row['url']})")
