from bs4 import BeautifulSoup 
import requests  
import pandas as pd 
import numpy as np 
import seaborn as sns 
import yfinance as yf
import matplotlib.pyplot as plt 
from flask import Flask, render_template
import  json
import io
import base64
import os
import time
import threading

static_dir=os.path.join(os.path.dirname(__file__), 'templates')
if not os.path.exists(static_dir):
   os.makedirs(static_dir)

app = Flask(__name__, template_folder="templates")

@app.route("/")  
def home():
    
    
    """ coin url
     "XRP-USD", "ADA-USD", "SOL-USD",
    "DOGE-USD", "DOT-USD", "BNB-USD", "LTC-USD", "MATIC-USD",
    "SHIB-USD", "AVAX-USD", "UNI-USD", "TRX-USD", "XLM-USD",
    "ATOM-USD", "LINK-USD", "FTT-USD", "ALGO-USD", "ICP-USD"
       """
    
    symbols = [
    "BTC-USD", "ETH-USD"]
    crepto_dt=[]




    for symbol in symbols:
      

      tce=yf.Ticker(symbol)
      



      a=tce.history(period="1d")

      b=a["Close"].iloc[-1]
      hh=yf.download(symbol , start="2024-01-01" , end="2025-01-04")
      plt.plot(hh.index , hh["Close"]  )
      plt.title("coin name: "+symbol )
      plt.grid(True)
      plt.legend()

      time.sleep(10)
     

      crepto_dt.append({"name": symbol , "price": b  })
      
     
    return render_template("hm.html"  ,  crepto=crepto_dt)



@app.route("/stock")
def stok():
   usstocks = ["AAPL", "MSFT", "GOOGL","AMZN", "TSLA", "META", "NVDA","META", "NVDA", "NFLX",  "AMD",   "INTC",  "ORCL",  "DIS",  "BA",    "NKE", "IBM","CSCO",  "CMCSA", "PYPL",  "ADBE", "PEP",   "COST",  "KO",    "MCD",   "QCOM",  "CVX",   "T",   "VZ",    "XOM",   "SPGI",  "GS",    "JPM",   "WMT",   "TGT",   "UNH",   "PFE","MRK" ]
   us=[]

   for abdstock  in usstocks : 
  
     st=yf.Ticker(abdstock)
     hstr=st.history(period="1d")
     end=hstr["Close"].iloc[-1]   
     us.append({"ad": abdstock , "fıyat": end })
   time.sleep(10)
   return render_template("stock.html", uasto=us )

thread=threading.Thread(target=stok)
thread.start()

@app.route("/info")
def inf():
      
      symbols = [
    "BTC-USD", "ETH-USD"]
      iinf=[]
      
      for sss in  symbols:
       
       """ info section """
       ttt=yf.Ticker(sss)

       iif=ttt.info
       """ market capt """
       mrecpt=iif.get("marketCap", 'N/A' )
       """ hacmi """
       hcm=iif.get("regularMarketVolume", 'N/A')
 
       iinf.append({"name" : sss , "marketCap:" : mrecpt , "hacım": hcm })
      return render_template("info.html",lk=iinf )


if __name__ == "__main__":
    app.run(debug=True)
