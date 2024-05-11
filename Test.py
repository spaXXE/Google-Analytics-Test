import streamlit as st
from PIL import Image
from pathlib import Path

# STREAMLIT PAGE CONFIG.

st.set_page_config(page_title='GOOGLE ANALYTICS TEST', page_icon='🏢', layout="centered", initial_sidebar_state="collapsed")

google_analytics = """ 
            <!-- Google tag (gtag.js) -->
            <script async src="https://www.googletagmanager.com/gtag/js?id=G-TSM5N1J350"></script>
            <script>
              window.dataLayer = window.dataLayer || [];
              function gtag(){dataLayer.push(arguments);}
              gtag('js', new Date());
            
              gtag('config', 'G-TSM5N1J350');
            </script>
            """
st.markdown(google_analytics, unsafe_allow_html=True)

hide_streamlit_style = """ 
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)



st.write("Hello World")
