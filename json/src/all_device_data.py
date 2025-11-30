"""
Retrieve data for all accessible devices for a user in a given time period using credentials supplied directly.
"""
import requests
import json


# User credentials

username = "<PROVIDE-USERNAME>"
api_key = "<PROVIDE-API-KEY>"

# URL for the Data Service

data_service = "<PROVIDE-DATA-SERVICE-URL>"

# Period of interest (UTC)

start = "2025-10-01T00:00:00"
end = "2025-10-01T23:59:59"

# JSON request for retrieving device metadata

devices_request = {
    "username": username,
    "apiKey": api_key
}

# Retrieve metadata for all accessible devices

devices_request_url = data_service + '/v1/device/get'
devices_response = requests.post(devices_request_url, json=devices_request)

if devices_response.status_code == 200:
    # Parse the response

    response_json = devices_response.json()

    # Inspect the response

    error_code = response_json["errorCode"]

    if error_code == 0:
        # Process the metadata for all accessible devices

        devices = response_json["devices"]

        for device in devices:
            # Retrieve and display data for this device

            network_device_id = device["networkDeviceId"]

            # Retrieve and display data for this device

            device_data_request = {
                "username": username,
                "apiKey": api_key,
                "networkDeviceId": network_device_id,
                "start": start,
                "end": end
            }

            device_data_request_url = data_service + '/v1/device/data/get'
            device_data_response = requests.post(device_data_request_url, json=device_data_request)

            if device_data_response.status_code == 200:
                # Parse the response

                response_json = device_data_response.json()
                error_code = response_json["errorCode"]

                if error_code == 0:
                    time_series = response_json["timeSeries"]

                    print(f'The data returned for the device "{network_device_id}" was:\n')
                    print(json.dumps(time_series, indent=4))
                else:
                    error_message = response_json["errorMessage"]

                    print(f'An error code of {error_code} was returned when requesting data for the device "{network_device_id}".')
                    print(f'The associated error message was "{error_code}".')
                    print(f'The JSON response received from the Data Service was:\n')
                    print(json.dumps(response_json, indent=4))
            else:
                print(f'A HTTP code of {device_data_response.status_code} was returned when requesting data for the device "{network_device_id}".')
                print(f"The associated error message was '{device_data_response.content.decode("utf-8")}'\n.")
    else:
        error_message = response_json["errorMessage"]

        print(f'An error code of {error_code} was returned when requesting metadata for all accessible devices.')
        print(f'The associated error message was "{error_code}".')
        print(f'The JSON response received from the Data Service was:\n')
        print(json.dumps(response_json, indent=4))
else:
    print(f'A HTTP code of {devices_response.status_code} was returned when requesting metadata for all accessible devices.')
    print(f"The associated error message was '{devices_response.content.decode("utf-8")}'.")
