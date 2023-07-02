import streamlit as st
from repo import repo_files

from design import images


# BASIC SETUP OF WEB PAGE
def basic_setup():
    st.set_page_config(page_title='Nasdaq Stock Game', layout='wide')
    st.markdown(f'<span style="color: #18448c; font-size: 32px"><b>NASDAQ STOCK GAME</b></span>'
             , unsafe_allow_html=True)
    st.button(':red[New Game]', on_click=new_game())
    st.markdown('___')
    # Sidebar
    with st.sidebar:
        st.markdown(f'<span style="color: #18448c; font-size: 24px"><b>Game Options</b></span>'
                    , unsafe_allow_html=True)

        st.sidebar.button('Save Game', on_click=save_game())




# New Game
def new_game():
    pass

def save_game():
    pass

