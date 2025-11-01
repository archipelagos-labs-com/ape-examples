"""
Retrieve the status published by a specified device in a given time period using credentials supplied directly.
"""
import requests
import json


# User credentials

username = "<PROVIDE-USERNAME>"
username = "admin"

api_key = "<PROVIDE-API-KEY>"
api_key = '54e696ee-243b-46bb-9b75-ea1c5f94e70e'

# URL for the Data Service

data_service = "<PROVIDE-DATA-SERVICE-URL>"
data_service = "http://localhost:32000"

# Devices and fields of interest

device = "70b3d57ba00007b0"
fields = ["batteryLevel", "margin"]

# Period of interest

start = "2025-10-01T00:00:00"
end = "2025-10-31T23:59:59"

# JSON request to send; remove "fields" if you want all fields for a device

request = {
    "username": username,
    "apiKey": api_key,
    "networkDeviceId": device,
    "fields": fields,
    "start": start,
    "end": end,
    "tenantName": "wicks-farm"
}

# Send the request

request_url = data_service + '/v1/device/status/get'
response = requests.post(request_url, json=request)

if response.status_code == 200:
    # Parse the response

    response_json = response.json()

    # Inspect the response

    error_code = response_json["errorCode"]

    if error_code == 0:
        time_series = response_json["timeSeries"]

        print(f'An error code of {error_code} was returned signalling that the request was successful.')
        print(f'The JSON response received from the Data Service was:\n')
        print(json.dumps(time_series, indent=4))
    else:
        error_message = response_json["errorMessage"]

        print(f'An error code of {error_code} was returned signalling that an error occurred.')
        print(f'The associated error message was "{error_code}".')
        print(f'The JSON response received from the Data Service was:\n')
        print(json.dumps(response_json, indent=4))
else:
    print(f'A HTTP code of {response.status_code} was returned signalling that an error occurred.')
    print(f"The associated error message was '{response.content.decode("utf-8")}'.")
