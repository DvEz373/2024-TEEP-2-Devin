import xml.etree.ElementTree as ET
import json
import requests
from ncclient import manager

# Define device connection parameters
device_params = {
    "host": "192.168.135.102",
    "port": 830,
    "username": "netconf",
    "password": "Greigns-2022"
}

# NETCONF filter for retrieving configuration data
filter_str = """<multiran-cm xmlns="urn:reign-altran-o1-cm-multiran:1.0"/>"""

m = manager.connect(**device_params, hostkey_verify=False)
print("NETCONF Session Connected Successfully.")

get_reply = m.get(filter=('subtree', filter_str))
print("NETCONF GET Operation Result:")
print(get_reply)

# Parse the XML data
root = ET.fromstring(str(get_reply))

# Define the namespaces
namespaces = {
    'base': 'urn:ietf:params:xml:ns:netconf:base:1.0',
    'multiran': 'urn:reign-altran-o1-cm-multiran:1.0'
}

# Find all ran-id elements and their corresponding data
ran_data = {}
for multiran_cm in root.findall('.//multiran:multiran-cm', namespaces):
    ran_id = multiran_cm.find('multiran:ran-id', namespaces).text
    PLMNID = multiran_cm.find('.//multiran:PLMNID', namespaces).text
    BBU_IP = multiran_cm.find('.//multiran:IP_info/multiran:BBU_IP', namespaces).text
    BBU_NETMASK = multiran_cm.find('.//multiran:IP_info/multiran:BBU_NETMASK', namespaces).text
    BBU_Gateway_IP = multiran_cm.find('.//multiran:IP_info/multiran:BBU_Gateway_IP', namespaces).text
    AMF_IP = multiran_cm.find('.//multiran:IP_info/multiran:AMF_IP', namespaces).text
    gNB_ID = multiran_cm.find('.//multiran:NCI/multiran:gNB_ID', namespaces).text

    ran_data[ran_id] = {
        "PLMNID": PLMNID,
        "BBU_IP": BBU_IP,
        "BBU_NETMASK": BBU_NETMASK,
        "BBU_Gateway_IP": BBU_Gateway_IP,
        "AMF_IP": AMF_IP,
        "gNB_ID": gNB_ID
    }

# Function to create and send the POST request
def send_post_request(ran_id, ran_info):
    payload = {
        "event": {
            "commonEventHeader": {
                "domain": "other",
                "eventId": "node1.cluster.local_2024-04-19T08:51:36.801439+00:00Z",
                "eventName": "heartbeat_O_RAN_COMPONENT",
                "eventType": "O_RAN_COMPONENT",
                "lastEpochMicrosec": 1713516696801439,
                "nfNamingCode": "SDN-Controller",
                "nfVendorName": "O-RAN-SC OAM",
                "priority": "Low",
                "reportingEntityId": "",
                "reportingEntityName": "node1.cluster.local",
                "sequence": 357,
                "sourceId": "",
                "sourceName": "node1.cluster.local",
                "startEpochMicrosec": 1713516696801439,
                "timeZoneOffset": "+00:00",
                "version": "4.1",
                "vesEventListenerVersion": "7.2.1"
            },
            "otherFields": {
                "otherFieldsVersion": "3.0",
                "arrayOfNamedHashMap": [
                    {
                        "name": ran_id,
                        "hashMap": ran_info
                    }
                ]
            }
        }
    }

    # Convert payload to JSON string
    payload_json = json.dumps(payload, indent=2)

    # Define the URL and headers for the POST request
    url = "http://192.168.0.19:30417/eventListener/v7"
    headers = {
        "Content-Type": "application/json"
    }

    # Send the POST request
    response = requests.post(url, headers=headers, data=payload_json, auth=('sample1', 'sample1'), verify=False)
    print(payload_json)
    # Print the response
    print(response.status_code)
    print(response.text)

# Send separate POST requests for ran1 and ran2
for ran_id, ran_info in ran_data.items():
    send_post_request(ran_id, ran_info)