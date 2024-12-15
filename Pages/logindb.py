import streamlit as st
import pyodbc
import pandas as pd
import sqlite3

conn = sqlite3.connect('hybrid.db')

cursor = conn.cursor()


# Title
st.title("Login Page")

# Username input
user_name = st.text_input("Username")
pass_word = st.text_input("Password", type="password")
item_pass= "" #(relatefile['password'])

found_user = False
found_pass = False
relate = "SELECT username,password FROM users;"
relatefile = pd.read_sql(relate,conn)
st.write(relatefile)  

# Login button
if st.button("Login"):
    relate = "SELECT username,password FROM users WHERE (((users.username)=" + "'" + user_name + "'" + "));"
   
    relatefile = pd.read_sql(relate,conn)
    
    if relatefile.empty == False:
        found_user = True
        for mypass in relatefile['password']:
            if mypass == pass_word:
                found_pass = True
                break

    if found_user == True  and found_pass == True:

        st.success("Logged in successfully!")
        conn.close()
    else:
        st.error("Invalid username or password")
       



