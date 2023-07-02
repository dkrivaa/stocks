import streamlit as st


from design import images


# BASIC SETUP OF WEB PAGE
def basic_setup():
    st.set_page_config(page_title='Nasdaq Stock Game', layout='wide')
    st.markdown(f'<span style="color: #18448c; font-size: 32px"><b>NASDAQ STOCK GAME</b></span>'
             , unsafe_allow_html=True)
    with st.container():
        cols = st.columns(8)
        with cols[0]:
            st.button('Start New Game', on_click=new_game)
        with cols[1]:
            st.button('Continue game', on_click=continue_game)
    st.markdown('___')



# Start page
def start_page():
    pass



# New Game
def new_game():
    pass


# Continue game
def continue_game():
    pass


