import requests
import env
import pandas as pd
from oauth2client.service_account import ServiceAccountCredentials
from df2gspread import df2gspread as d2g

# Configure the following variables
base_url = 'http://api.exchangeratesapi.io/v1/'
query = {'access_key': env.API_KEY}
rates_date = '2015-01-15'
spreadsheet_key = '1egtwf73Zvi_TjoVAW9EHX3tFiVHlK6fyoacRC7s2O1M'  # Google Spreadsheet ID taken from the URL
filename = "output.html"  # Filename of the html file to be exported

r = requests.get(base_url + rates_date, params=query).json()

# Using pandas library to transform data and convert to html
df = pd.DataFrame.from_dict(r).reset_index()
df = df[['index', 'rates']]
df.columns = ['Currency', 'Exchange rate (base EUR)']
df.to_html(open(filename, 'w'), index=False)
print(df)

# Export to Google Spreadsheet
scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']
credentials = ServiceAccountCredentials.from_json_keyfile_name('gsheets.json', scope)
d2g.upload(df, spreadsheet_key, credentials=credentials, row_names=False)
