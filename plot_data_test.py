import json
import requests
import numpy
import matplotlib

import SECRETS

from pprint import pprint

headers = {
    "Content-type": "application/json",
    "Authorization": "Token " + SECRETS.API_KEY
}

response = requests.get("https://api.tiingo.com/tiingo/crypto/prices?tickers=btcusd&startDate=2020-10-21&resampleFreq=4hour",
                        headers=headers)

r = response.json()
price_data = r[0]["priceData"]


for point in price_data:
    pass
