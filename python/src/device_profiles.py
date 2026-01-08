"""
Retrieve details for the device profiles associated with devices belonging to a specified tenant.
"""
from ape_client import Client


# Tenant name

tenant = "<ENTER-TENANT-NAME>"

# Login to platform

client = Client()
client.login()

# Retrieve the tenant

tenant = client.get_tenant_named(tenant_name=tenant)

# Retrieve all devices for the tenant

devices = client.get_devices(tenant_id=tenant.tenant_id)

for device in devices:
    # Retrieve and display the device profile for this device

    device_profile = client.get_device_profile(device_profile_id=device.device_profile_id)
    print(device_profile)
