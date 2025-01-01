from bs4 import BeautifulSoup 
import requests  
import pandas as pd 
import numpy as np 
import seaborn as sns 
import yfinance as yf
import matplotlib.pyplot as plt 
from flask import Flask, render_template
import  json

app = Flask(__name__, template_folder="templates")

@app.route("/")  
def home():
    
    
    """ coin url """
    symbols = ["BTC-USD", "ETH-USD", "XRP-USD"]
    crepto_dt=[]
    for symbol in symbols:
      

      tce=yf.Ticker(symbol)
      a=tce.history(period="1mo")

      b=a["Close"].iloc[-1]
      crepto_dt.append({"name": symbol , "price": b})

    return render_template("hm.html", crepto=crepto_dt)
      
    


@app.route("/stock")
def stok():
   usstocks = ["AAPL", "MSFT", "GOOGL", "AMZN", "TSLA", "META", "NVDA", "BRK.B", "JPM", "V"]
   us=[]

   for abdstock in usstocks: 
     st=yf.Ticker(abdstock)
     hstr=st.history(period="1mo")
     end=hstr["Close"].iloc[-1]
     if hstr.empty:
        us.append("hata oluştu")
        continue
        
     
     us.append({"ad": abdstock , "fıyat": end })
   return render_template("stock.html", uasto=us )


if __name__ == "__main__":
    app.run(debug=True)
