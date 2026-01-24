"""
Retrieve data for all accessible devices for a user in a given time period using credentials supplied in an ape.toml file.
"""
from ape_client import Client

from pandas import Timestamp


# Period of interest (UTC)

start = Timestamp(year=2025, month=10, day=1, hour=0, minute=0)
end = Timestamp(year=2025, month=10, day=1, hour=23, minute=59)

# Login to the platform

client = Client()
client.login()

# Retrieve metadata for all accessible devices

devices = client.get_device()

for device in devices:
    # Retrieve and display data for this device

    df = client.get_device_data(network_device_id=device.network_device_id, lower_limit=start, upper_limit=end)
    print(df)
