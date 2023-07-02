import streamlit as st

from design import images

# BASIC SETUP OF WEB PAGE
def basic_setup():
    st.set_page_config(page_title='Nasdaq Stock Game', layout='wide')
    st.markdown(f'<span style="color: #18448c; font-size: x-large"><b>NASDAQ STOCK GAME</b></span>'
             , unsafe_allow_html=True)
    st.markdown('___')


def start_page():
    cols = st.columns([1, 8])
    with cols[0]:
        url = 'https://cdn4.iconfinder.com/data/icons/success-filloutline/64/chart-analytics-stocks-increasing-growth-64.png'
        st.image(images.get_image(url))
        st.write('')
        st.button('Start New Game')
    with cols[1]:
        url = 'https://cdn0.iconfinder.com/data/icons/customicondesignoffice5/64/continue.png'
        st.image(images.get_image(url))
        st.write('')
        st.button('Continue Game')


