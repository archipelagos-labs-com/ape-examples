"""
Retrieve time series data for all accessible entities for a user in a given time period using credentials supplied directly.
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

# Retrieve metadata for all accessible entities

entities_request_url = data_service + '/v1/entity/get'
entities_response = requests.post(entities_request_url, json=devices_request)

if entities_response.status_code == 200:
    # Parse the response

    response_json = entities_response.json()

    # Inspect the response

    error_code = response_json["errorCode"]

    if error_code == 0:
        # Process the metadata for all accessible entities

        entities = response_json["entities"]

        for entity in entities:
            # Retrieve and display data for this entity

            code = entity["code"]

            # Retrieve and display data for this entity

            device_data_request = {
                "username": username,
                "apiKey": api_key,
                "code": code,
                "start": start,
                "end": end
            }

            entity_time_series_data_request_url = data_service + '/v1/entity/time-series/get'
            entity_time_series_data_response = requests.post(entity_time_series_data_request_url, json=device_data_request)

            if entity_time_series_data_response.status_code == 200:
                # Parse the response

                response_json = entity_time_series_data_response.json()
                error_code = response_json["errorCode"]

                if error_code == 0:
                    time_series = response_json["timeSeries"]

                    print(f'The time series data returned for the entity "{code}" was:\n')
                    print(json.dumps(time_series, indent=4))
                else:
                    error_message = response_json["errorMessage"]

                    print(f'An error code of {error_code} was returned when requesting time series data for the entity "{code}".')
                    print(f'The associated error message was "{error_code}".')
                    print(f'The JSON response received from the Data Service was:\n')
                    print(json.dumps(response_json, indent=4))
            else:
                print(f'A HTTP code of {entity_time_series_data_response.status_code} was returned when requesting time series data for the entity "{code}".')
                print(f"The associated error message was '{entity_time_series_data_response.content.decode("utf-8")}'\n.")
    else:
        error_message = response_json["errorMessage"]

        print(f'An error code of {error_code} was returned when requesting metadata for all accessible entities.')
        print(f'The associated error message was "{error_code}".')
        print(f'The JSON response received from the Data Service was:\n')
        print(json.dumps(response_json, indent=4))
else:
    print(f'A HTTP code of {entities_response.status_code} was returned when requesting metadata for all accessible entities.')
    print(f"The associated error message was '{entities_response.content.decode("utf-8")}'.")
