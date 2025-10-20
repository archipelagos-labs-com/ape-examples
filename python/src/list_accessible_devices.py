"""
Retrieve details for all devices that a user can access.
"""
from ape_client import Client


# Login to platform

client = Client()
client.login()

# Retrieve and display devices

devices = client.get_devices()
print(devices)
