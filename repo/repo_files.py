import streamlit as st
import requests
import base64
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