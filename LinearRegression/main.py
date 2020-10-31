import requests

import pandas as pd

import SECRETS

headers = {
    "Content-type": "application/json",
    "Authorization": "Token " + SECRETS.API_KEY
}

startDate = "2020-10-23"
endDate = "2020-10-30"

response = requests.get("""https://api.tiingo.com/tiingo/crypto/prices?tickers=btcusd&startDate=""" + startDate + """&endDate=""" + endDate + """&resampleFreq=4hour""",
                        headers=headers)

r = response.json()
price_data = r[0]["priceData"]
price_data = pd.DataFrame(price_data)
print(price_data.head())
