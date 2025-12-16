"""
Retrieve data for a specified device in a given time period using credentials supplied directly.
"""
import requests
import json


# User credentials

username = "<PROVIDE-USERNAME>"
api_key = "<PROVIDE-API-KEY>"

# URL for the Data Service

data_service = "<PROVIDE-DATA-SERVICE-URL>"

# Device of interest

network_device_id = "<PROVIDE-NETWORK-DEVICE-ID>"

# Fields of interest

fields = ["ambient_temperature", "relative_humidity"]

# Period of interest (UTC)

start = "2025-10-01T00:00:00"
end = "2025-10-01T23:59:59"

# JSON request to send; remove "fields" if you want all fields for a device

request = {
    "username": username,
    "apiKey": api_key,
    "networkDeviceId": network_device_id,
    "fields": fields,
    "start": start,
    "end": end
}

# Send the request

request_url = data_service + '/v1/device/data/get'
response = requests.post(request_url, json=request)

if response.status_code == 200:
    # Parse the response

    response_json = response.json()

    # Inspect the response

    error_code = response_json["errorCode"]

    if error_code == 0:
        time_series = response_json["timeSeries"]

        print(f'The device data returned for the device "{network_device_id}" was:\n')
        print(json.dumps(time_series, indent=4))
    else:
        error_message = response_json["errorMessage"]

        print(f'An error code of {error_code} was returned.')
        print(f'The associated error message was "{error_code}".')
        print(f'The JSON response received from the Data Service was:\n')
        print(json.dumps(response_json, indent=4))
else:
    print(f'A HTTP code of {response.status_code} was returned.')
    print(f"The associated error message was '{response.content.decode("utf-8")}'.")
