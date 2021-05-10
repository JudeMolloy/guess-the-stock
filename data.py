import json
import os
import requests
from app.models import StockData
from dotenv import load_dotenv

load_dotenv()

script = True

if script:
    
    MARKET_STACK_API_KEY = os.getenv('MARKET_STACK_API_KEY')

    class Data():
        res = requests.get("https://api.swaggystocks.com/wsb/sentiment/top?limit=500")
        stocks = res.json()[:100]
        stocks = list(map(lambda x:x['ticker'], stocks))

    for name in Data.stocks:
        price_dict = {}
        try:
            object = requests.get(f"http://api.marketstack.com/v1/eod?access_key={MARKET_STACK_API_KEY}&symbols={name}&date_from=2015-01-01").json()
        except:
            print("--error--")
        tempdates, tempdata = [], []
        if "error" not in object and object["data"] != []:
            for data in object["data"]:
                if data["close"] != None:
                    tempdates.append(data["date"][:10])
                    tempdata.append(data["close"])
            price_dict = {
                "name": object["data"][0]["symbol"],
                "dates": tempdates[::-1],
                "data": tempdata[::-1]
            }
            print(price_dict["name"])

            # Check if the stock is in the db.
            stock = StockData.query.filter_by(name=price_dict.get("name")).first()

            if not stock:
                stock = StockData(name=price_dict.get("name"), json_string=json.dumps(price_dict))
                stock.save_to_db()
    print("--SCRIPT COMPLETE--")
# Dictionary format:
# price_dict = {
#   "name": "TSLA",
#   "dates": [2020-10-06", "2020-10-07"],
#   "data": [420, 500]
# }