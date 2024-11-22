import yfinance as yf
import requests
import time

stock=yf.Ticker("AAPL")
print(stock.history(period=("1d")))




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
    print(xx["name"], xx["current_price"])








