import pandas as pd
import streamlit as st


from repo import repo_files
from stock_data import stocks

from trade import trade
from design import images


# BASIC SETUP OF WEB PAGE
def basic_setup():
    st.set_page_config(page_title='Nasdaq Stock Game', layout='wide')
    st.markdown(f'<span style="color: #18448c; font-size: 32px"><b>NASDAQ STOCK GAME</b></span>'
             , unsafe_allow_html=True)
    st.button(':red[New Game]', on_click=new_game)
    st.markdown('___')

    # Getting data:
    # my stocks
    my_stocks = repo_files.read_file('my_stocks')
    # My cash
    my_cash = repo_files.read_file('my_cash')
    # updated stock data
    s_data = stocks.get_data()

    # st.write(my_cash)

    # Sidebar
    with st.sidebar:
        st.title('My Portfolio Worth')
        st.write(f'cash: ')
        st.write(f'stocks: ')
        st.markdown('___')

        st.markdown('___')


# New Game
def new_game():
    try:
        repo_files.del_file('base')
        repo_files.del_file('my_stocks')
        repo_files.del_file('my_cash')
    except:
        pass


    # Save base df
    base = (stocks.get_data())
    repo_files.save_new_file(base, 'base')
    # make my_stocks file
    my_stocks = pd.DataFrame({'symbol': [], 'amount': [], 'buy_price': []})
    my_cash = pd.DataFrame({'cash': [100000]})
    repo_files.save_new_file(my_stocks, 'my_stocks')
    repo_files.save_new_file(my_cash, 'my_cash')





def save_game():
    pass
# repo_files.save_new_file(my_stocks, 'my_stocks')
