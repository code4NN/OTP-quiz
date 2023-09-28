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

@st.cache_resource
def get_google_credential():
    gc = gspread.authorize(ServiceAccountCredentials.from_json_keyfile_dict(credentials_info,SCOPE))
    workbook = gc.open_by_key(sheetid)
    worksheet = workbook.worksheet(RESPONSE)
    
    return worksheet

def append_data(array_data):
    try :
        worksheet = get_google_credential()
        worksheet.append_rows(  values=[array_data],
                            value_input_option='USER_ENTERED',
                            table_range='A:Z')
        st.header("From Method 1")
        return 'success'
    except Exception as e:
        try:
            gc = gspread.authorize(ServiceAccountCredentials.from_json_keyfile_dict(credentials_info,SCOPE))
            workbook = gc.open_by_key(sheetid)
            worksheet = workbook.worksheet(RESPONSE)
            worksheet.append_rows(  values=[array_data],
                                value_input_option='USER_ENTERED',
                                table_range='A:Z')
            st.header("From Method 2")
            return 'success'
        except Exception as e:
            return 'error'
        return 'error'