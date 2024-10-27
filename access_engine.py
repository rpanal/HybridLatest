import streamlit as st
import urllib
import pandas as pd
from sqlalchemy import create_engine, text

def access_engine(access_db):
    cnnstr = (
        r"Driver={Microsoft Access Driver (*.mdb, *.accdb)};"
        r"DBQ=" + access_db
    )
    cnnurl = f"access+pyodbc:///?odbc_connect={urllib.parse.quote_plus(cnnstr)}"
    acc_engine = create_engine(cnnurl)
    return acc_engine

db_path = (r".\Data\CCLPIHN_be.accdb")
engine = access_engine(db_path)

username = st.text_input("User Name",255)
password = st.text_input("Password",255)
if st.button("Save!"):
    params = {
        "username": username,
        "password": password
    }
    relate = 'SELECT username, password FROM users ORDER BY username;'

    sql = text("""INSERT INTO users (username,password) VALUES (:username,:password);""")
        

    with engine.connect() as cnn:
        relatefile = pd.read_sql(relate,cnn)
       # result = cnn.execute(sql,params)
        item = (relatefile['username'])
        st.write(item)
        #cnn.commit()
        st.write("You have been added!")
else:
    st.write("Click save to added")

