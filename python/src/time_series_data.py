"""
Retrieve data for a specified time series in a given time period using credentials supplied in an ape.toml file.
"""
from ape_client import Client

from pandas import Timestamp


# Time series code and fields of interest

code = "OM-SR-FORECAST-H"
fields = ["forecast"]

# Period of interest

start = Timestamp(year=2025, month=10, day=1, hour=0, minute=0)
end = Timestamp(year=2025, month=10, day=1, hour=23, minute=59)

# Login to the platform

client = Client()
client.login()

# Retrieve and display time series data

df = client.get_time_series_data(code=code, fields=fields, start=start, end=end)
print(df)
