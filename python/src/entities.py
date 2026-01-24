"""
Retrieve details for all devices.py that a user can access using credentials supplied in an ape.toml file.
"""
from ape_client import Client


# Login to platform

client = Client()
client.login()

# Retrieve and display entities

entities = client.get_entity()
print(entities)
