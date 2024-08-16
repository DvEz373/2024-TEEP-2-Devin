# AI/ML Model

## MQTT Data Collection
NIC:
ens18 -> 192.168.0.237
ens19 -> 192.168.135.199
```bash
sudo ifconfig ens19 192.168.135.199
```
MQTT Sub Command: (To be able to collect data via MQTT from BBU)
```bash
mosquitto_sub -h 192.168.135.102 -p 1883 -t netconf-proxy/oran-o1/pm -u guest -P guest
```

## SNMP Data Collection for socket information
```bash
crontab -e
```
edit to this:
```bash
# Edit this file to introduce tasks to be run by cron.
#
# Each task to run has to be defined through a single line
# indicating with different fields when the task will be run
# and what command to run for the task
#
# To define the time you can provide concrete values for
# minute (m), hour (h), day of month (dom), month (mon),
# and day of week (dow) or use '*' in these fields (for 'any').
#
# Notice that tasks will be started based on the cron's system
# daemon's notion of time and timezones.
#
# Output of the crontab jobs (including errors) is sent through
# email to the user the crontab file belongs to (unless redirected).
#
# For example, you can run a backup of all your user accounts
# at 5 a.m every week with:
# 0 5 * * 1 tar -zcf /var/backups/home.tgz /home/
#
# For more information see the manual pages of crontab(5) and cron(8)
#
# m h  dom mon dow   command
*/1 * * * * /usr/bin/python3 /home/ubuntu/influxdb_data_collect.py
```
the code for `influxdb_data_collect.py`:
```python
from pysnmp.hlapi import SnmpEngine, CommunityData, UdpTransportTarget, ContextData, ObjectType, ObjectIdentity, nextCmd
from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import WriteOptions
import datetime

# Parameter Settings
INFLUXDB_URL = "http://192.168.0.237:30001"
BUCKET = "socket_info"
ORG = "influxdata"
TOKEN = "PjyOR0GXhjDXDdtx4Hx8J7E6PfvLUvNU" # Change to your InfluxDB Token

# Target SNMP Server
SNMP_HOST = "192.168.1.10"
COMMUNITY = "public"

# OID and Field Name Mapping Table
OIDS = {
    "outVoltage": ".1.3.6.1.4.1.26104.3.3.3.1.6",
    "outCurrent": ".1.3.6.1.4.1.26104.3.3.3.1.7",
    "outPowerLoad": ".1.3.6.1.4.1.26104.3.3.3.1.9"
}

# Initialize InfluxDB Client
client = InfluxDBClient(url=INFLUXDB_URL, token=TOKEN, org=ORG)
write_api = client.write_api(write_options=WriteOptions(batch_size=1))

def snmp_walk(oid):
    results = []
    for (errorIndication, errorStatus, errorIndex, varBinds) in nextCmd(
        SnmpEngine(),
        CommunityData(COMMUNITY),
        UdpTransportTarget((SNMP_HOST, 161)),
        ContextData(),
        ObjectType(ObjectIdentity(oid)),
        lexicographicMode=False
    ):
        if errorIndication:
            print(errorIndication)
            break
        elif errorStatus:
            print('%s at %s' % (errorStatus.prettyPrint(),
                                errorIndex and varBinds[int(errorIndex) - 1][0] or '?'))
            break
        else:
            for varBind in varBinds:
                results.append(varBind)
    return results

def main():
    for measurement, oid in OIDS.items():
        varBinds = snmp_walk(oid)
        for varBind in varBinds:
            oid_index = str(varBind[0]).split('.')[-1]
            value = float(varBind[1])
            timestamp = datetime.datetime.utcnow().isoformat()  # Generate unique timestamps
            point = Point(measurement).tag("index", oid_index).field("value", value).time(timestamp, WritePrecision.NS)
            write_api.write(bucket=BUCKET, org=ORG, record=point)
    write_api.flush()  # Ensure that all pending write operations complete

if __name__ == "__main__":
    main()
    write_api.close()  # Ensure that all writes are completed before closing the client
    client.close()
```

## Physical Resource Block Prediction for On/Off Cell
Using **LSTM** Model for **Time Series Forecasting** to be able to predict future usage of Physical Resource Block.

### Input Parameters
Here is the table with corresponding parameters formatted as bullet points:

| Parameter Name                | Yes/No | Corresponding Parameters                                  |
|-------------------------------|--------|----------------------------------------------------------|
| Data Volume                   | Yes    | - Sys.DataVolumeDL                                       |
| UL/DL UE Throughput           | Yes    | - total_ul_tp                                            |
|                               |        | - total_dl_tp                                            |
|                               |        | - ul_tp                                                  |
|                               |        | - dl_tp                                                  |
| RLC PDU Volume                | Yes    | - QosFlow.PdcpPduVolumeDL                                |
|                               |        | - QosFlow.PdcpPduVolumeUL                                |
| Active UEs                    | Yes    | - num_of_ue                                              |
| UL/DL Total PRB Usage         | Yes    | - RRU.PrbTotDL                                           |
|                               |        | - RRU.PrbTotUL                                           |
| RU (Power, Voltage, Current)  | Yes    | - inFeedVoltage                                          |
|                               |        | - inFeedCurrent                                          |
|                               |        | - inFeedPowerLoad                                        |
| PDU (Power, Voltage, Current) | Yes    | - outVoltage                                             |
|                               |        | - outCurrent                                             |
|                               |        | - outPowerLoad                                           |
|                               |        | - inFeedPowerLoad                                        |

Additional notes:
1. Temperature measurement is not feasible.
2. inFeedPowerLoad refers to total power load.

### Output Parameters (Prediction)
* RRU.PrbTotDl (Total PrB Usage DownLink) in future timesteps
* RRU.PrbTotUl (Total PrB Usage UpLink) in future timesteps

