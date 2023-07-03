import streamlit as st

from stock_data import stocks

s_data = stocks.get_data()


def buy(symbol, amount):     # symbol in ''
    cash = 100000
    price = s_data.loc[s_data['symbol'] == symbol, 'price']
    cost = int(price * amount)
    if cost <= cash:
        new_stock = {'symbol': symbol, 'amount': amount, 'buy_price': price}
        cash = cash - cost
    else:
        st.success('You do NOT have enough cash to make this purchase')

buy('AAPL', 10000)

def sell(symbol, amount):
    pass



