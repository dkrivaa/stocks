import streamlit as st
from design import design
from stock_data import stocks
from repo import repo_files
from trade import trade


# setting up basic page setup
sell_list = design.basic_setup()
buy_list = design.market()


st.write(sell_list)
st.write(buy_list)









