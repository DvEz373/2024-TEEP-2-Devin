import json
import requests
from datetime import datetime
import random
import string

import paho.mqtt.client as mqtt

# Get the current timestamp in microseconds
timestamp = datetime.utcnow().timestamp()
# Convert the timestamp to seconds
time_in_s = int(timestamp)
# Get the milliseconds part
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

def generate_event_id(prefix='other_', length=10):
    random_string = ''.join(random.choices(string.ascii_uppercase + string.digits, k=length))
    return prefix + random_string

event_id = generate_event_id()

def generate_json1(mqtt_data):
    template = {
        "event": {
            "commonEventHeader": {
                "domain": "other",
                "eventId": event_id,
                "eventName": "ue_info",
                "eventType": "ue_pm",
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
            "otherFields": {
                "otherFieldsVersion": "3.0",
                "arrayOfNamedHashMap": [
                {
                "name": "total",
                "hashMap": {
                    "num_of_ue": str(mqtt_data['num_of_ue']),
                    "total_ul_tp": str(mqtt_data['total_ul_tp']),
                    "total_ul_pkt":str(mqtt_data['total_ul_pkt']),
                    "total_dl_tp":str(mqtt_data['total_dl_tp']),
                    "total_dl_pkt":str(mqtt_data['total_dl_pkt'])
                }
                }
                ]
             }
        }
    }

    return template

def generate_json2(mqtt_data):
    ue_array = []

    for i in range(mqtt_data['num_of_ue']):
        ue_info = mqtt_data['ue'][i]
        ue_payload = {
            "name": "personal",
            "hashMap": {
                "ue_id": str(ue_info['ue_id']),
                "ul_tp": str(ue_info['ul_tp']),
                "ul_pkt": str(ue_info['ul_pkt']),
                "dl_tp": str(ue_info['dl_tp']),
                "dl_pkt": str(ue_info['dl_pkt'])
            }
        }
        ue_array.append(ue_payload)

    template = {
        "event": {
            "commonEventHeader": {
                "domain": "other",
                "eventId": event_id,
                "eventName": "ue_info",
                "eventType": "ue_pm",
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
            "otherFields": {
                "otherFieldsVersion": "3.0",
                "arrayOfNamedHashMap": [ue_array[i] for i in range(len(ue_array))]
            }
        }
    }

    return template

def send_http_request(payload):
    try:
        # Set the target address
        url = 'http://192.168.0.175:30417/eventListener/v7'

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
        json_payload = generate_json1(mqtt_data)  # or use generate_json2
        json_payload2 = generate_json2(mqtt_data)
        # Call the function to send the HTTP POST request
        send_http_request(json_payload)
        send_http_request(json_payload2)
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
client.subscribe('ran1/pdcp_tp')

# Start the loop
client.loop_forever()
