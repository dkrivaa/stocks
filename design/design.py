import streamlit as st


from design import images


# BASIC SETUP OF WEB PAGE
def basic_setup():
    st.set_page_config(page_title='Nasdaq Stock Game', layout='wide')
    st.markdown(f'<span style="color: #18448c; font-size: 32px"><b>NASDAQ STOCK GAME</b></span>'
             , unsafe_allow_html=True)
    st.write('')
    with st.container():
        cols = st.columns([1,1,1,1,1,1,1,1,2])
        with cols[0]:
            st.button('Start New Game', on_click=new_game)
        with cols[1]:
            st.button('button 1')
        with cols[2]:
            st.button('button 2')
        with cols[3]:
            st.button('button 3')
        with cols[4]:
            st.button('button 4')
        with cols[5]:
            st.button('button 5')
        with cols[6]:
            st.button('button 6')
        with cols[7]:
            st.button('About')
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


