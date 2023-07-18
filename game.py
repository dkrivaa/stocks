import streamlit as st
from design import design
from stock_data import stocks
from repo import repo_files
from trade import trade


# setting up basic page setup
exist_stocks = design.basic_setup()

st.write(exist_stocks)










