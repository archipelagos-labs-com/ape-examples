"""
Subscribe all the streaming device data that a user has access to.
"""
from urllib.parse import urlencode
from datetime import datetime
import websockets
import asyncio
import json


# User credentials

username = "<PROVIDE-USERNAME>"
api_key = "<PROVIDE-API-KEY>"

# URL for the Streaming Service

streaming_service = "<PROVIDE-STREAMING-SERVICE-URL>"

# Type of data to receive

data_type = "device-uplink-data"

# Function that receives streaming data

async def subscribe(uri: str):
    """
    (Blocking) Function that gets executed by the asyncio run function.
    """
    # Continuously subscribe to messages

    async with websockets.connect(uri) as websocket:
        async for message in websocket:
            # Parse the JSON message

            json_message = json.loads(message)

            # Obtain the message header and body

            header = json_message["header"]
            body = json_message["body"]

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


# Build the URI to use when subscribing

query_params = {"username": username,
                "api-key": api_key}

if data_type is not None:
    query_params["data-type"] = data_type

query_params = urlencode(query_params, doseq=False, safe='', encoding=None, errors=None)
uri = streaming_service + "/subscribe?" + query_params

# Start subscribing

asyncio.run(subscribe(uri=uri))
