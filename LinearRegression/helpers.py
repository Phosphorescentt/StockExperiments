import time
from calendar import timegm


# Helper function to remove the time off the datetime string returned
# by the tiingo API - just cleans up plot rendering
def remove_time(date_time=str):
    date, _, __ = date_time.partition("T")
    return date


# Convert date string to unix epoch time
def date_string_to_epoch(date=str):
    utc_time = time.strptime(date, "%Y-%M-%d")
    epoch_time = timegm(utc_time)
    return epoch_time


# Convert epoch time to date string
def epoch_to_date_string(epoch=int):
    return time.strftime("%Y-%M-%d", time.localtime(epoch))
