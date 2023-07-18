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
    # My stocks
    my_stocks = repo_files.read_file('my_stocks')
    # My cash
    my_cash = repo_files.read_file('my_cash')
    # updated stock data
    s_data = stocks.get_data()

    # Calculating stock worth
    stock_worth = calc_stock_worth(my_stocks, s_data)

    # Populating sidebar
    sidebar(my_cash, stock_worth)

    # Populating table of stocks owned
    my_stocks = my_stocks.rename_axis(index='ID')

    # Adding info and calculations for my stocks
    if len(my_stocks) == 0:
        st.write('No Stocks')
    elif len(my_stocks) != 0:
        my_symbol = my_stocks['symbol'].tolist()
        latest_price = []
        latest_change = []
        for s in my_symbol:
            x = float(s_data.loc[s_data['symbol'] == s, 'price'])
            latest_price.append(x)
            y = ((float(x)/float(my_stocks.loc[my_stocks['symbol'] == s, 'org_price']))-1)*100
            latest_change.append(y)
        my_stocks['price'] = latest_price
        my_stocks['change'] = latest_change
        my_stocks['sell'] = False
        st.write(latest_price)
        st.write(latest_change)
        # Showing my stocks
        st.markdown(f'<span style="color: #18448c; font-size: 18px"><b>My stocks</b></span>'
                 , unsafe_allow_html=True)
        exist_stocks = st.data_editor(my_stocks, column_config={
            'symbol': st.column_config.Column('Symbol', disabled=True),
            'amount': st.column_config.NumberColumn('Amount Owned', disabled=True),
            'org_price': st.column_config.NumberColumn('Purchase price', disabled=True),
            'price': st.column_config.NumberColumn('Latest Price', disabled=True),
            'change': st.column_config.NumberColumn('% Change', disabled=True, format='%.2f%%'),
            'sell': st.column_config.CheckboxColumn('Sell?')
        })

    st.button('Continue with sale?', on_click=sell(exist_stocks))


def sell(exist_stocks):
    for i in range(0, len(exist_stocks)):
        sell_list = []
        if exist_stocks['sell'][i]:
            sell_list.append(exist_stocks['symbol'][i])
    st.write(sell_list)


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


def sidebar(my_cash, stock_worth):
    # Sidebar
    with st.sidebar:
        st.title('My Portfolio')
        st.write(f'cash: {int(my_cash):,} ')
        st.write(f'stocks: {stock_worth:,}')
        st.markdown('___')

        st.markdown('___')
        st.sidebar.button('save game', type='primary', on_click=save_game)


def calc_stock_worth(my_stocks, s_data):
    # calculating worth of stock portfolio
    if len(my_stocks) != 0:
       stock_worth = 0
       my_stock_list = my_stocks['symbol'].unique().tolist()
       for symbol in my_stock_list:
           amount = int(my_stocks.loc[my_stocks['symbol'] == symbol, 'amount'].sum())
           price = int(s_data.loc[s_data['symbol'] == symbol, 'price'])
           worth = price * amount
           stock_worth = stock_worth + worth
    else:
        stock_worth = 0

    return int(stock_worth)
