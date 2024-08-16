import json
import requests
from datetime import datetime

import paho.mqtt.client as mqtt

# Get the timestamp of the current time (in microseconds)
timestamp = datetime.utcnow().timestamp()
# Convert the timestamp to seconds
time_in_s = int(timestamp)
# Get the millisecond part
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
                    "intervalStartTime":interval_start_time ,
                    "intervalEndTime": interval_end_time
                },
                "version": "4.1",
                "vesEventListenerVersion": "7.2.1"
            },
            "measurementFields": {
                "additionalFields": {
                    "ran_id": "1",
                    "src_id": "gNB_RU"
                },
                "additionalMeasurements": [
                    {
                        "name": "pm_data",
                        "hashMap": mqtt_data["pm_data"]
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

def send_http_request(payload):
    try:
        # Set the target address
        url = 'http://192.168.0.237:30417/eventListener/v7'

        # Set the username and password
        username1 = 'sample1'
        password1 = 'sample1'

        headers = {'content-type': 'application/json'}
        verify = False

        # Send the HTTP POST request
        response = requests.post(url, json=payload, auth=(username1, password1), headers=headers, verify=verify)

        # Check the response status code
        if response.status_code >= 200 and response.status_code <= 300:
            print(payload)
            print('Data sent successfully')
        else:
            print('Failed to send data:', response.text)
    except Exception as e:
        print('Error occurred while sending data:', e)


# MQTT message callback function
def on_message(client, userdata, msg):
    try:
        # Convert the message to a UTF-8 encoded string and print it
        payload_str = msg.payload.decode("utf-8")
        print("Received message:", payload_str)

        # Parse the JSON string into a Python object
        mqtt_data = json.loads(payload_str)

        # Generate the JSON data to be sent
        json_payload = generate_json(mqtt_data)

        # Call the function to send the HTTP POST request
        send_http_request(json_payload)
    except Exception as e:
        print('Error occurred while sending data:', e)


# Set up the MQTT client
client = mqtt.Client(protocol=mqtt.MQTTv311)
client.on_message = on_message

# Connect to the MQTT broker
broker_address = '192.168.135.102'
broker_port = 1883
client.connect(broker_address, broker_port)

# Subscribe to the topic
client.subscribe('netconf-proxy/oran-o1/pm')

# Start the loop
client.loop_forever()
