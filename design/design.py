import streamlit as st


# BASIC SETUP OF WEB PAGE
def basic_setup():
    st.set_page_config(page_title='Nasdaq Stock Game', layout='wide')
    st.markdown(f'<span style="color: #18448c; font-size: x-large"><b>Welcome to the NASDAQ STOCK GAME</b></span>'
             , unsafe_allow_html=True)
    st.markdown('___')
    st.write('test')