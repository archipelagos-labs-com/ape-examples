"""
Retrieve time series data for a specified entity in a given time period using credentials supplied in an ape.toml file.
"""
from ape_client import Client

from pandas import Timestamp


# Entity of interest

code = "<PROVIDE-ENTITY-CODE>"

# Period of interest

start = Timestamp(year=2026, month=1, day=25, hour=0, minute=0)
end = Timestamp(year=2026, month=1, day=25, hour=23, minute=59)

# Login to the platform

client = Client()
client.login()

# Retrieve and display time series data

df = client.get_time_series_data(code=code, start=start, end=end)
print(df)
