from sqlalchemy import ColumnElement, true
import streamlit as st
import pyodbc
import pandas as pd
import numpy as np


conn = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=data/CCLPIHN_be.accdb;')

relate = 'SELECT username, password FROM users ORDER BY username;'

relatefile = pd.read_sql(relate,conn,)
conn.close()


# Title
st.title("Login Page")

# Username input
username = st.text_input("Username")

item = (relatefile['username'])

found_user = False
for item_search in item:
    
    if item_search == username:
        found_user = True
     
        break
    
password = st.text_input("Password", type="password")

itempass= (relatefile['password'])

found_pass = False

for itempass_search in itempass:

    if itempass_search == password:
        found_pass = True
       
        break

# Login button

if st.button("Login"):
    
    if found_user == True  and found_pass == True:

        st.success("Logged in successfully!")
    else:
        st.error("Invalid username or password")
       



