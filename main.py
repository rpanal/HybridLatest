
import streamlit as st
import pandas as pd
import numpy as np
import streamlit as st
from pages import genealogy,logindb,login

def main():

    st.markdown("# CCLPI - Hybrid ")

# Add a title to the sidebar

# Add a selectbox to the sidebar
option = st.sidebar.selectbox(
    "Select an option:",
    ["Log In", "Genelogy", "Option 3"]
    )
if option.index == 0:
    logindb
if option.index == 1:
    genealogy

if __name__ == "__main__":
    
    main() 
   



#app = MultiPage()


# Add pages to the app


# Run the app
#app.run()

