from design import design
from stock_data import stocks
from repo import repo_files

# setting up basic page setup
design.basic_setup()

# Save base df
repo_files.save_new_file(stocks.get_data(), 'test')








