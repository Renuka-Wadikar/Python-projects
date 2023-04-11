import streamlit as st
import pandas

st.set_page_config(layout='wide')
col1, col2 = st.columns([1.5,5])

with col1:
    st.image('images/photo.jpg')

with col2:
    st.title("Renuka Wadikar")
    content = """Hi, I am Renuka! As a recent graduate in Computer Science
    with a keen interest in programming,I have developed a strong passion for 
    the world of Python programming. With a solid foundation in the principles
    of software engineering and a deep understanding of programming concepts,
    I am confident in my ability to create complex and efficient software solutions.
    
    My experience includes hands-on work with Python programming, including building
    web applications, data analysis and visualization, and machine learning.
    I have also worked on various projects, from simple scripts to complex applications.
    
    Through this site, I aim to share all the projects ,I created while learning the language"""
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
