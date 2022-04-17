# Getting data from an API - Export to html file and Google Spreadsheets

This script can get exchange rate data using exchangeratesapi.io API. 
The main purpose is to export the data to an html file in a table format, and a Google Spreadsheet. 
Below are the steps required to run it.

## 1) Get an API key for Exchange rates API
To obtain an API key for exchangeratesapi, please sign-up at https://exchangeratesapi.io/ (Click “GET API KEY” and register. Once registered, an API will be provided.. 

For security reasons, the API key is not in main.py. Before running the script, please make sure to set the API key in the env.py file

**Please note: The free subscription plan has a limit of 250 requests/month.**

## 2) Setup authentication and authorization for Google Sheets API
To access spreadsheets via Google Sheets API you need to authenticate and authorize the application. To do this, please follow the instructions [here](https://docs.gspread.org/en/latest/oauth2.html) from the beginning (Authentication), until step 6 (included), of the “_For Bots: Using Service Account_” section, which is sharing your spreadsheet with the _client_email_, that can be found in the downloaded json file.

Once those steps are completed, please copy the content of your downloaded  json file, and paste it into the gsheets.json file of the project. 

## 3) Installation
The script was created using Python 3.9. 

1. (Optional) Create a [python virtual environment](https://docs.python.org/3.9/library/venv.html) and activate it

- e.g. in Linux: 
```bash
python -m venv venv
source venv/bin/activate
```

2. To install the dependencies (packages) of the project please run:
```bash
pip install -r requirements.txt
```

3. Copy `env.py.example` to `env.py`, and `gsheets.json.example` to `gsheets.json`. 
Set the credentials accordingly as explained in (1) and (2). 

In the main.py script, set the following variables as desired: 
- spreadsheet_key = Google Spreadsheet ID taken from the URL
- rates_date = Date to get the exchange rates. Format should be YYYY-MM-DD

## 4) Run the script
```bash
python main.py
```


## 5) Expected output

Once you run the script, you should expect: 

1. The following output in the console remained for debugging reasons. _Note: Exchange rate values might be different, depending on the desired date explained above_: 
```
    Currency  Exchange rate (base EUR)
0        AED                  4.270765
1        AFN                 67.321536
2        ALL                139.519660
3        AMD                555.609039
4        ANG                  2.080767
..       ...                       ...
161      YER                249.995000
162      ZAR                 13.432082
163      ZMK               6107.815118
164      ZMW                  7.610103
165      ZWL                374.806125

[166 rows x 2 columns]
```
2. A new output.html file generated containing a table with the above, as the example below (for the full example see `example_output.html` file):

![html output example](https://i.imgur.com/T3a7w8J.png "HTML example")

3. Your Google Sheet to be updated with the same data
