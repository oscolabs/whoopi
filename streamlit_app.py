import streamlit as st
import numpy as np
import pandas as pd
import altair as alt
from datetime import datetime, timedelta

# Page title
st.set_page_config(page_title='Support Ticket Workflow', page_icon='🎫')
st.title('🎫 Support Ticket Workflow')
st.info('To write a ticket, fill out the form below. Check status or review ticketing analytics using the tabs below.')


# Generate data
import requests

data = requests.get("https://api.prod.whoop.com/oauth/oauth2/auth").json()
st.write(data)
