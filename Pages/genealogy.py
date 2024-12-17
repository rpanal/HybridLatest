import streamlit as st
import sqlite3
import pandas as pd

conn = sqlite3.connect('hybrid.db')

current_user = ""
with st.sidebar:
    user_name = st.text_input("Username")
    logbutton = st.button("Login")


if logbutton:
    relate = "SELECT username,leftusername,rightusername FROM users WHERE (((users.username)=" + "'" + user_name + "'" + "));"
    relatefile = pd.read_sql(relate,conn,)
    current_user = list(relatefile['username'])
    level2l, evel1l,level0c,level1r ,level2r = st.columns(5)
    with level0c:
        st.image("./pix/user.png",caption=  current_user,width=150,)
    
    level2l,level1l, level0c,level1r,level2r = st.columns(5)
    with level1l:
        st.image("./pix/user.png",caption = list(relatefile['leftusername']),width=150)
    with level1r:
        st.image("./pix/user.png",caption = list(relatefile['rightusername']),width=150)   
    level2l,level2lc,level1l, level0c,level1r,level2rc, level2r = st.columns(7)
    with level2l:
        st.image("./pix/user.png",width=130)
    with level2r:
        st.image("./pix/user.png",width=130)
    with level1r:
        st.image("./pix/user.png",width=130)
    with level1l:
        st.image("./pix/user.png",width=130)