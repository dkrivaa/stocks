import streamlit as st
import requests
import base64
import pandas as pd
import json


# function to save file to repo on GitHub
def save_new_file(file_name, filename):  # file_name as a Dataframe, filename with ''
    file_name.name = str(file_name)
    # Secrets
    repo_url = st.secrets['REPO']
    access_token = st.secrets['ACCESS_TOKEN']  # Personal Access Token with repo scope
    # name and content of file to save
    file_path = filename + '.csv'
    file_content = file_name.to_csv(index=False)
    # Encoding
    encoded_content = base64.b64encode(file_content.encode("utf-8")).decode("utf-8")
    # Prepare the API URL
    api_url = f"https://api.github.com/repos/{repo_url}/contents/{file_path}"
    # Set up the request headers with the access token
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Accept": "application/vnd.github.v3+json"
    }
    # Create the request payload
    payload = {
        "message": "Add file via Streamlit Share",
        "content": encoded_content
    }
    # Make the API request to create
    response = requests.put(api_url, headers=headers, json=payload)


# Function to read file (the function returns Dataframe) from GitHub repository
def read_file(filename):  # filename with ''
    # Secrets
    repo_url = st.secrets['REPO']
    access_token = st.secrets['ACCESS_TOKEN']  # Personal Access Token with repo scope
    # name and content of file to save
    file_path = filename + '.csv'
    # Prepare the API URL
    api_url = f"https://api.github.com/repos/{repo_url}/contents/{file_path}"
    # Set up the request headers with the access token
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Accept": "application/vnd.github.v3+json"
    }
    response = requests.get(api_url, headers=headers)
    if response.status_code == 200:
        content = response.json()['content']
        # Decode the content from base64
        data = base64.b64decode(content).decode('utf-8')
        if filename == 'base':
            data_list = data.split()
            data_list = data_list[2:]
            symbol = []
            stock_price = []
            for items in data_list:
                items = items.split(',')
                symbol.append(items[0])
                stock_price.append(items[1])
            base_org = pd.DataFrame({'symbol': symbol, 'stock price': stock_price})
            return base_org
        elif filename == 'my_stocks':
            st.write(data)
        elif filename == 'my_cash':
            data_list = data.split()
            cash = (data_list[1])
            return cash

# Function to delete file in repo of GitHub
def del_file(filename):  # filename in ''
    # Secrets
    repo_url = st.secrets['REPO']
    access_token = st.secrets['ACCESS_TOKEN']  # Personal Access Token with repo scope
    # name and content of file to save
    file_path = f'{filename}.csv'
    # Prepare the API URL
    api_url = f"https://api.github.com/repos/{repo_url}/contents/{file_path}"
    # Set up the request headers with the access token
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Accept": "application/vnd.github.v3+json"
    }
    response = requests.get(api_url, headers=headers)
    if response.status_code == 200:
        file_info = response.json()
        sha = file_info["sha"]
        # Construct the request payload
        delete_payload = {
            "message": "Delete file",
            "sha": sha
         }
    # Make the API request to delete the file
    response = requests.delete(api_url, headers=headers, json=delete_payload)

