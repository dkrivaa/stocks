from stock_data import stocks

cash = 100000
cash = "{:,}".format(cash)
s_data = stocks.get_data()


def buy(symbol, amount):
    price = s_data.loc[s_data['symbol'] == symbol, 'price']
    cost = price * amount
    if cost <= cash:
        new_stock = {'symbol': symbol, 'amount': amount, 'buy_price': price}
        cash = cash - cost



def sell(symbol, amount):
    pass



