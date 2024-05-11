import streamlit as st
from PIL import Image
from pathlib import Path

# STREAMLIT PAGE CONFIG.

st.set_page_config(page_title='GOOGLE ANALYTICS TEST', page_icon='🏢', layout="centered", initial_sidebar_state="collapsed")

hide_streamlit_style = """ 
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)


st.write("Hello World")