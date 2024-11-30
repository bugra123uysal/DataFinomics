import yfinance as yf
import requests
import time
import pandas as pd
from bs4 import BeautifulSoup
import tkinter as tk
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

tü=tk.Tk()
tü.title("finance")
tü.geometry("500x500")


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
   
time.sleep(1)

stock=[ "AAPL", "MSFT", "GOOGL", "AMZN", "TSLA", "NVDA", "META", "NFLX", "ADBE", "PEP",#abd
    

    "THYAO.IS", "GARAN.IS", "AKBNK.IS", "ISCTR.IS", "YKBNK.IS", "EREGL.IS", "KRDMD.IS", "TOASO.IS", #ist
    "TUPRS.IS"]
def grf(vv ,  stock_name, prc):

  hıss=plt.plot(vv.index , vv["Close"], label=f"{stock}")
  plt.show()

  reo= form.get()
  if reo == "":
   reo=1
  reo=float(reo)
  uyth= reo * prc
  pie=tk.Label(text=f"hisselerim:{uyth}")
  pie.pack()
     
form=tk.Entry()
form.pack(side="right") 

 


for xx in stock:
    
    try:

       vv=yf.download(xx, start= "2024-01-01",end="2024-12-31" )
      

       ff=yf.Ticker(xx)
       prc=ff.history(period="1d")["Close"].iloc[-1]
       bas=tk.Button(text=f"{xx}:{prc} ", command=lambda  vv=vv, stock_name=xx , prc=prc:   grf(vv, stock_name, prc) )
       bas.pack()

       
    
       
    except Exception as e:
        print("tekrar")
       




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
    

   
tü.mainloop()
