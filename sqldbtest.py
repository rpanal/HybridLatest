import pyodbc
import sqlite3
import streamlit as st

conn = sqlite3.connect('hybrid.db')

cursor = conn.cursor()

cursor.execute("SELECT * FROM users")
rows = cursor.fetchall()
for row in rows:
    st.write(row)

conn.close()
