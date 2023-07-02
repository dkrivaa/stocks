import streamlit as st
from design import design
from stock_data import stocks
from repo import repo_files

# setting up basic page setup
design.basic_setup()


# Save base df
# base = (stocks.get_data())
# repo_files.save_new_file(base, 'base')

repo_files.del_file('test')







