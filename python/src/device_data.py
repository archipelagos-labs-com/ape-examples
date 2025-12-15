"""
Retrieve data for a specified device in a given time period using credentials supplied in an ape.toml file.
"""
from ape_client import Client

from pandas import Timestamp


# Devices and fields of interest

network_device_id = "70b3d57ba00007b0"
fields = ["ambient_temperature", "relative_humidity"]

# Period of interest (UTC)

start = Timestamp(year=2025, month=10, day=1, hour=0, minute=0)
end = Timestamp(year=2025, month=10, day=1, hour=23, minute=59)

# Login to the platform

client = Client()
client.login()

# Retrieve and display device data

df = client.get_device_data(network_device_id=network_device_id, lower_limit=start, upper_limit=end, fields=fields)
print(df)
