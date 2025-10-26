"""
Retrieve data for a specified device in a given time period.
"""
from ape_client import Client

from pandas import Timestamp


# Devices and fields of interest

device = "70b3d57ba00007b0"
fields = ["air_temperature", "air_humidity"]

# Period of interest

start = Timestamp(year=2025, month=4, day=25, hour=0, minute=0)
end = Timestamp(year=2025, month=5, day=25, hour=23, minute=59)

# Login to the platform

client = Client()
client.login()

# Retrieve and display device data

df = client.get_device_data(network_device_id=device, lower_limit=start, upper_limit=end)
print(df)
