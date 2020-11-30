import requests
import time


bitcoin_api = "https://api.coindesk.com/v1/bpi/currentprice.json"

while True:
    data = requests.get(bitcoin_api)
    data = eval(data.text) 
    print(data['bpi']['USD']['rate'])
    time.sleep(60)