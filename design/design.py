import streamlit as st
import webbrowser


from design import images


start = True

# BASIC SETUP OF WEB PAGE
def basic_setup():
    st.set_page_config(page_title='Nasdaq Stock Game', layout='wide')
    st.markdown(f'<span style="color: #18448c; font-size: 32px"><b>NASDAQ STOCK GAME</b></span>'
             , unsafe_allow_html=True)
    st.markdown('___')



# Start page
def start_page():
    if start:
        cols = st.columns([1, 2])
        with cols[0]:
            url = 'https://cdn1.iconfinder.com/data/icons/finance-251/64/56-64.png'
            st.image(images.get_image(url))
            st.write('')
            st.button('Start New Game', on_click=new_game)
        with cols[1]:
            url = 'https://cdn0.iconfinder.com/data/icons/customicondesignoffice5/64/continue.png'
            st.image(images.get_image(url))
            st.write('')
            st.button('Continue Game', on_click=continue_game)


# New Game
def new_game():
    webbrowser.open('https://trading-stocks.streamlit.app/new_game')

# Continue game
def continue_game():
    pass


