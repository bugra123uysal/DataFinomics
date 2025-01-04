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
app = Flask(__name__, template_folder="templates")

@app.route("/")  
def home():
    
    
    """ coin url """
    symbols = [
       "BTC-USD", "ETH-USD", "XRP-USD", "ADA-USD", "SOL-USD",
    "DOGE-USD", "DOT-USD", "BNB-USD", "LTC-USD", "MATIC-USD",
    "SHIB-USD", "AVAX-USD", "UNI-USD", "TRX-USD", "XLM-USD",
    "ATOM-USD", "LINK-USD", "FTT-USD", "ALGO-USD", "ICP-USD",
    

   
]

    crepto_dt=[]
    for symbol in symbols:
      

      tce=yf.Ticker(symbol)
      a=tce.history(period="1d")

      b=a["Close"].iloc[-1]
      crepto_dt.append({"name": symbol , "price": b})
      
       
      hh=yf.download(symbol , start="2024-01-01" , end="2025-01-04")
      plt.plot(hh.index , hh["Close"]  )
      plt.title("coin name: "+symbol )
      plt.grid(True)
      plt.show()
     
    return render_template("hm.html", crepto=crepto_dt)


@app.route("/stock")
def stok():
   usstocks = ["AAPL", "MSFT", "GOOGL","AMZN", "TSLA", "META", "NVDA","META", "NVDA", "NFLX",  
    "AMD",   
    "INTC",  
    "ORCL",  
    "DIS",  
    "BA",    
    "NKE", 
    "IBM",
    "CSCO",  
    "CMCSA", 
    "PYPL",  
    "ADBE", 
    "PEP",   
    "COST",  
    "KO",    
    "MCD",   
    "QCOM",  
    "CVX",   
    "T",   
    "VZ",    
    "XOM",   
    "SPGI",  
    "GS",    
    "JPM",   
    "WMT",   
    "TGT",   
    "UNH",   
    "PFE",   
    "MRK"
        ]
  

   us=[]

   for abdstock  in usstocks : 

  
     st=yf.Ticker(abdstock)
     hstr=st.history(period="1d")
     end=hstr["Close"].iloc[-1]   
     us.append({"ad": abdstock , "fıyat": end })
   return render_template("stock.html", uasto=us )






if __name__ == "__main__":
    app.run(debug=True)
