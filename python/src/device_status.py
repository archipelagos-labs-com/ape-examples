"""
Retrieve the status published by a specified device in a given time period using credentials supplied in an ape.toml file.
"""
from ape_client import Client

from pandas import Timestamp


# Device of interest

network_device_id = "<PROVIDE-NETWORK-DEVICE-ID>"

# Period of interest (UTC)

start = Timestamp(year=2025, month=10, day=1, hour=0, minute=0)
end = Timestamp(year=2025, month=10, day=31, hour=23, minute=59)

# Login to the platform

client = Client()
client.login()

# Retrieve and display data

df = client.get_device_status(network_device_id=network_device_id, start=start, end=end)
print(df)
