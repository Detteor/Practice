import requests
import pandas as pd
from keys import ameritrade
import pickle as pkl
import time
from datetime import datetime as dt
import re
import json
import os

now = dt.now()

url = 'https://api.tdameritrade.com/v1/instruments'
    
xlFile = '/home/mark/Downloads/Complete_List.xlsx'

df = pd.read_excel(xlFile)

symbols = df['Symbol'].values.tolist()

start = 0
end = 500

while start < len(symbols):
    tickers = symbols[start:end]
    now = dt.now()
    param = {'apikey': ameritrade,
        'symbol': tickers,
        'projection': 'fundamental'
        }
    results = requests.get(url, params= param)
    data = results.json()
    f_name = '{}/{}{}'.format('/media/WDB/Backup/Projects/Practice/Practice/FreeCodeCamp/Stock Ticker', now.strftime('%I-%M-%S-%f'), '.json')
    with open(f_name, 'wb') as file:
        json.dump(data, file, indent=2)
    
    start = end
    end += 500
    time.sleep(1)