import requests
from datetime import date
from time import sleep
import time
import pandas as pd
import os
from prettytable import PrettyTable

baseEndPoint = 'https://dapi.binance.com'
futuresPremiumIndex = '/dapi/v1/premiumIndex'
secondsSleep = 1800
payload = []
dias = []
response = []

payload = [{'symbol': 'BTCUSD_220325'}, {'symbol': 'ETHUSD_220325'},
           {'symbol': 'XRPUSD_220325'}, {'symbol': 'BNBUSD_220325'},
           {'symbol': 'ADAUSD_220325'}, {'symbol': 'LINKUSD_220325'},
           {'symbol': 'BCHUSD_220325'}, {'symbol': 'DOTUSD_220325'},
           {'symbol': 'LTCUSD_220325'},
           {'symbol': 'BTCUSD_220624'}, {'symbol': 'ETHUSD_220624'},
           {'symbol': 'XRPUSD_220624'}, {'symbol': 'BNBUSD_220624'},
           {'symbol': 'ADAUSD_220624'}, {'symbol': 'LINKUSD_220624'},
           {'symbol': 'BCHUSD_220624'}, {'symbol': 'DOTUSD_220624'},
           {'symbol': 'LTCUSD_220624'}
           ]

df = pd.DataFrame(payload)
df['response'] = ''

while True:
    t = PrettyTable([
                'Symbol',
                'Mark',
                'Index',
                'Dias',
                'TNA',
                'TEA',
                'Tasa Directa'])
    t.align = 'r'
    n=0
    print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()))
    for i in df['symbol']:
        param = {'symbol': df['symbol'][n]}
        response = requests.request("GET", url = baseEndPoint+futuresPremiumIndex, params = param)
        responses = pd.DataFrame(response.json(), index=[0])
        iniAnio = (df.iloc[n]['symbol']).find("_") + 1
        dias=(date(int('20'+df.iloc[n]['symbol'][iniAnio: iniAnio +2]), int(df.iloc[n]['symbol'][iniAnio + 2:iniAnio + 4]), int(df.iloc[n]['symbol'][iniAnio + 4:iniAnio + 6])) - date.today()).days  
        markPrice = round(float(responses.iloc[0]['markPrice']),4)
        indexPrice = round(float(responses.iloc[0]['indexPrice']),4)
        tna = round(((markPrice / indexPrice)-1) * (365 / dias) * 100, 2)
        tasaImplicita = round(((markPrice / indexPrice) ** (365 / dias) - 1) * 100, 2)
        tasaDirecta = round(((markPrice / indexPrice)-1) * 100, 2)
        t.add_row([
            i, 
              markPrice,
              indexPrice,
              dias, 
              tna,
              tasaImplicita,
              tasaDirecta]
            )
        if n == len(payload) / 2 - 1:
            t.add_row([
                '--------------'] * 7)
        n+=1
    print(t)
    sleep(secondsSleep)
