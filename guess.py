import json
import os
import requests

from app.models import StockData

MARKET_STACK_API_KEY = os.getenv('MARKET_STACK_API_KEY')

class Data():
    stocks = ["AAPL", "BB", "GME", "UBER", "TSLA", "SHOP", "PLTR"]

price_dict = {}
for name in Data.stocks:
    price_dict = {}
    object = requests.get(f"http://api.marketstack.com/v1/eod?access_key={MARKET_STACK_API_KEY}&symbols={name}&date_from=2015-01-01").json()
    object = requests.get(f"http://api.marketstack.com/v1/eod?access_key=713d8bdd9b293056ed674b25b19aeb94&symbols={name}&date_from=2015-01-01").json()
    tempdates, tempdata = [], []
    for data in object["data"]:
        if data["close"] != None:
            tempdates.append(data["date"][:10])
            tempdata.append(data["close"])
    price_dict = {
        "name": object["data"][0]["symbol"],
        "dates": tempdates[::-1],
        "data": tempdata[::-1]
    }

    # Check if the stock is in the db.
    stock = StockData.query.filter_by(name=price_dict.get("name")).first()

    if not stock:
        stock = StockData(name=price_dict.get("name"), json_string=json.dumps(price_dict))
        stock.save_to_db()

    #if not in db
    #send to db
print(price_dict)
# Dictionary format:
# price_dict = {
#   "name": "TSLA",
#   "dates": [2020-10-06", "2020-10-07"],
#   "data": [420, 500]
# }