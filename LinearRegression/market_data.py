# import requests

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

import LinearRegression

import helpers
# import SECRETS


####################################################################
# Just used to request data at start of project so I don't have to #
# poll the API every time I run this file                          #
####################################################################
# headers = {
#     "Content-type": "application/json",
#     "Authorization": "Token " + SECRETS.API_KEY
# }
#
# startDate = "2020-10-01"
# endDate = "2020-10-30"
#
# response = requests.get("""https://api.tiingo.com/tiingo/crypto/prices?tickers=btcusd&startDate=""" + startDate + """&endDate=""" + endDate + """&resampleFreq=1day""",
#                         headers=headers)
# r = response.json()
# price_data = r[0]["priceData"]
# price_data = pd.DataFrame(price_data)


# Data polled once a day for the month of October
#  price_data = pd.read_csv("btc_usd_oct.csv")
#  dates = price_data["date"]
#  cleaned_dates = pd.Series(list(map(helpers.remove_time, dates)))
#  dates_epoch = list(map(helpers.date_string_to_epoch, cleaned_dates))
#  opening_prices = price_data["open"]

#  transform_dates = lambda x : x - min(dates_epoch)
#  dates_epoch_norm = pd.Series(list(map(transform_dates, dates_epoch)))

#  transform_prices = lambda x : x - min(opening_prices)
#  opening_prices_norm = pd.Series(list(map(transform_prices, opening_prices)))

#  plt.title("BTC value in USD")
#  plt.gcf().subplots_adjust(bottom=0.2)
#  plt.scatter(dates_epoch_norm, opening_prices_norm)
#  plt.xticks(rotation=-90)
#  plt.savefig("market_data_no_trend.png")

#  r = LinearRegression.SimpleRegressor()
#  r.fit(dates_epoch_norm.to_numpy(), opening_prices_norm.to_numpy(), 38)

#  predict_X = np.array([dates_epoch_norm[0], dates_epoch_norm.iloc[-1]])
#  predict_y = r.predict_points(predict_X)
#  plt.plot(predict_X, predict_y)

#  plt.savefig("market_data_trend.png")

#  print("m: " + str(r.m))
#  print("c: " + str(r.c))

price_data = pd.read_csv("btc_usd_oct.csv")
dates = price_data["date"]
opening_prices = price_data["open"]

# Clean up dates
dates_cleaned = list(map(helpers.remove_time, dates))
dates_epoch = list(map(helpers.date_string_to_epoch, dates_cleaned))
transform_dates_epoch = lambda x : (x - min(dates_epoch))/(3600 * 24)
dates_epoch_norm = pd.Series(list(map(transform_dates_epoch, dates_epoch)))

# Clean up prices
transform_prices = lambda x : x - min(opening_prices)
opening_prices_norm = pd.Series(list(map(transform_prices, opening_prices)))

# Create plot without trendline
plt.title("BTC value in USD")
plt.gcf().subplots_adjust(bottom=0.2)
plt.scatter(dates_cleaned, opening_prices)
plt.xticks(rotation=-90)
plt.savefig("market_data_no_trend.png")

# Fit regressor
r = LinearRegression.SimpleRegressor()
r.fit(dates_epoch_norm, opening_prices_norm, 38)

# Get our prediction line
transform_dates_epoch_inv = lambda x : (x*3600*24) + min(dates_epoch)
transform_prices_inv = lambda x : x + min(opening_prices)

test_X = np.array([0, 29])
test_y = r.predict_points(test_X)

test_X = pd.Series(list(map(transform_dates_epoch_inv, test_X)))
test_y = pd.Series(list(map(transform_prices_inv, test_y)))

test_X_converted = pd.Series(list(map(helpers.epoch_to_date_string, test_X)))

plt.plot(test_X_converted, test_y)
plt.savefig("market_data_trend.png")

# print(dates_epoch_norm)
# print(opening_prices_norm)
