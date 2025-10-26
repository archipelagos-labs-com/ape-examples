"""
Retrieve the status published by a specified device in a given time period.
"""
from ape_client import Client

from pandas import Timestamp


# Devices and fields of interest

device = "70b3d57ba00007b0"
fields = ["batteryLevel", "margin"]

# Period of interest

start = Timestamp(year=2025, month=10, day=1, hour=0, minute=0)
end = Timestamp(year=2025, month=10, day=30, hour=23, minute=59)

# Login to the platform

client = Client()
client.login()

# Retrieve and display data

df = client.get_device_status(network_device_id=device, fields=fields, lower_limit=start, upper_limit=end)
print(df)
