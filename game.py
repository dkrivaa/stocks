import streamlit as st
from design import design
from stock_data import stocks
from repo import repo_files
from trade import trade


# setting up basic page setup
# My stocks
sell_list = design.basic_setup()
st.button('test')

# design.look()
# All market
buy_list = design.market()











