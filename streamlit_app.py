import streamlit as st
import numpy as np
import pandas as pd
import altair as alt
from datetime import datetime, timedelta

# Page title
st.set_page_config(page_title='Whoopi', page_icon='🎫')
st.title('🎫 Whoopi')
st.info('To write a ticket, fill out the form below. Check status or review ticketing analytics using the tabs below.')

client_id='07fa9a7e-6e68-4ca1-aa03-e535ca5f7816'
client_secret= 'f488d57fb86082c1125b565a36375ba9c63e3768c2fe04a82c3bff6b1097fbb8'

def get_access_token(url, client_id, client_secret):
    response = requests.post(
        url,
        data={"grant_type": "client_credentials"},
        auth=(client_id, client_secret),
    )
    return response.json()["access_token"]


# get_access_token("https://api.example.com/access_token", "abcde", "12345")

# # Generate data
# import requests


# '

# r = requests.get("https://api.prod.whoop.com/oauth/oauth2/auth", data={})
# r.json()



