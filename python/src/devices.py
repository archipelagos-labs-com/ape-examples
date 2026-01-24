"""
Retrieve details for all devices that a user can access using credentials supplied in an ape.toml file.
"""
from ape_client import Client


# Login to platform

client = Client()
client.login()

# Retrieve and display devices

devices = client.get_device()
print(devices)
