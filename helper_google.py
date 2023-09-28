import streamlit as st
import gspread
from oauth2client.service_account import ServiceAccountCredentials

sheetid = st.secrets['response_sheet']['id']
RESPONSE = 'response'

credentials_info = st.secrets['service_account']
SCOPE = [
    "https://spreadsheets.google.com/feeds",
    "https://www.googleapis.com/auth/drive",
    "https://www.googleapis.com/auth/spreadsheets"
]

def append_data(array_data):
    gc = gspread.authorize(ServiceAccountCredentials.from_json_keyfile_dict(credentials_info,SCOPE))
    workbook = gc.open_by_key(sheetid)
    worksheet = workbook.worksheet(RESPONSE)
    try :
        worksheet.append_rows(  values=[array_data],
                            value_input_option='USER_ENTERED',
                            table_range='A:Z')
        return 'success'
    except Exception as e:
        return 'retry'