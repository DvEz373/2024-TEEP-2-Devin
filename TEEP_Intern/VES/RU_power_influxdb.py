from influxdb_client import InfluxDBClient, Point
from influxdb_client.client.write_api import SYNCHRONOUS
import json
from datetime import datetime

# InfluxDB connection configuration
host = '192.168.0.237'  # InfluxDB hostname or IP address
port = 30001         # InfluxDB port number
database = 'RU_power' # InfluxDB database name
username = 'admin'  # InfluxDB username
password = 'lun6ty62sIJekDKEswGRJH9L8SX95jsD'  # InfluxDB password

# Create InfluxDB client object
client = InfluxDBClient(url=f"http://{host}:{port}", token="i1hL1dOtZiR5FWAACDKgiAznEjnqyHIT", org="influxdata")
write_api = client.write_api(write_options=SYNCHRONOUS)

def json_to_influx_points(data):
    points = []
    measurement = "power_data"
    timestamp = datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ')

    # Add general information point
    general_tags = {"type": "general"}
    general_fields = {
        "num_of_socket": data["num_of_socket"],
        "total_current": data["total_current"],
        "total_powerload": data["total_powerload"]
    }
    general_point = {
        "measurement": measurement,
        "tags": general_tags,
        "fields": general_fields,
        "time": timestamp
    }
    points.append(general_point)

    # Add socket-specific information points
    for socket in data["socket"]:
        socket_tags = {"type": "socket", "socket_id": str(socket["socket_id"])}
        socket_fields = {
            "socket_voltage": socket["socket_voltage"],
            "socket_current": socket["socket_current"],
            "socket_powerload": socket["socket_powerload"]
        }
        socket_point = {
            "measurement": measurement,
            "tags": socket_tags,
            "fields": socket_fields,
            "time": timestamp
        }
        points.append(socket_point)

    return points

# Input JSON Data
input_data = {
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

points = json_to_influx_points(input_data)

# Write data to InfluxDB
write_api.write(bucket=database, record=points)
print("Data sent to InfluxDB successfully.")