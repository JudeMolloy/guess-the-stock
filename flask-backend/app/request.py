import os
import requests

MARKET_STACK_API_KEY = os.getenv('MARKET_STACK_API_KEY')

stocks = ["AAPL", "BB", "GME", "UBER", "TSLA", "SHOP", "PLTR"]

price_dict = {}
for name in stocks: # TODO: replace api key back to var
    object = requests.get(f"http://api.marketstack.com/v1/eod?access_key=713d8bdd9b293056ed674b25b19aeb94&symbols={name}&date_from=2015-01-01").json()
    temp = []
    for data in object["data"]:
        temp.append({"date" : data["date"], "price" : data["close"]})
    price_dict= {
        "name": object["data"][0]["symbol"],
        "data": temp
    }
    print(price_dict)
        
    #if not in db
    #send to db