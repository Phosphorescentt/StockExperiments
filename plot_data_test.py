import json
import requests

import matplotlib.pyplot as plt
import numpy as np

import SECRETS

from pprint import pprint

headers = {
    "Content-type": "application/json",
    "Authorization": "Token " + SECRETS.API_KEY
}

response = requests.get("https://api.tiingo.com/tiingo/crypto/prices?tickers=btcusd&startDate=2020-10-19&resampleFreq=4hour",
                        headers=headers)

r = response.json()
price_data = r[0]["priceData"]

open_prices = []
close_prices = []
low_prices = []
high_prices = []
dates = []

for price_point in price_data:
    open_prices.append(price_point["open"])
    close_prices.append(price_point["close"])
    low_prices.append(price_point["low"])
    high_prices.append(price_point["high"])
    dates.append(price_point["date"])

plt.title("Bitcoin value in USD")
plt.plot(dates, open_prices, label="Opening Prices")
plt.plot(dates, close_prices, label="Closing Prices")
plt.plot(dates, low_prices, label="Low Prices")
plt.plot(dates, high_prices, label="High Prices")
plt.legend()
plt.xticks(rotation=90)
plt.savefig("market_data.png")
