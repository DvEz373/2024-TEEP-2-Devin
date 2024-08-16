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


def generate_event_id(prefix='fault_', length=10):
    random_string = ''.join(random.choices(string.ascii_uppercase + string.digits, k=length))
    return prefix + random_string

event_id = generate_event_id()

def generate_json(mqtt_data):
    event_id = generate_event_id()

    a = mqtt_data['notification']['alarm-notif']['is-cleared']
    if a == "false":
        a = "Idle"
    elif a == "true":
        a = "Active"

    template = {
        "event": {
            "commonEventHeader": {
                "domain": "fault",
                "eventId": event_id,
                "eventName": mqtt_data['notification']['alarm-notif']['fault-text'],
                "eventType": "oam_Alarms",
                "sequence": 0,
                "priority": "High",
                "reportingEntityId": "",
                "reportingEntityName": mqtt_data['notification']['alarm-notif']['ran-id'],
                "sourceId": "",
                "sourceName": mqtt_data['notification']['alarm-notif']['ran-id'],
                "startEpochMicrosec": collection_start_time_micros,
                "lastEpochMicrosec": collection_end_time_micros,
                "nfNamingCode": "oam",
                "nfVendorName": "gregins",
                "timeZoneOffset": "+00:00",
                "version": "4.1",
                "vesEventListenerVersion": "7.2.1"
            },
            "faultFields": {
                "faultFieldsVersion": "4.0",
                "eventSeverity": mqtt_data['notification']['alarm-notif']["fault-severity"],
                "eventSourceType": "fault",
                "eventCategory": "network",
                "alarmCondition": mqtt_data['notification']['alarm-notif']["fault-text"],
                "specificProblem": mqtt_data['notification']['alarm-notif']["fault-text"],
                "vfStatus": a,
                "alarmInterfaceA": "N/A"
            }
        }
    }

    print("Generated JSON template:", template)
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
client.subscribe('netconf-proxy/oran-o1/fm')

# Start the loop
client.loop_forever()
