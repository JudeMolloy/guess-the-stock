import requests

stocks = ["AAPL", "BB", "GME", "UBER", "TSLA", "SHOP", "PLTR"]
for name in stocks:
    object = requests.get(f"http://api.marketstack.com/v1/eod?access_key=713d8bdd9b293056ed674b25b19aeb94&symbols={name}&date_from=2015-01-01").json()
    #if not in db
    #send to db

print("done")