import streamlit as st
from design import design
from stock_data import stocks
from repo import repo_files

# setting up basic page setup
design.basic_setup()




# Save game
st.sidebar.button('save game', on_click=design.save_game)
# repo_files.save_new_file(my_stocks, 'my_stocks')







