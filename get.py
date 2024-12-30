from bs4 import BeautifulSoup 
import requests  
import pandas as pd 
import numpy as np 
import seaborn as sns 
import matplotlib.pyplot as plt 
from flask import Flask, render_template
import  json

app = Flask(__name__, template_folder="templates")

@app.route("/")  
def home():
    url="https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc&per_page=100&page=1&sparkline=false"
    a= requests.get(url)
    c=BeautifulSoup(a.content , 'html.parser')
    
    co=json.loads(c.text)
    coins=[]
    for coin in co:

        coins.append({"name": coin['name'], "price": coin['current_price'] })

      


    return render_template('hm.html', coins=coins  )

   
if __name__ == "__main__":
    app.run(debug=True)
