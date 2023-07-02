import streamlit as st


from design import design
from stock_data import stocks


# setting up basic setup
design.basic_setup()

st.write(stocks.get_data())






