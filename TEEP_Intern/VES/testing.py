import json
from datetime import datetime

# Get the timestamp of the current time (in microseconds)
timestamp = datetime.utcnow().timestamp()
# Convert the timestamp to seconds
time_in_s = int(timestamp)
# Get the microsecond part
time_ms = int((timestamp - time_in_s) * 1000000)
# Format the time
event_time = datetime.utcfromtimestamp(time_in_s).strftime('%Y-%m-%dT%H:%M:%S') + f'.{time_ms:06d}Z'

# Round down to the nearest multiple of 900 seconds
collection_end_time = int(timestamp - (timestamp % 900))
# Calculate the timestamp for 900 seconds before collectionEndTime
collection_start_time = collection_end_time - 900
# Convert collectionStartTime and collectionEndTime to microseconds
collection_start_time_micros = collection_start_time * 1000000
collection_end_time_micros = collection_end_time * 1000000
# Format collectionStartTime and collectionEndTime as readable time strings
interval_start_time = datetime.utcfromtimestamp(collection_start_time).strftime('%a, %d %b %Y %H:%M:%S GMT')
interval_end_time = datetime.utcfromtimestamp(collection_end_time).strftime('%a, %d %b %Y %H:%M:%S GMT')

# Set granularity
granularity = "PM1min"

event_id = "f2030d4z-8f0e-11eb-8dcd-0242ac130003"

def generate_json(mqtt_data):
    template = {
        "event": {
            "commonEventHeader": {
                "domain": "measurement",
                "eventId": event_id,
                "eventName": "oran_pm",
                "eventType": "PM",
                "sequence": 0,
                "priority": "Low",
                "reportingEntityId": "",
                "reportingEntityName": "node1.cluster.local",
                "sourceId": "",
                "sourceName": "BBU_greigns",
                "startEpochMicrosec": collection_start_time_micros,
                "lastEpochMicrosec": collection_end_time_micros,
                "internalHeaderFields": {
                    "intervalStartTime": interval_start_time,
                    "intervalEndTime": interval_end_time
                },
                "version": "4.1",
                "vesEventListenerVersion": "7.2.1"
            },
            "measurementFields": {
                "additionalFields": {
                    "ran_id": mqtt_data["ran_id"],
                    "src_id": mqtt_data["src_id"]
                },
                "additionalMeasurements": [
                    {
                        "name": "pm_data",
                        "hashMap": {k: str(v) for k, v in mqtt_data["pm_data"].items()}
                    }
                ],
                "measurementInterval": 15,
                "measurementFieldsVersion": "4.0"
            }
        }
    }

    return template

def convert_to_pm_data(input_data):
    pm_data = {
        "ran_id": input_data["ran_id"],
        "src_id": input_data["src_id"],
        "pm_data": {
            "num_of_socket": input_data["pm_data"]["num_of_socket"],
            "total_current": input_data["pm_data"]["total_current"],
            "total_powerload": input_data["pm_data"]["total_powerload"]
        }
    }
    
    # Iterate over each socket and add its attributes to pm_data with an index suffix
    for i, socket in enumerate(input_data["pm_data"]["socket"]):
        pm_data["pm_data"][f"socket_id_{i+1}"] = socket["socket_id"]
        pm_data["pm_data"][f"socket_voltage_{i+1}"] = socket["socket_voltage"]
        pm_data["pm_data"][f"socket_current_{i+1}"] = socket["socket_current"]
        pm_data["pm_data"][f"socket_powerload_{i+1}"] = socket["socket_powerload"]
    
    return pm_data

# Example input data structure as provided
input_data = {
    "ran_id": "ran1",
    "src_id": "gNB_RU",
    "pm_data": {
        "num_of_socket": 4,
        "total_current": 10.5,
        "total_powerload": 23270,
        "socket": [
            {"socket_id": 0, "socket_voltage": 386519.04, "socket_current": 5862, "socket_powerload": 188984852.48},
            {"socket_id": 1, "socket_voltage": 386519.04, "socket_current": 5862, "socket_powerload": 188984852.48},
            {"socket_id": 2, "socket_voltage": 386519.04, "socket_current": 5862, "socket_powerload": 188984852.48},
            {"socket_id": 3, "socket_voltage": 386519.04, "socket_current": 5862, "socket_powerload": 188984852.48}
        ]
    }
}

# Convert input data to pm_data format
pm_data = convert_to_pm_data(input_data)

# Generate the JSON with stringified measurement data
mqtt_data = generate_json(pm_data)

print(json.dumps(mqtt_data, indent=4))
