import streamlit as st
import sqlite3
import pandas as pd
import pyodbc 

conn = sqlite3.connect('./data/hybrid.db')

current_user = ""
user_name = st.text_input("Username")
#conpy = pyodbc.connect('./data/hybrid.db')
if st.button("Login"):
    relate = "SELECT username,leftusername,rightusername FROM users WHERE (((users.username)=" + "'" + user_name + "'" + "));"
    relatefile = pd.read_sql(relate,conn,)
    current_user = list(relatefile['username'])
    level0,level0c,level0r = st.columns(3)
    with level0c:
        st.image("./pix/user.png",caption=  current_user,width=300,)

    level1l,level1c,level1r=st.columns(3)
    with level1l:
        st.image("./pix/user.png",caption = list(relatefile['leftusername']),width=300)
    with level1r:
        st.image("./pix/user.png",caption = list(relatefile['rightusername']),width=300)