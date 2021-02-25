import os
import requests

MARKET_STACK_API_KEY = os.getenv('MARKET_STACK_API_KEY')

stocks = ["AAPL", "BB", "GME", "UBER", "TSLA", "SHOP", "PLTR"]
for name in stocks:
    object = requests.get(f"http://api.marketstack.com/v1/eod?access_key={MARKET_STACK_API_KEY}&symbols={name}&date_from=2015-01-01").json()
    #if not in db
    #send to db

print("done")