import streamlit as st
from repo import repo_files
from stock_data import stocks
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
        with st.container:
            st.title('My Portfolio Worth')
            st.write(f'cash: ')
            st.write(f'stocks:')




# New Game
def new_game():
    try:
        repo_files.del_file('base')
        repo_files.del_file('my_stocks')
    except:
        pass
    # Save base df
    base = (stocks.get_data())
    repo_files.save_new_file(base, 'base')
    cash = 100000
    return cash



