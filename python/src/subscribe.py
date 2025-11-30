"""
Subscribe all the streaming device data that a user has access to.
"""
from ape_client import Client

from datetime import datetime
from typing import Dict, Any


def data_received(message: Dict[str, Any]):
    """
    Called when data has been received.

    :param message: Message received.
    :type message: Dict[str, Any]
    """
    # Obtain the message header and body

    header = message["header"]
    body = message["body"]

    # Obtain relevant metadata from the header

    tenant_name = header["tenantName"]
    network_device_id = header["networkDeviceId"]

    # Parse timestamp at a second accuracy

    timestamp = body["timestamp"].split(".")[0]
    timestamp = datetime.strptime(timestamp, "%Y-%m-%dT%H:%M:%S")

    # Parse the field data

    to_print = f"Device '{network_device_id}' from '{tenant_name}' at '{timestamp.strftime("%H:%M:%S %d-%m-%Y")}' published: "
    fields = body["fields"]
    first = True

    for field_data in fields:
        # Obtain field name and value

        field_name = field_data["name"]
        field_value = field_data["value"]

        # Append data to the text to print

        if first:
            first = False
        else:
            to_print = to_print + ", "

        to_print = to_print + f"{field_name}={field_value}"

    # Print out message

    print(to_print)


# Login to the platform

client = Client()
client.login()

# Subscribe to streaming data

client.subscribe(data_type="device-uplink-data",
                 data_received=data_received)
