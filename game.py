import streamlit as st
from design import design
from stock_data import stocks
from repo import repo_files
from trade import trade


# setting up basic page setup
design.basic_setup()
st.write("Streamlit version:", st.__version__)

# Save game
st.sidebar.button('save game', on_click=design.save_game)

st.dataframe(df, column_config={"Website": st.column_config.LinkColumn()})







