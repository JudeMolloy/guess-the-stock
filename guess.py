import os
import requests

MARKET_STACK_API_KEY = os.getenv('MARKET_STACK_API_KEY')

stocks = ["AAPL", "BB", "GME", "UBER", "TSLA", "SHOP", "PLTR"]

price_dict = {}
for name in stocks:
    price_dict = {}
    object = requests.get(f"http://api.marketstack.com/v1/eod?access_key={MARKET_STACK_API_KEY}&symbols={name}&date_from=2015-01-01").json()
    object = requests.get(f"http://api.marketstack.com/v1/eod?access_key=713d8bdd9b293056ed674b25b19aeb94&symbols={name}&date_from=2015-01-01").json()
    tempdates, tempdata = [], []
    for data in object["data"]:
        if data["close"] != None:
            tempdates.append(data["date"])
            tempdata.append(data["close"])
    price_dict= {
        "name": object["data"][0]["symbol"],
        "dates": tempdates,
        "data": tempdata
    }
    #if not in db
    #send to db
    
print(price_dict)
# Dictionary format:
# price_dict = {
#   "name": "TSLA",
#   "dates": [2020-10-06T00:00:00+0000", "2020-10-07T00:00:00+0000"],
#   "data": [420, 500]
# }