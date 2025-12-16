"""
Retrieve data for a specified device in a given time period using credentials supplied directly.
"""
from ape_client import Client

from pandas import Timestamp


# User credentials

username = "<PROVIDE-USERNAME>"
password = "<PROVIDE-PASSWORD>"

# URL for the Data Service

data_service = "<PROVIDE-DATA-SERVICE-URL>"

# Device of interest

device = "<PROVIDE-NETWORK-DEVICE-ID>"

# Fields of interest

fields = ["air_temperature", "air_humidity"]

# Period of interest

start = Timestamp(year=2025, month=10, day=1, hour=0, minute=0)
end = Timestamp(year=2025, month=10, day=31, hour=23, minute=59)

# Login to the platform

client = Client(data_service=data_service)
client.login(username=username, password=password)

# Retrieve and display device data

df = client.get_device_data(network_device_id=device, lower_limit=start, upper_limit=end)
print(df)
