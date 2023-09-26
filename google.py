import streamlit as st
import gspread
from oauth2client.service_account import ServiceAccountCredentials

credentials_info = st.secrets['service_account']
sheetid = st.secrets['response_sheet']['id']
SCOPE = [
    "https://spreadsheets.google.com/feeds",
    "https://www.googleapis.com/auth/drive",
    "https://www.googleapis.com/auth/spreadsheets"
]
gc = gspread.authorize(ServiceAccountCredentials.from_json_keyfile_dict(credentials_info,SCOPE))
workbook = gc.open_by_key()