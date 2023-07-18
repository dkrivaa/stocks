import streamlit as st
from design import design
from stock_data import stocks
from repo import repo_files
from trade import trade


# setting up basic page setup
design.basic_setup()

for i in range(0, len(design.exist_stocks)):
    sell_list = []
    if exist_stocks['sell'][i] == True:
        sell_list.append(exist_stocks['symbol'][i])
st.write(sell_list)








