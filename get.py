import yfinance as yf
import requests
import time
import pandas as pd
from bs4 import BeautifulSoup



ım=("https://tradingeconomics.com/matrix")

""" istek gönderme """
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
}

pp=requests.get(ım,headers=headers)

if pp.status_code == 200:


   yy=BeautifulSoup(pp.content,'html.parser')
   rr=yy.find("table")
   if rr:
    print("bulundu ")
    row=rr.find_all("tr")
   for onn in row:
    cols=onn.find_all("td")
    data=[col.text.strip() for col in cols]
    print(data)

   else:
     print("bulunamadı tekrar deneyiniz")

else:
    print("istek başarısız")
   






stock=yf.Ticker("AAPL")
print(stock.history(period=('1d')))




time.sleep(2)


url=("https://api.coingecko.com/api/v3/coins/markets")

params = {
    "vs_currency": "usd",
    "order": "market_cap_desc",
    "per_page": 10,
    "page": 1
}



aa=requests.get(url,params=params)
bb=aa.json()

for xx in bb:
    print(xx["name"],  xx["current_price"])
    


