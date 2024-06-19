import streamlit as st
import numpy as np
import pandas as pd
import altair as alt
from datetime import datetime, timedelta
import requests

# Page title
st.set_page_config(page_title='Whoopi', page_icon='🎫')
st.title('🎫 Whoopi')
st.info('To write a ticket, fill out the form below. Check status or review ticketing analytics using the tabs below.')

import os
import base64
import json
from requests import post

client_id='07fa9a7e-6e68-4ca1-aa03-e535ca5f7816'
client_secret= 'f488d57fb86082c1125b565a36375ba9c63e3768c2fe04a82c3bff6b1097fbb8'

url2 = 'https://api.prod.whoop.com/oauth/oauth2/token'


print(client_id, client_secret)

def get_token():
    auth_string = client_id + ':' + client_secret
    auth_bytes = auth_string.encode('utf-8')
    auth_base64 = str(base64.b64encode(auth_bytes), "utf-8")

    url = 'https://api.prod.whoop.com/oauth/oauth2/auth'
    headers = {
        'Authorization': 'Basic ' + auth_base64,
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    data = {'grant_type': 'client_credentials'}
    result = post(url, headers=headers, data=data)
    json_result = json.loads(result.content)
    token = json_result['access_token']
    return token 

token = get_token()
print(token)

# client_id='07fa9a7e-6e68-4ca1-aa03-e535ca5f7816'
# client_secret= 'f488d57fb86082c1125b565a36375ba9c63e3768c2fe04a82c3bff6b1097fbb8'
# url = 'https://api.prod.whoop.com/oauth/oauth2/auth'

# import requests

# # Define the token endpoint and the necessary payload
# token_url = 'https://api.whoop.com/oauth/token'
# payload = {
#     'grant_type': 'authorization_code',
#     'code': 'AUTHORIZATION_CODE',
#     'redirect_uri': 'YOUR_REDIRECT_URI',
#     'client_id': 'YOUR_CLIENT_ID',
#     'client_secret': 'f488d57fb86082c1125b565a36375ba9c63e3768c2fe04a82c3bff6b1097fbb8'
# }

# # Make the POST request to exchange the authorization code for an access token
# response = requests.post(token_url, data=payload)
# token_data = response.json()

# # Extract the access token from the response
# access_token = token_data['access_token']
# refresh_token = token_data.get('refresh_token')  # if provided

# print("Access Token:", access_token)
# print("Refresh Token:", refresh_token)


# # Obtain an access token (example, may vary depending on Whoop's actual method)
# auth_url = 'https://api.whoop.com/oauth/token'
# auth_data = {
#     'client_id': client_id,
#     'client_secret': client_secret,
#     'grant_type': 'client_credentials'
# }

# response = requests.post(url, data=auth_data)
# response_data = response.json()
# st.write(response_data)
# access_token = response_data['access_token']

# # Use the access token to make an API request
# api_url = 'https://api.whoop.com/v1/endpoint'  # Replace with actual endpoint
# headers = {
#     'Authorization': f'Bearer {access_token}'
# }

# api_response = requests.get(api_url, headers=headers)
# api_data = api_response.json()

# print(api_data)


# def get_access_token(url, client_id, client_secret):
#     response = requests.post(
#         url,
#         data={"grant_type": "client_credentials"},
#         auth=(client_id, client_secret),
#     )
#     token = response.json()["access_token"]

#     st.write(token)
#st.write(response.json()["access_token"])
# get_access_token("https://api.example.com/access_token", "abcde", "12345")

# # Generate data
# import requests


# '

# r = requests.get("https://api.prod.whoop.com/oauth/oauth2/auth", data={})
# r.json()



