import streamlit as st
import pandas as pd


from stock_data import stocks
from repo import repo_files


def buy(symbol, amount):     # symbol in ''
    # Getting data:
    # my stocks
    my_stocks = repo_files.read_file('my_stocks')
    # My cash
    my_cash = repo_files.read_file('my_cash')
    # updated stock data
    s_data = stocks.get_data()
    cash = int(my_cash)
    price = int(s_data.loc[s_data['symbol'] == symbol, 'price'])
    cost = price * amount
    if cost <= cash:
        new_stock = {'symbol': symbol, 'amount': amount, 'buy_price': price}
        cash = cash - cost
        # updating my_stocks file
        my_stocks.append(new_stock)
        repo_files.del_file('my_stocks')
        repo_files.save_new_file(my_stocks, 'my_stocks')
        # updating my_cash file
        repo_files.del_file('my_cash')
        my_cash = pd.DataFrame({'cash': cash})
        repo_files.save_new_file(my_cash, 'my_cash')

    else:
        st.success('You do NOT have enough cash to make this purchase')


def sell(symbol, amount):
    pass



