import streamlit as st
from design import design
from stock_data import stocks
from repo import repo_files
from trade import trade


# setting up basic page setup
exist_stocks = design.basic_setup()

if exist_stocks is not None:
    for i in range(0, len(exist_stocks)):
        sell_list = []
        if exist_stocks['sell'][i]:
            sell_list.append(exist_stocks['symbol'][i])
    st.write(sell_list)









