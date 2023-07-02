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
        url = 'https://images.unsplash.com/photo-1590283603385-17ffb3a7f29f?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Mnx8c3RvY2slMjBtYXJrZXR8ZW58MHx8MHx8fDA%3D&auto=format&fit=crop&w=500&q=60'
        st.image(images.get_image(url))
        st.write('')
        st.button('Start New Game')
    with cols[1]:
        url = 'https://images.unsplash.com/photo-1486572788966-cfd3df1f5b42?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8N3x8Y29udGludWUlMjBnYW1lfGVufDB8fDB8fHww&auto=format&fit=crop&w=500&q=60'
        st.image(images.get_image(url))
        st.write('')
        st.button('Continue Game')


