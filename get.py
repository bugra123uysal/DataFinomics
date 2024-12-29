from bs4 import BeautifulSoup 
import requests  
import pandas as pd 
import numpy as np 
import seaborn as sns 
import matplotlib.pyplot as plt 
from flask import Flask, render_template


app = Flask(__name__, template_folder="templates")
url="https://www.coingecko.com/tr"
a= requests.get(url)
c=BeautifulSoup(a.content , 'html.parser')
stock=c.find_all("div", class_="tw-text-gray-700 dark:tw-text-moon-100 tw-font-semibold tw-text-sm tw-leading-5" )
pirice=c.find_all("span", {"data-price-target": "price"} )



data_stockk=[]
for stocks , pirices in zip(stock, pirice):
    stock_name=stocks.text.strip()
    price_name=pirices.text.strip() 
    data_stockk.append({"name": stock_name , "price": price_name})

for item in data_stockk:
    print(f" {item['name']},: {item['price']}")

@app.route("/")  
def home():
    
    return render_template('hm.html', stocks=data_stockk)

   
if __name__ == "__main__":
    app.run(debug=True)


