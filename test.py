import json
import requests

import SECRETS

from pprint import pprint

headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Token ' + SECRETS.API_KEY
        }

# r = requests.get("https://api.tiingo.com/api/test",
#                                headers=headers)
# r = requests.get("https://api.tiingo.com/api/daily/aapl/prices",
#                  headers=headers)
# response = requests.get("https://api.tiingo.com/tiingo/daily/aapl/prices?startDate=2020-10-15",
#                         headers=headers)
# response = requests.get("https://api.tiingo.com/tiingo/crypto/top?tickers=curebtc",
#                         headers=headers)
response = requests.get("https://api.tiingo.com/tiingo/crypto/prices?tickers=btcusd&startDate=2020-10-21&resampleFreq=5min",
                         headers=headers)

r = response.json()
# pprint(r)

for request in r:
    pprint(request)
