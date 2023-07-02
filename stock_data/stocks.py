import requests
import json


# GETTING DATA FOR ALL STOCKS ON NASDAQ (latest close)
def get_data():
    url = 'https://stockanalysis.com/api/screener/s/f?m=marketCap&s=desc&c=no,s,n,marketCap,price,change,revenue,volume,industry,sector,revenueGrowth,netIncome,fcf,netCash&cn=0&f=exchange-is-NASDAQ&p=2&dd=true&i=allstocks'
    response = requests.get(url)
    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the JSON data
        stock_data = json.loads(response.text)
    # Extract data and make dataframe
    nested_data = stock_data['data']['data']
    return nested_data


#Making dataframe with all stock data
# df = pd.DataFrame(nested_data)
# df = df.rename(columns={'s': 'symbol', 'n': 'company name', 'marketCap': 'market capital',
#                         'price': 'stock price', 'change': 'percentage change',
#                         'fcf': 'free cash flow', 'netCash': 'net chash / debt'})
# df.drop('no', axis=1, inplace=True)