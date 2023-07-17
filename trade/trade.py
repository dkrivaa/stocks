import streamlit as st
import pandas as pd


from stock_data import stocks
from repo import repo_files
from design import design

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
        new_stock = {'symbol': symbol, 'amount': amount, 'org_price': price}
        cash = cash - cost

        # updating my_stocks file
        my_stocks.loc[len(my_stocks)] = new_stock
        repo_files.del_file('my_stocks')
        repo_files.save_new_file(my_stocks, 'my_stocks')

        # updating my_cash file
        repo_files.del_file('my_cash')
        my_cash = pd.DataFrame({'cash': [cash]})
        repo_files.save_new_file(my_cash, 'my_cash')

        my_stocks = repo_files.read_file('my_stocks')
        stock_worth = design.calc_stock_worth(my_stocks, s_data)
        design.sidebar(cash, stock_worth)
    else:
        st.success('You do NOT have enough cash to make this purchase')

    st.experimental_rerun()


def sell(symbol, amount):
    pass



