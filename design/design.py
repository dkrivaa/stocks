import pandas as pd
import streamlit as st


from repo import repo_files
from stock_data import stocks

from trade import trade
from design import images


def sidebar(my_cash, stock_worth):
    # Sidebar
    with st.sidebar:
        st.title('My Portfolio')
        st.write(f'cash: {my_cash} ')
        st.write(f'stocks: {stock_worth}')
        st.markdown('___')

        st.markdown('___')

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

    # calculating worth of stock portfolio
    if len(my_stocks) != 0:
       stock_worth = 0
       my_stock_list = my_stocks['symbol'].unique().tolist()
       for symbol in my_stock_list:
           amount = int(my_stocks.loc[my_stocks['symbol'] == symbol, 'amount'].sum())
           price = int(s_data.loc[s_data['symbol'] == symbol, 'price'])
           worth = price * amount
           st.write(amount, price, worth)
           stock_worth = stock_worth + worth
    else:
        stock_worth = 0

    sidebar(my_cash, stock_worth)


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
    my_stocks = pd.DataFrame({'symbol': [], 'amount': [], 'org_price': []})
    my_cash = pd.DataFrame({'cash': [100000]})
    repo_files.save_new_file(my_stocks, 'my_stocks')
    repo_files.save_new_file(my_cash, 'my_cash')





def save_game():
    pass
# repo_files.save_new_file(my_stocks, 'my_stocks')
