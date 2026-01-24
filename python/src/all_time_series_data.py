"""
Retrieve data for all accessible entities for a user in a given time period using credentials supplied in an ape.toml file.
"""
from ape_client import Client

from pandas import Timestamp


# Period of interest (UTC)

start = Timestamp(year=2025, month=10, day=1, hour=0, minute=0)
end = Timestamp(year=2025, month=10, day=1, hour=23, minute=59)

# Login to the platform

client = Client()
client.login()

# Retrieve metadata for all accessible entities

entities = client.get_entity()

for entity in entities:
    # Retrieve and display data for this entity

    df = client.get_time_series_data(code=entity.code, start=start, end=end)
    print(df)
