import streamlit as st
from design import design
from stock_data import stocks
from repo import repo_files
from trade import trade

st.sidebar.markdown(f'<span style="color: #18448c; font-size: 18px"><b>Navigation</b></span>'
             , unsafe_allow_html=True)
# setting up basic page setup
design.basic_setup()

# Getting my stocks
sell_list = design.startup_my_stocks()

# Stocks to pay attention to
# design.look()


# # All market
# buy_list = design.market()
#
# for i in range(0, len(buy_list)):
#     pass











