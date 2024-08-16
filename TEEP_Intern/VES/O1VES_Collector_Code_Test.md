# VES Data Collector (O1 Code and Test)
## K8S
### Delete Problematic Container in k8s
```bash
kubectl delete pods --field-selector=status.phase!=Running,status.phase!=Completed -n <namespace>
```

### Find k8s internal IP
```bash
kubectl get svc -n onap
```
output:
```bash
root@node1:~# kubectl get svc -n onap
NAME                                    TYPE        CLUSTER-IP      EXTERNAL-IP   PORT(S)                                        AGE
dcae-ves-collector                      NodePort    10.233.51.139   <none>        8080:30417/TCP                                 3d18h
http-cluster                            ClusterIP   None            <none>        2550/TCP                                       3d18h
mariadb-galera                          ClusterIP   10.233.59.42    <none>        3306/TCP                                       3d18h
mariadb-galera-headless                 ClusterIP   None            <none>        4567/TCP,4568/TCP,4444/TCP                     3d18h
message-router                          ClusterIP   10.233.10.242   <none>        3904/TCP                                       3d18h
neng-serv                               ClusterIP   10.233.58.133   <none>        8080/TCP                                       3d18h
onap-mariadb-galera-metrics             ClusterIP   10.233.40.207   <none>        9104/TCP                                       3d18h
onap-policy-mariadb-metrics             ClusterIP   10.233.10.229   <none>        9104/TCP                                       3d18h
onap-strimzi-kafka-0                    NodePort    10.233.62.43    <none>        9094:30490/TCP                                 3d18h
onap-strimzi-kafka-bootstrap            ClusterIP   10.233.55.71    <none>        9091/TCP,9092/TCP,9093/TCP                     3d18h
onap-strimzi-kafka-brokers              ClusterIP   None            <none>        9090/TCP,9091/TCP,8443/TCP,9092/TCP,9093/TCP   3d18h
onap-strimzi-kafka-external-bootstrap   NodePort    10.233.33.185   <none>        9094:30493/TCP                                 3d18h
onap-strimzi-zookeeper-client           ClusterIP   10.233.1.17     <none>        2181/TCP                                       3d18h
onap-strimzi-zookeeper-nodes            ClusterIP   None            <none>        2181/TCP,2888/TCP,3888/TCP                     3d18h
policy-apex-pdp                         ClusterIP   10.233.18.121   <none>        6969/TCP                                       3d18h
policy-api                              ClusterIP   10.233.51.69    <none>        6969/TCP                                       3d18h
policy-clamp-ac-a1pms-ppnt              ClusterIP   10.233.11.41    <none>        8086/TCP                                       3d18h
policy-clamp-ac-http-ppnt               ClusterIP   10.233.13.168   <none>        8084/TCP                                       3d18h
policy-clamp-ac-pf-ppnt                 ClusterIP   10.233.61.84    <none>        8085/TCP                                       3d18h
policy-clamp-runtime-acm                ClusterIP   10.233.48.109   <none>        6969/TCP                                       3d18h
policy-mariadb                          ClusterIP   10.233.29.202   <none>        3306/TCP                                       3d18h
policy-mariadb-headless                 ClusterIP   None            <none>        4567/TCP,4568/TCP,4444/TCP                     3d18h
policy-pap                              ClusterIP   10.233.38.16    <none>        6969/TCP,5005/TCP                              3d18h
sdnc                                    NodePort    10.233.21.214   <none>        8282:30267/TCP,8182:31984/TCP                  3d18h
sdnc-ansible-server                     ClusterIP   10.233.5.45     <none>        8000/TCP                                       3d18h
sdnc-callhome                           NodePort    10.233.48.115   <none>        4334:30266/TCP                                 3d18h
sdnc-dgbuilder                          NodePort    10.233.56.128   <none>        3100:30203/TCP                                 3d18h
sdnc-dmaap-listener                     ClusterIP   10.233.61.37    <none>        80/TCP                                         3d18h
sdnc-oam                                ClusterIP   10.233.28.44    <none>        8282/TCP,8202/TCP                              3d18h
sdnc-web                                NodePort    10.233.30.203   <none>        8080:30205/TCP                                 3d18h
sdnrdb                                  ClusterIP   10.233.57.197   <none>        9200/TCP                                       3d18h
sdnrdb-discovery                        ClusterIP   None            <none>        9300/TCP                                       3d18h
sdnrdb-service                          ClusterIP   10.233.29.188   <none>        9300/TCP                                       3d18h
```

### Check Deployment
```bash
kubectl get deployment -n onap
```
output:
```bash

root@node1:~# kubectl get deployment -n onap
NAME                               READY   UP-TO-DATE   AVAILABLE   AGE
onap-dcae-ves-collector            1/1     1            1           3d18h
onap-network-name-gen              1/1     1            1           3d18h
onap-policy-apex-pdp               1/1     1            1           3d18h
onap-policy-api                    1/1     1            1           3d18h
onap-policy-clamp-ac-a1pms-ppnt    1/1     1            1           3d18h
onap-policy-clamp-ac-http-ppnt     1/1     1            1           3d18h
onap-policy-clamp-ac-k8s-ppnt      1/1     1            1           3d18h
onap-policy-clamp-ac-kserve-ppnt   1/1     1            1           3d18h
onap-policy-clamp-ac-pf-ppnt       1/1     1            1           3d18h
onap-policy-clamp-runtime-acm      1/1     1            1           3d18h
onap-policy-pap                    1/1     1            1           3d18h
onap-sdnc-ansible-server           1/1     1            1           3d18h
onap-sdnc-dgbuilder                1/1     1            1           3d18h
onap-sdnc-dmaap-listener           1/1     1            1           3d18h
onap-sdnc-web                      1/1     1            1           3d18h
onap-sdnrdb-coordinating-only      1/1     1            1           3d18h
onap-strimzi-entity-operator       1/1     1            1           3d18h
```
### Restart Deployment
```bash
kubectl rollout restart deployment onap-dcae-ves-collector -n onap
```

## Linux
### Query whether the target port is enabled
```bash
nmap -p 1883 192.168.135.102
nmap -Pn 1883 192.168.135.102
```
**note: Greigns company has configured the DU O1 IP as `192.168.135.102`**
output:
```bash
root@node1:~# nmap -p 1883 192.168.135.102
Starting Nmap 7.80 ( https://nmap.org ) at 2024-07-15 03:40 UTC
Note: Host seems down. If it is really up, but blocking our ping probes, try -Pn
Nmap done: 1 IP address (0 hosts up) scanned in 3.15 seconds

root@node1:~# nmap -Pn 1883 192.168.135.102
Starting Nmap 7.80 ( https://nmap.org ) at 2024-07-15 03:41 UTC
Nmap scan report for 1883 (0.0.7.91)
Host is up.
All 1000 scanned ports on 1883 (0.0.7.91) are filtered

Nmap scan report for 192.168.135.102
Host is up (0.0021s latency).
Not shown: 994 filtered ports
PORT    STATE  SERVICE
21/tcp  open   ftp
53/tcp  open   domain
80/tcp  open   http
110/tcp open   pop3
113/tcp closed ident
143/tcp open   imap

Nmap done: 2 IP addresses (2 hosts up) scanned in 6.74 seconds
```

## Platform access points
### SDNR WEB
```bash
http://192.168.0.237:30205/odlux/index.html
```
username: admin
password: Kp8bJ4SXszM0WXlhak3eHlcse2gAw84vaoGGmJvUy2U
![image](https://hackmd.io/_uploads/rygNizfdA.png)

### NONRTRIC Dashboard
```bash
http://192.168.0.237:30091/
```

![image](https://hackmd.io/_uploads/BJdFizMuC.png)

### InfluxDB
```bash
http://192.168.0.237:30001
```
username: admin
password: 
```bash
kubectl get secret -n o1ves o1ves-influxdb2-auth -o json
echo enVqWmJqNDRheGdrdVRzWEkyOTJQQU1uQkYxNTNMWng= | base64 -d
```
![image](https://hackmd.io/_uploads/BkYlTzGdA.png)

### Grafana
```bash
http://192.168.0.237:30000
```
username: admin
password: smo
![image](https://hackmd.io/_uploads/rkus2fzu0.png)

## o1ves Configuration
### Requires module installation
```bash
sudo apt-get install ipmitool
pip3 install influxdb-client
pip3 install pysnmp
pip3 install paho-mqtt
```

### Specification Files
references:
* https://docs.onap.org/projects/onap-vnfrqts-requirements/en/latest/Chapter8/ves7_1spec.html#common-event-format
* https://docs.onap.org/projects/onap-dcaegen2/en/montreal/sections/apis/ves.html

#### Use the current version of each Fields (required parameters)
![image](https://hackmd.io/_uploads/rJBdlVM_R.png)

#### Events you can choose to use
* commonEventHeader is a necessary event (red box)
* FaultFields and measurementFields are the events selected this time (green box)

![image](https://hackmd.io/_uploads/HJMPNrzdA.png)

#### measurementFields
Data structure:
* measurementInterval (required parameter)
* measurementFieldsVersion (required parameter)

```bash
{
    "event": {
        "commonEventHeader": {
            "domain": "@domain@",
            "eventId": "@eventId@",
            "eventName": "@domain@_@eventType@_@granularity@",
            "eventType": "@eventType@_@granularity@",
            "sequence": 0,
            "priority": "Low",
            "reportingEntityId": "",
            "reportingEntityName": "@controllerName@",
            "sourceId": "",
            "sourceName": "@pnfId@",
            "startEpochMicrosec": "@collectionStartTime@",
            "lastEpochMicrosec": "@collectionEndTime@",
            "internalHeaderFields": {
                "intervalStartTime": "@intervalStartTime@",
                "intervalEndTime": "@intervalEndTime@"
            },
            "version": "4.1",
            "vesEventListenerVersion": "7.2.1"
        },
        "measurementFields": {
            "additionalFields": {},
            "additionalMeasurements": [{
                    "name": "@interface@-1",
                    "hashMap": {
                        "es": "0",
                        "ses": "1",
                        "cses": "0",
                        "unavailability": "0"
                    }
                },
                {
                    "name": "@interface@-2",
                    "hashMap": {
                        "es": "0",
                        "ses": "1",
                        "cses": "0",
                        "unavailability": "0"
                    }
                }
            ],
            "additionalObjects": [],
            "codecUsageArray": [],
            "concurrentSessions": 2,
            "configuredEntities": 2,
            "cpuUsageArray": [],
            "diskUsageArray": [],
            "featureUsageArray": {
                "https://www.itu.int/rec/T-REC-G.841": "true"
            },
            "filesystemUsageArray": [],
            "hugePagesArray": [],
            "ipmi": {},
            "latencyDistribution": [],
            "loadArray": [],
            "machineCheckExceptionArray": [],
            "meanRequestLatency": 1000,
            "measurementInterval": 234,
            "measurementFieldsVersion": "4.0",
            "memoryUsageArray": [],
            "numberOfMediaPortsInUse": 234,
            "requestRate": 23,
            "nfcScalingMetric": 3,
            "nicPerformanceArray": [],
            "processStatsArray": []
        }
    }
}
```

#### FaultFields
Data structure:
* faultFieldsVersion (required parameter)
* eventSeverity (required parameters):
* Event severity enumeration: CRITICAL, MAJOR, MINOR, WARNING, NORMAL.
* eventSourceType (required parameters)
* alarmCondition (required parameter)
* specificProblem (required parameters)
* vfStatus (required parameter)

```bash
{
    "event": {
        "commonEventHeader": {
            "domain": "@domain@",
            "eventId": "@eventId@",
            "eventName": "@domain@_@eventType@_Alarms_@alarm@",
            "eventType": "@eventType@_Alarms",
            "sequence": 0,
            "priority": "High",
            "reportingEntityId": "",
            "reportingEntityName": "@controllerName@",
            "sourceId": "",
            "sourceName": "@pnfId@",
            "startEpochMicrosec": "@timestamp@",
            "lastEpochMicrosec": "@timestamp@",
            "nfNamingCode": "@type@",
            "nfVendorName": "@vendor@",
            "timeZoneOffset": "+00:00",
            "version": "4.1",
            "vesEventListenerVersion": "7.2.1"
        },
        "faultFields": {
            "faultFieldsVersion": "4.0",
            "alarmCondition": "@alarm@",
            "alarmInterfaceA": "@interface@",
            "eventSourceType": "@eventType@",
            "specificProblem": "@alarm@",
            "eventSeverity": "@severity@",
            "vfStatus": "Active",
            "alarmAdditionalInformation": {
                "eventTime": "@eventTime@",
                "equipType": "@type@",
                "vendor": "@vendor@",
                "model": "@model@"
            }
        }
    }
}
```

#### otherFields
data structure
* otherFields (required parameters)
```bash
curl -i -k -u sample1:sample1 -X POST -d '{
  "event": {
    "commonEventHeader": {
      "domain": "heartbeat",
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
          "name": "total",
          "hashMap": {
            "num_of_ue": "1",
            "total_ul_tp": "12321312.23",
            "total_ul_pkt":"123",
            "total_dl_tp":"123.45",
            "total_dl_pkt":"23"
          }
        },
        {
          "name": "personal",
          "hashMap": {
            "ue_id":"0",
            "ul_tp":"3432423",
            "ul_pkt":"234324",
            "dl_tp":"12312",
            "dl_pkt":"213213"
          }
        }
      ]
    }
  }
}' --header "Content-Type: application/json" http://192.168.0.237:30417/eventListener/v7
```

### PM Rules
Currently PM `value.yaml` can receive CU and DU information.
bucket : `o1_performance`
measurement: `ran1_gNB_DU_PM`, `ran1_gNB_CU_PM`
matches(filter rules):
ran1_gNB_DU_PM:
ran_id : ran1
src_id : gNB_DU
ran1_gNB_CU_PM:
ran_id : ran1
src_id : gNB_CU

rules code (`values.yaml`):
```yaml=
dmaap-influxdb-adapter:
  enabled: true
  image:
    repository: harbor.winfra.cs.nycu.edu.tw/winlab-oran/dmaap-influxdb-adapter
  influxdb:
    host: o1ves-influxdb2
    port: 80
    tokenSecret: o1ves-influxdb2-auth
    org: influxdata
  logLevel: DEBUG

  rules:
    - topic: unauthenticated.VES_MEASUREMENT_OUTPUT
      rules:
        - bucket: o1_performance
          measurement: ran1_gNB_DU_PM
          matches:
            - key: event.measurementFields.additionalFields.ran_id
              value: ran1
            - key: event.measurementFields.additionalFields.src_id
              value: gNB_DU
          tags:
            - key: name
              field: event.measurementFields.additionalMeasurements[0].name
          fields:
            - key: "RRU.PrbTotDl"
              field: event.measurementFields.additionalMeasurements[0].hashMap."RRU.PrbTotDl"
              type: int
            - key: "RRU.PrbAvailDl"
              field: event.measurementFields.additionalMeasurements[0].hashMap."RRU.PrbAvailDl"
              type: int
            - key: "RRU.PrbTotUl"
              field: event.measurementFields.additionalMeasurements[0].hashMap."RRU.PrbTotUl"
              type: int
            - key: "RRU.PrbAvailUl"
              field: event.measurementFields.additionalMeasurements[0].hashMap."RRU.PrbAvailUl"
              type: int
            - key: "RRU.PrbTotDlDist.BinBelow50Percentage"
              field: event.measurementFields.additionalMeasurements[0].hashMap."RRU.PrbTotDlDist.BinBelow50Percentage"
              type: int
            - key: "RRU.PrbTotDlDist.Bin50To60Percentage"
              field: event.measurementFields.additionalMeasurements[0].hashMap."RRU.PrbTotDlDist.Bin50To60Percentage"
              type: int
            - key: "RRU.PrbTotDlDist.Bin61To70Percentage"
              field: event.measurementFields.additionalMeasurements[0].hashMap."RRU.PrbTotDlDist.Bin61To70Percentage"
              type: int
            - key: "RRU.PrbTotDlDist.Bin71To80Percentage"
              field: event.measurementFields.additionalMeasurements[0].hashMap."RRU.PrbTotDlDist.Bin71To80Percentage"
              type: int
            - key: "RRU.PrbTotDlDist.Bin81To85Percentage"
              field: event.measurementFields.additionalMeasurements[0].hashMap."RRU.PrbTotDlDist.Bin81To85Percentage"
              type: int
            - key: "RRU.PrbTotDlDist.Bin86To90Percentage"
              field: event.measurementFields.additionalMeasurements[0].hashMap."RRU.PrbTotDlDist.Bin86To90Percentage"
              type: int
            - key: "RRU.PrbTotDlDist.Bin91To93Percentage"
              field: event.measurementFields.additionalMeasurements[0].hashMap."RRU.PrbTotDlDist.Bin91To93Percentage"
              type: int
            - key: "RRU.PrbTotDlDist.Bin94To96Percentage"
              field: event.measurementFields.additionalMeasurements[0].hashMap."RRU.PrbTotDlDist.Bin94To96Percentage"
              type: int
            - key: "RRU.PrbTotDlDist.Bin97To98Percentage"
              field: event.measurementFields.additionalMeasurements[0].hashMap."RRU.PrbTotDlDist.Bin97To98Percentage"
              type: int
            - key: "RRU.PrbTotDlDist.BinAbove98Percentage"
              field: event.measurementFields.additionalMeasurements[0].hashMap."RRU.PrbTotDlDist.BinAbove98Percentage"
              type: int
            - key: "RRU.PrbTotUlDist.BinBelow50Percentage"
              field: event.measurementFields.additionalMeasurements[0].hashMap."RRU.PrbTotUlDist.BinBelow50Percentage"
              type: int
            - key: "RRU.PrbTotUlDist.Bin50To60Percentage"
              field: event.measurementFields.additionalMeasurements[0].hashMap."RRU.PrbTotUlDist.Bin50To60Percentage"
              type: int
            - key: "RRU.PrbTotUlDist.Bin61To70Percentage"
              field: event.measurementFields.additionalMeasurements[0].hashMap."RRU.PrbTotUlDist.Bin61To70Percentage"
              type: int
            - key: "RRU.PrbTotUlDist.Bin71To80Percentage"
              field: event.measurementFields.additionalMeasurements[0].hashMap."RRU.PrbTotUlDist.Bin71To80Percentage"
              type: int
            - key: "RRU.PrbTotUlDist.Bin81To85Percentage"
              field: event.measurementFields.additionalMeasurements[0].hashMap."RRU.PrbTotUlDist.Bin81To85Percentage"
              type: int
            - key: "RRU.PrbTotUlDist.Bin86To90Percentage"
              field: event.measurementFields.additionalMeasurements[0].hashMap."RRU.PrbTotUlDist.Bin86To90Percentage"
              type: int
            - key: "RRU.PrbTotUlDist.Bin91To93Percentage"
              field: event.measurementFields.additionalMeasurements[0].hashMap."RRU.PrbTotUlDist.Bin91To93Percentage"
              type: int
            - key: "RRU.PrbTotUlDist.Bin94To96Percentage"
              field: event.measurementFields.additionalMeasurements[0].hashMap."RRU.PrbTotUlDist.Bin94To96Percentage"
              type: int
            - key: "RRU.PrbTotUlDist.Bin97To98Percentage"
              field: event.measurementFields.additionalMeasurements[0].hashMap."RRU.PrbTotUlDist.Bin97To98Percentage"
              type: int
            - key: "RRU.PrbTotUlDist.BinAbove98Percentage"
              field: event.measurementFields.additionalMeasurements[0].hashMap."RRU.PrbTotUlDist.BinAbove98Percentage"
              type: int
            - key: "L1M.PHR1.BinLessThanMinus32dBm"
              field: event.measurementFields.additionalMeasurements[0].hashMap."L1M.PHR1.BinLessThanMinus32dBm"
              type: int
            - key: "L1M.PHR1.BinMinus32ToMinus26dBm"
              field: event.measurementFields.additionalMeasurements[0].hashMap."L1M.PHR1.BinMinus32ToMinus26dBm"
              type: int
            - key: "L1M.PHR1.BinMinus25ToMinus19dBm"
              field: event.measurementFields.additionalMeasurements[0].hashMap."L1M.PHR1.BinMinus25ToMinus19dBm"
              type: int
            - key: "L1M.PHR1.BinMinus18ToMinus12dBm"
              field: event.measurementFields.additionalMeasurements[0].hashMap."L1M.PHR1.BinMinus18ToMinus12dBm"
              type: int
            - key: "L1M.PHR1.BinMinus11ToMinus5dBm"
              field: event.measurementFields.additionalMeasurements[0].hashMap."L1M.PHR1.BinMinus11ToMinus5dBm"
              type: int
            - key: "L1M.PHR1.BinMinus4To2dBm"
              field: event.measurementFields.additionalMeasurements[0].hashMap."L1M.PHR1.BinMinus4To2dBm"
              type: int
            - key: "L1M.PHR1.Bin3To9dBm"
              field: event.measurementFields.additionalMeasurements[0].hashMap."L1M.PHR1.Bin3To9dBm"
              type: int
            - key: "L1M.PHR1.Bin10To16dBm"
              field: event.measurementFields.additionalMeasurements[0].hashMap."L1M.PHR1.Bin10To16dBm"
              type: int
            - key: "L1M.PHR1.Bin17To23dBm"
              field: event.measurementFields.additionalMeasurements[0].hashMap."L1M.PHR1.Bin17To23dBm"
              type: int
            - key: "L1M.PHR1.Bin24To31dBm"
              field: event.measurementFields.additionalMeasurements[0].hashMap."L1M.PHR1.Bin24To31dBm"
              type: int
            - key: "L1M.PHR1.Bin32To37dBm"
              field: event.measurementFields.additionalMeasurements[0].hashMap."L1M.PHR1.Bin32To37dBm"
              type: int
            - key: "L1M.PHR1.BinGreaterThan38"
              field: event.measurementFields.additionalMeasurements[0].hashMap."L1M.PHR1.BinGreaterThan38"
              type: int
            - key: "RACH.PreambleDedCell"
              field: event.measurementFields.additionalMeasurements[0].hashMap."RACH.PreambleDedCell"
              type: int
            - key: "RACH.PreambleACell"
              field: event.measurementFields.additionalMeasurements[0].hashMap."RACH.PreambleACell"
              type: int
            - key: "RACH.PreambleBCell"
              field: event.measurementFields.additionalMeasurements[0].hashMap."RACH.PreambleBCell"
              type: int
            - key: "RACH.PreambleDed.0"
              field: event.measurementFields.additionalMeasurements[0].hashMap."RACH.PreambleDed.0"
              type: int
            - key: "RACH.PreambleA.0"
              field: event.measurementFields.additionalMeasurements[0].hashMap."RACH.PreambleA.0"
              type: int
            - key: "RACH.PreambleB.0"
              field: event.measurementFields.additionalMeasurements[0].hashMap."RACH.PreambleB.0"
              type: int
        - bucket: o1_performance
          measurement: ran1_gNB_CU_PM
          matches:
            - key: event.measurementFields.additionalFields.ran_id
              value: ran1
            - key: event.measurementFields.additionalFields.src_id
              value: gNB_CU
          tags:
            - key: name
              field: event.measurementFields.additionalMeasurements[0].name
          fields:
            - key: "PAG.ReceivedNbrCnInitiated"
              field: event.measurementFields.additionalMeasurements[0].hashMap."PAG.ReceivedNbrCnInitiated"
              type: int
            - key: "PAG.DiscardedNbrCnInitiated"
              field: event.measurementFields.additionalMeasurements[0].hashMap."PAG.DiscardedNbrCnInitiated"
              type: int
            - key: "MM.HoPrepInterReq"
              field: event.measurementFields.additionalMeasurements[0].hashMap."MM.HoPrepInterReq"
              type: int
            - key: "MM.HoResAlloInterReq"
              field: event.measurementFields.additionalMeasurements[0].hashMap."MM.HoResAlloInterReq"
              type: int
            - key: "MM.HoExeInterReq"
              field: event.measurementFields.additionalMeasurements[0].hashMap."MM.HoExeInterReq"
              type: int
            - key: "MM.HoPrepInterSucc"
              field: event.measurementFields.additionalMeasurements[0].hashMap."MM.HoPrepInterSucc"
              type: int
            - key: "MM.HoResAlloInterSucc"
              field: event.measurementFields.additionalMeasurements[0].hashMap."MM.HoResAlloInterSucc"
              type: int
            - key: "MM.HoExeInterSucc"
              field: event.measurementFields.additionalMeasurements[0].hashMap."MM.HoExeInterSucc"
              type: int
            - key: "MM.HoPrepInterFail"
              field: event.measurementFields.additionalMeasurements[0].hashMap."MM.HoPrepInterFail"
              type: int
            - key: "MM.HoResAlloInterFail"
              field: event.measurementFields.additionalMeasurements[0].hashMap."MM.HoResAlloInterFail"
              type: int
            - key: "MM.MM.HoExeInterFail.UeCtxtRelCmd.cause"
              field: event.measurementFields.additionalMeasurements[0].hashMap."MM.MM.HoExeInterFail.UeCtxtRelCmd.cause"
              type: int
            - key: "MM.HoPrepIntraReq"
              field: event.measurementFields.additionalMeasurements[0].hashMap."MM.HoPrepIntraReq"
              type: int
            - key: "MM.HoExeIntraReq"
              field: event.measurementFields.additionalMeasurements[0].hashMap."MM.HoExeIntraReq"
              type: int
            - key: "MM.HoPrepIntraSucc"
              field: event.measurementFields.additionalMeasurements[0].hashMap."MM.HoPrepIntraSucc"
              type: int
            - key: "MM.HoExeIntraSucc"
              field: event.measurementFields.additionalMeasurements[0].hashMap."MM.HoExeIntraSucc"
              type: int
            - key: "RRC.ConnMean"
              field: event.measurementFields.additionalMeasurements[0].hashMap."RRC.ConnMean"
              type: int
            - key: "RRC.ConnMax"
              field: event.measurementFields.additionalMeasurements[0].hashMap."RRC.ConnMax"
              type: int
            - key: "RRC.ConnEstabAtt"
              field: event.measurementFields.additionalMeasurements[0].hashMap."RRC.ConnEstabAtt"
              type: int
            - key: "RRC.ConnEstabSucc"
              field: event.measurementFields.additionalMeasurements[0].hashMap."RRC.ConnEstabSucc"
              type: int
            - key: "RRC.ReEstabAtt"
              field: event.measurementFields.additionalMeasurements[0].hashMap."RRC.ReEstabAtt"
              type: int
            - key: "PAG.SuccessRatio"
              field: event.measurementFields.additionalMeasurements[0].hashMap."PAG.SuccessRatio"
              type: int
            - key: "RRC.ReEstabSuccWithoutUeContext"
              field: event.measurementFields.additionalMeasurements[0].hashMap."RRC.ReEstabSuccWithoutUeContext"
              type: int
            - key: "QosFlow.PdcpPduVolumeDl"
              field: event.measurementFields.additionalMeasurements[0].hashMap."QosFlow.PdcpPduVolumeDl"
              type: int
            - key: "QosFlow.PdcpPduVolumeUl"
              field: event.measurementFields.additionalMeasurements[0].hashMap."QosFlow.PdcpPduVolumeUl"
              type: int
            - key: "Sys.DataVolumeDL"
              field: event.measurementFields.additionalMeasurements[0].hashMap."Sys.DataVolumeDL"
              type: int
            - key: "Sys.DataVolumeUL"
              field: event.measurementFields.additionalMeasurements[0].hashMap."Sys.DataVolumeUL"
              type: int
            - key: "Sys.SpecEffDL"
              field: event.measurementFields.additionalMeasurements[0].hashMap."Sys.SpecEffDL"
              type: float
            - key: "Sys.SpecEffUL"
              field: event.measurementFields.additionalMeasurements[0].hashMap."Sys.SpecEffUL"
              type: float
            - key: "Sys.CellAvail"
              field: event.measurementFields.additionalMeasurements[0].hashMap."Sys.CellAvail"
              type: int
        - bucket: o1_performance
          measurement: BBU_instantaneous_power
          matches:
            - key: event.measurementFields.additionalFields.ran_id
              value: ran1
            - key: event.measurementFields.additionalFields.src_id
              value: BBU
          tags:
            - key: name
              value: event.measurementFields.additionalMeasurements[0].name
          fields:
            - key: "instantaneous_power"
              field: event.measurementFields.additionalMeasurements[0].hashMap."instantaneous_power"
              type: float
buckets:
  - name: o1_performance
```

proxy forward PM program code in python:
```python=
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
                    "ran_id": mqtt_data["ran_id"],
                    "src_id": mqtt_data["src_id"]
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
```

### FM rules
The new FM rule is that `value.yaml` currently sending fake packets can be received.
* bucket : o1_fault_event
* measurement : BBU_FM_Event
* matches(filter rules):
* domain : fault

rules code (`values.yaml`):
```yaml=
    - topic: unauthenticated.SEC_FAULT_OUTPUT
      rules:
        - bucket: o1_fault_event
          measurement: BBU_FM_Event
          matches:
            - key: event.commonEventHeader.domain
              value: fault
          tags:
            - key: eventType
              field: event.commonEventHeader.eventType
          fields:
            - key: eventName
              field: event.commonEventHeader.eventName
              type: string
            - key: sourceName
              field: event.commonEventHeader.sourceName
              type: string
            - key: nfVendorName
              field: event.commonEventHeader.nfVendorName
              type: string
            - key: eventSeverity
              field: event.faultFields.eventSeverity
              type: string
            - key: specificProblem
              field: event.faultFields.specificProblem
              type: string
```

proxy forward FM program code:
```python=
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
```

### otherFields rules
The new PDCP Throughput rules are in value.yaml. Currently, fake packets sent can be received.
* bucket : PDCP_Throughput
* measurement : ue_info、ue_sum_info、BBU_Info
* matches(filter rules):
    * ue_info :
        * domain : other
        * name : personal
    * ue_sum_info :
        * domain : other
        * name : total
    * BBU_Info: Although ran1 and ran2 were received at one time, they were sent to influxDB in two separate transactions.
        * domain : other
        * name : ran1、ran2

rules code (`values.yaml`):
```yaml=
    - topic: unauthenticated.SEC_OTHER_OUTPUT
      rules:
        - bucket: PDCP_Throughput
          measurement: ue_sum_info
          matches:
            - key: event.commonEventHeader.domain
              value: other
            - key: event.otherFields.arrayOfNamedHashMap[0].name
              value: total
          tags:
            - key: name
              field: event.otherFields.arrayOfNamedHashMap[0].name
          fields:
            - key: num_of_ue
              field: event.otherFields.arrayOfNamedHashMap[0].hashMap.num_of_ue
              type: int
            - key: total_ul_tp
              field: event.otherFields.arrayOfNamedHashMap[0].hashMap.total_ul_tp
              type: float
            - key: total_ul_pkt
              field: event.otherFields.arrayOfNamedHashMap[0].hashMap.total_ul_pkt
              type: int
            - key: total_dl_tp
              field: event.otherFields.arrayOfNamedHashMap[0].hashMap.total_dl_tp
              type: float
            - key: total_dl_pkt
              field: event.otherFields.arrayOfNamedHashMap[0].hashMap.total_dl_pkt
              type: int
        - bucket: PDCP_Throughput
          measurement: ue_info
          matches:
            - key: event.commonEventHeader.domain
              value: other
            - key: event.otherFields.arrayOfNamedHashMap[0].name
              value: personal
          tags:
            - key: name
              field: event.otherFields.arrayOfNamedHashMap[0].name
          fields:
            - key: ue_id
              field: event.otherFields.arrayOfNamedHashMap[0].hashMap.ue_id
              type: int
            - key: ul_tp
              field: event.otherFields.arrayOfNamedHashMap[0].hashMap.ul_tp
              type: float
            - key: ul_pkt
              field: event.otherFields.arrayOfNamedHashMap[0].hashMap.ul_pkt
              type: int
            - key: dl_tp
              field: event.otherFields.arrayOfNamedHashMap[0].hashMap.dl_tp
              type: float
            - key: dl_pkt
              field: event.otherFields.arrayOfNamedHashMap[0].hashMap.dl_pkt
              type: int
        - bucket: BBU_Info
          measurement: BBU_Info
          matches:
            - key: event.commonEventHeader.domain
              value: other
            - key: event.otherFields.arrayOfNamedHashMap[0].name
              value: ran1
          tags:
            - key: name
              field: event.otherFields.arrayOfNamedHashMap[0].name
          fields:
            - key: PLMNID
              field: event.otherFields.arrayOfNamedHashMap[0].hashMap.PLMNID
              type: string
            - key: BBU_IP
              field: event.otherFields.arrayOfNamedHashMap[0].hashMap.BBU_IP
              type: string
            - key: BBU_NETMASK
              field: event.otherFields.arrayOfNamedHashMap[0].hashMap.BBU_NETMASK
              type: string
            - key: BBU_Gateway_IP
              field: event.otherFields.arrayOfNamedHashMap[0].hashMap.BBU_Gateway_IP
              type: string
            - key: AMF_IP
              field: event.otherFields.arrayOfNamedHashMap[0].hashMap.AMF_IP
              type: string
            - key: gNB_ID
              field: event.otherFields.arrayOfNamedHashMap[0].hashMap.gNB_ID
              type: string
        - bucket: BBU_Info
          measurement: BBU_Info
          matches:
            - key: event.commonEventHeader.domain
              value: other
            - key: event.otherFields.arrayOfNamedHashMap[0].name
              value: ran2
          tags:
            - key: name
              field: event.otherFields.arrayOfNamedHashMap[0].name
          fields:
            - key: PLMNID
              field: event.otherFields.arrayOfNamedHashMap[0].hashMap.PLMNID
              type: string
            - key: BBU_IP
              field: event.otherFields.arrayOfNamedHashMap[0].hashMap.BBU_IP
              type: string
            - key: BBU_NETMASK
              field: event.otherFields.arrayOfNamedHashMap[0].hashMap.BBU_NETMASK
              type: string
            - key: BBU_Gateway_IP
              field: event.otherFields.arrayOfNamedHashMap[0].hashMap.BBU_Gateway_IP
              type: string
            - key: AMF_IP
              field: event.otherFields.arrayOfNamedHashMap[0].hashMap.AMF_IP
              type: string
            - key: gNB_ID
              field: event.otherFields.arrayOfNamedHashMap[0].hashMap.gNB_ID
              type: string
```
proxy forwarding PDUP Throughput code in python:
```python=
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

```
proxy forward Netconf BBU Info code in python:
```python=
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
```

### influxdb-client-python
reference: https://github.com/influxdata/influxdb-client-python

First confirm whether grafana can be displayed after influxdb receives the data.
Because the influxdb of k8s is version 1.8 or above, you need to install influxdb-client to connect to influxdb.
Program code:
* config:
    * host IP
    * influxdb port
    * bucket
    * username
    * password
    * token
    * 
`influxdb_example.py`:
```python=
from influxdb_client import InfluxDBClient, Point
from influxdb_client.client.write_api import SYNCHRONOUS
from datetime import datetime

# InfluxDB connection configuration
host = '192.168.0.237'  # InfluxDB hostname or IP address
port = 30001         # InfluxDB port number
database = 'smo' # InfluxDB database name
username = 'admin'  # InfluxDB username
password = 'lun6ty62sIJekDKEswGRJH9L8SX95jsD'  # InfluxDB password

# Create InfluxDB client object
client = InfluxDBClient(url=f"http://{host}:{port}", token="aTFoTDFkT3RaaVI1RldBQUNES2dpQXpuRWpucXlISVQ", org="influxdata")
write_api = client.write_api(write_options=SYNCHRONOUS)

# Create sample data
measurement = 'example_measurement'
tags = {'tag1': 'value1', 'tag2': 'value2'}
fields = {'field1': 123, 'field2': 3.14}
time = datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ')

# Create data point
data = [
    {
        "measurement": measurement,
        "tags": tags,
        "fields": fields,
        "time": time
    }
]

# Write data to InfluxDB
write_api.write(bucket=database, record=data)
print("Data sent to InfluxDB successfully.")
```
result:
There is data displayed in influxDB. Grafana is not displayed and configuration needs to be set.
```bash
root@node1:~# python3 influxdb_example.py
Data sent to InfluxDB successfully.
```
![image](https://hackmd.io/_uploads/S1sVzTG_A.png)

### Grafana
references:
* https://hackmd.io/@KenLiang/grafana-tutorials
* https://docs.influxdata.com/influxdb/v2/query-data/get-started/query-influxdb/

**instruction**
Flux uses `|>` instructions to continue, and `yield()` the output results need to be added at the end.
1. Instruction Bucket
```bash
from(bucket:"example-bucket")
```
2. Specify Time Range
* Relatively
```bash
from(bucket:"example-bucket")        // Display data from the past 1 hour
    |> range(start: -1h)

from(bucket:"example-bucket")         // Display data from 1 hour ago to 10 minutes ago
    |> range(start: -1h, stop: -10m)
```
* Absolutely
```bash
from(bucket:"example-bucket")
    |> range(start: 2021-01-01T00:00:00Z, stop: 2021-01-01T12:00:00Z)
```

Filter Data
filter(): iterates each row of data into FLUX records, and each record is passed to the next.
The calculation result is false -> the data deletion
calculation result is true -> retain the output data
**filter only retains rows that meet the conditions, and deletes those that do not meet the conditions.**
```bash
from(bucket: "example-bucket")
    |> range(start: -15m)
    |> filter(fn: (r) => r._measurement == "cpu" and r._field == "usage_system" and r.cpu == "cpu-total")
```
sample code:
```bash
Query A :
from(bucket: "smo")
  |> range(start: -30m)
  |> filter(fn: (r) =>
    r._measurement == "example_measurement" and
    r._field == "field1"
  )
  |>yield()
#########################################################################  
Query B :
from(bucket: "smo")
  |> range(start: -30m)
  |> filter(fn: (r) =>
    r._measurement == "example_measurement" and
    r._field == "field2"
  )
  |>yield()
```
result:


## Test Results
### ves collector Receive BBU PM
**gNB_DU_PM curl test code:**
```bash
curl -i -k -u sample1:sample1 -X POST -d '{
    "event": {
        "commonEventHeader": {
            "domain": "measurement",
            "eventId": "greigns_1713425400_PM15min",
            "eventName": "measurement_O_RAN_COMPONENT_PM15min",
            "eventType": "O_RAN_COMPONENT_PM15min",
            "sequence": 0,
            "priority": "Low",
            "reportingEntityId": "",
            "reportingEntityName": "node1.cluster.local",
            "sourceId": "",
            "sourceName": "greigns",
            "startEpochMicrosec": 1713424500000000,
            "lastEpochMicrosec": 1713425400000000,
            "internalHeaderFields": {
                "intervalStartTime": "Thu, 18 Apr 2024 07:15:00 +0000",
                "intervalEndTime": "Thu, 18 Apr 2024 07:30:00 +0000"
            },
            "version": "4.1",
            "vesEventListenerVersion": "7.2.1"
        },
        "measurementFields": {
            "additionalFields": {
                "ran_id": "ran1",
                "src_id": "gNB_DU"
            },
            "additionalMeasurements": [
                {
                    "name": "pm_data",
                    "hashMap": {
 "PAG.ReceivedNbrCnInitiated": "0",
        "RRU.PrbTotDl": "0",
        "RRU.PrbAvailDl": "132",
        "RRU.PrbTotUl": "1",
        "RRU.PrbAvailUl": "78",
        "RRU.PrbTotDlDist.BinBelow50Percentage": "1",
        "RRU.PrbTotDlDist.Bin50To60Percentage": "0",
        "RRU.PrbTotDlDist.Bin61To70Percentage": "0",
        "RRU.PrbTotDlDist.Bin71To80Percentage": "0",
        "RRU.PrbTotDlDist.Bin81To85Percentage": "0",
        "RRU.PrbTotDlDist.Bin86To90Percentage": "0",
        "RRU.PrbTotDlDist.Bin91To93Percentage": "0",
        "RRU.PrbTotDlDist.Bin94To96Percentage": "0",
        "RRU.PrbTotDlDist.Bin97To98Percentage": "0",
        "RRU.PrbTotDlDist.BinAbove98Percentage": "0",
        "RRU.PrbTotUlDist.BinBelow50Percentage": "1",
        "RRU.PrbTotUlDist.Bin50To60Percentage": "0",
        "RRU.PrbTotUlDist.Bin61To70Percentage": "0",
        "RRU.PrbTotUlDist.Bin71To80Percentage": "0",
        "RRU.PrbTotUlDist.Bin81To85Percentage": "0",
        "RRU.PrbTotUlDist.Bin86To90Percentage": "0",
        "RRU.PrbTotUlDist.Bin91To93Percentage": "0",
        "RRU.PrbTotUlDist.Bin94To96Percentage": "0",
        "RRU.PrbTotUlDist.Bin97To98Percentage": "0",
        "RRU.PrbTotUlDist.BinAbove98Percentage": "0",
        "L1M.PHR1.BinLessThanMinus32dBm": "0",
        "L1M.PHR1.BinMinus32ToMinus26dBm": "0",
        "L1M.PHR1.BinMinus25ToMinus19dBm": "0",
        "L1M.PHR1.BinMinus18ToMinus12dBm": "0",
        "L1M.PHR1.BinMinus11ToMinus5dBm": "0",
        "L1M.PHR1.BinMinus4To2dBm": "0",
        "L1M.PHR1.Bin3To9dBm": "0",
        "L1M.PHR1.Bin10To16dBm": "0",
        "L1M.PHR1.Bin17To23dBm": "0",
        "L1M.PHR1.Bin24To31dBm": "0",
        "L1M.PHR1.Bin32To37dBm": "0",
        "L1M.PHR1.BinGreaterThan38": "0",
        "RACH.PreambleDedCell": "0",
        "RACH.PreambleACell": "0",
        "RACH.PreambleBCell": "0",
        "RACH.PreambleDed.0": "0",
        "RACH.PreambleA.0": "0",
        "RACH.PreambleB.0": "0"
                    }
                }
            ],
            "measurementInterval": 234,
            "measurementFieldsVersion": "4.0"
        }
    }
}' --header "Content-Type: application/json" http://192.168.0.237:30417/eventListener/v7
```
output:
```bash
HTTP/1.1 202
Content-Type: application/json
Content-Length: 23
Date: Mon, 15 Jul 2024 15:56:25 GMT

Successfully send event
```

**gNB_CU_PM curl test code:**
```bash
curl -i -k -u sample1:sample1 -X POST -d '{
    "event": {
        "commonEventHeader": {
            "domain": "measurement",
            "eventId": "greigns_1713425400_PM15min",
            "eventName": "measurement_O_RAN_COMPONENT_PM15min",
            "eventType": "O_RAN_COMPONENT_PM15min",
            "sequence": 0,
            "priority": "Low",
            "reportingEntityId": "",
            "reportingEntityName": "node1.cluster.local",
            "sourceId": "",
            "sourceName": "greigns",
            "startEpochMicrosec": 1713424500000000,
            "lastEpochMicrosec": 1713425400000000,
            "internalHeaderFields": {
                "intervalStartTime": "Thu, 18 Apr 2024 07:15:00 +0000",
                "intervalEndTime": "Thu, 18 Apr 2024 07:30:00 +0000"
            },
            "version": "4.1",
            "vesEventListenerVersion": "7.2.1"
        },
        "measurementFields": {
            "additionalFields": {
                "ran_id": "ran1",
                "src_id": "gNB_CU"
            },
            "additionalMeasurements": [
                {
                    "name": "pm_data",
                    "hashMap": {
                        "RRU.PrbTotDl": "0",
 "PAG.ReceivedNbrCnInitiated": "0",
        "PAG.DiscardedNbrCnInitiated": "0",
        "MM.HoPrepInterReq": "0",
        "MM.HoResAlloInterReq": "0",
        "MM.HoExeInterReq": "0",
        "MM.HoPrepInterSucc": "0",
        "MM.HoResAlloInterSucc": "0",
        "MM.HoExeInterSucc": "0",
        "MM.HoPrepInterFail": "0",
        "MM.HoResAlloInterFail": "0",
        "MM.MM.HoExeInterFail.UeCtxtRelCmd.cause": "0",
        "MM.HoPrepIntraReq": "0",
        "MM.HoExeIntraReq": "0",
        "MM.HoPrepIntraSucc": "0",
        "MM.HoExeIntraSucc": "0",
        "RRC.ConnMean": "0",
        "RRC.ConnMax": "0",
        "RRC.ConnEstabAtt": "0",
        "RRC.ConnEstabSucc": "0",
        "RRC.ReEstabAtt": "0",
        "RRC.ReEstabSuccWithUeContext": "0",
        "RRC.ReEstabSuccWithoutUeContext": "0",
        "PAG.SuccessRatio": "0",
        "QosFlow.PdcpPduVolumeDl": "0",
        "QosFlow.PdcpPduVolumeUl": "0",
        "Sys.DataVolumeDL": "0",
        "Sys.DataVolumeUL": "0",
        "Sys.SpecEffDL": "0.0",
        "Sys.SpecEffUL": "0.0",
        "Sys.CellAvail": "100"

                    }
                }
            ],
            "measurementInterval": 234,
            "measurementFieldsVersion": "4.0"
        }
    }
}' --header "Content-Type: application/json" http://192.168.0.237:30417/eventListener/v7
```
output:
```bash
HTTP/1.1 202
Content-Type: application/json
Content-Length: 23
Date: Mon, 15 Jul 2024 15:57:27 GMT

Successfully send event
```

### Kubectl DMAAP Logs
#### proxy forwards gNB_CU_PM successfully result
```bash!
DEBUG:root:Pulling messages from topic unauthenticated.VES_MEASUREMENT_OUTPUT...
DEBUG:root:Pull response: ['{"event":{"commonEventHeader":{"sourceId":"","startEpochMicrosec":1713424500000000,"eventId":"greigns_1713425400_PM15min","reportingEntityId":"","internalHeaderFields":{"collectorTimeStamp":"Tue, 07 16 2024 02:46:52 GMT"},"eventType":"O_RAN_COMPONENT_PM15min","priority":"Low","version":"4.1","reportingEntityName":"node1.cluster.local","sequence":0,"domain":"measurement","lastEpochMicrosec":1713425400000000,"eventName":"measurement_O_RAN_COMPONENT_PM15min","vesEventListenerVersion":"7.2.1","sourceName":"greigns"},"measurementFields":{"measurementInterval":234,"measurementFieldsVersion":"4.0","additionalFields":{"src_id":"gNB_CU","ran_id":"ran1"},"additionalMeasurements":[{"name":"pm_data","hashMap":{"Sys.SpecEffDL":"0.0","RRC.ReEstabSuccWithoutUeContext":"0","MM.HoPrepIntraSucc":"0","MM.HoPrepInterSucc":"0","RRC.ReEstabAtt":"0","Sys.DataVolumeDL":"0","RRC.ReEstabSuccWithUeContext":"0","RRU.PrbTotDl":"0","Sys.CellAvail":"100","MM.HoResAlloInterSucc":"0","QosFlow.PdcpPduVolumeDl":"0","MM.HoExeInterReq":"0","Sys.DataVolumeUL":"0","MM.HoResAlloInterReq":"0","RRC.ConnMax":"0","MM.HoPrepIntraReq":"0","MM.HoExeIntraSucc":"0","MM.HoExeInterSucc":"0","PAG.DiscardedNbrCnInitiated":"0","PAG.SuccessRatio":"0","QosFlow.PdcpPduVolumeUl":"0","MM.HoPrepInterFail":"0","RRC.ConnMean":"0","MM.HoResAlloInterFail":"0","MM.HoExeIntraReq":"0","MM.HoPrepInterReq":"0","Sys.SpecEffUL":"0.0","PAG.ReceivedNbrCnInitiated":"0","MM.MM.HoExeInterFail.UeCtxtRelCmd.cause":"0","RRC.ConnEstabAtt":"0","RRC.ConnEstabSucc":"0"}}]}}}']
DEBUG:root:Processing message: {"event":{"commonEventHeader":{"sourceId":"","startEpochMicrosec":1713424500000000,"eventId":"greigns_1713425400_PM15min","reportingEntityId":"","internalHeaderFields":{"collectorTimeStamp":"Tue, 07 16 2024 02:46:52 GMT"},"eventType":"O_RAN_COMPONENT_PM15min","priority":"Low","version":"4.1","reportingEntityName":"node1.cluster.local","sequence":0,"domain":"measurement","lastEpochMicrosec":1713425400000000,"eventName":"measurement_O_RAN_COMPONENT_PM15min","vesEventListenerVersion":"7.2.1","sourceName":"greigns"},"measurementFields":{"measurementInterval":234,"measurementFieldsVersion":"4.0","additionalFields":{"src_id":"gNB_CU","ran_id":"ran1"},"additionalMeasurements":[{"name":"pm_data","hashMap":{"Sys.SpecEffDL":"0.0","RRC.ReEstabSuccWithoutUeContext":"0","MM.HoPrepIntraSucc":"0","MM.HoPrepInterSucc":"0","RRC.ReEstabAtt":"0","Sys.DataVolumeDL":"0","RRC.ReEstabSuccWithUeContext":"0","RRU.PrbTotDl":"0","Sys.CellAvail":"100","MM.HoResAlloInterSucc":"0","QosFlow.PdcpPduVolumeDl":"0","MM.HoExeInterReq":"0","Sys.DataVolumeUL":"0","MM.HoResAlloInterReq":"0","RRC.ConnMax":"0","MM.HoPrepIntraReq":"0","MM.HoExeIntraSucc":"0","MM.HoExeInterSucc":"0","PAG.DiscardedNbrCnInitiated":"0","PAG.SuccessRatio":"0","QosFlow.PdcpPduVolumeUl":"0","MM.HoPrepInterFail":"0","RRC.ConnMean":"0","MM.HoResAlloInterFail":"0","MM.HoExeIntraReq":"0","MM.HoPrepInterReq":"0","Sys.SpecEffUL":"0.0","PAG.ReceivedNbrCnInitiated":"0","MM.MM.HoExeInterFail.UeCtxtRelCmd.cause":"0","RRC.ConnEstabAtt":"0","RRC.ConnEstabSucc":"0"}}]}}}
```

#### dmaap receives gNB_CU_PM and stores it in influxDB successful result
```bash!
DEBUG:root:Sending message to InfluxDB: ran1_gNB_CU_PM,name=pm_data MM.HoExeInterReq=0i,MM.HoExeInterSucc=0i,MM.HoExeIntraReq=0i,MM.HoExeIntraSucc=0i,MM.HoPrepInterFail=0i,MM.HoPrepInterReq=0i,MM.HoPrepInterSucc=0i,MM.HoPrepIntraReq=0i,MM.HoPrepIntraSucc=0i,MM.HoResAlloInterFail=0i,MM.HoResAlloInterReq=0i,MM.HoResAlloInterSucc=0i,MM.MM.HoExeInterFail.UeCtxtRelCmd.cause=0i,PAG.DiscardedNbrCnInitiated=0i,PAG.ReceivedNbrCnInitiated=0i,PAG.SuccessRatio=0i,QosFlow.PdcpPduVolumeDl=0i,QosFlow.PdcpPduVolumeUl=0i,RRC.ConnEstabAtt=0i,RRC.ConnEstabSucc=0i,RRC.ConnMax=0i,RRC.ConnMean=0i,RRC.ReEstabAtt=0i,RRC.ReEstabSuccWithoutUeContext=0i,Sys.CellAvail=100i,Sys.DataVolumeDL=0i,Sys.DataVolumeUL=0i,Sys.SpecEffDL=0,Sys.SpecEffUL=0
```

#### proxy forwards gNB_DU_PM successfully result
```bash!
DEBUG:root:Pulling messages from topic unauthenticated.VES_MEASUREMENT_OUTPUT...
DEBUG:root:Pull response: ['{"event":{"commonEventHeader":{"sourceId":"","startEpochMicrosec":1713424500000000,"eventId":"greigns_1713425400_PM15min","reportingEntityId":"","internalHeaderFields":{"collectorTimeStamp":"Tue, 07 16 2024 02:53:49 GMT"},"eventType":"O_RAN_COMPONENT_PM15min","priority":"Low","version":"4.1","reportingEntityName":"node1.cluster.local","sequence":0,"domain":"measurement","lastEpochMicrosec":1713425400000000,"eventName":"measurement_O_RAN_COMPONENT_PM15min","vesEventListenerVersion":"7.2.1","sourceName":"greigns"},"measurementFields":{"measurementInterval":234,"measurementFieldsVersion":"4.0","additionalFields":{"src_id":"gNB_DU","ran_id":"ran1"},"additionalMeasurements":[{"name":"pm_data","hashMap":{"RRU.PrbTotDlDist.Bin61To70Percentage":"0","L1M.PHR1.BinMinus11ToMinus5dBm":"0","RRU.PrbTotUlDist.Bin50To60Percentage":"0","RRU.PrbTotDlDist.Bin71To80Percentage":"0","RRU.PrbTotUlDist.BinAbove98Percentage":"0","L1M.PHR1.BinMinus25ToMinus19dBm":"0","RRU.PrbTotUlDist.BinBelow50Percentage":"1","RACH.PreambleDed.0":"0","RRU.PrbTotUlDist.Bin94To96Percentage":"0","RRU.PrbTotDlDist.Bin97To98Percentage":"0","RRU.PrbTotUlDist.Bin81To85Percentage":"0","L1M.PHR1.Bin3To9dBm":"0","RACH.PreambleDedCell":"0","RRU.PrbTotDlDist.Bin86To90Percentage":"0","RRU.PrbTotUlDist.Bin86To90Percentage":"0","RRU.PrbTotDl":"0","RRU.PrbTotDlDist.BinAbove98Percentage":"0","RRU.PrbTotUlDist.Bin91To93Percentage":"0","RACH.PreambleBCell":"0","RRU.PrbTotUl":"1","RRU.PrbTotDlDist.Bin50To60Percentage":"0","L1M.PHR1.BinLessThanMinus32dBm":"0","RRU.PrbTotUlDist.Bin61To70Percentage":"0","L1M.PHR1.Bin24To31dBm":"0","L1M.PHR1.Bin32To37dBm":"0","RACH.PreambleACell":"0","L1M.PHR1.BinMinus4To2dBm":"0","RRU.PrbTotDlDist.Bin91To93Percentage":"0","RRU.PrbTotUlDist.Bin97To98Percentage":"0","L1M.PHR1.BinMinus32ToMinus26dBm":"0","RRU.PrbTotDlDist.Bin81To85Percentage":"0","L1M.PHR1.Bin10To16dBm":"0","RRU.PrbTotDlDist.Bin94To96Percentage":"0","RRU.PrbAvailUl":"78","L1M.PHR1.BinMinus18ToMinus12dBm":"0","PAG.ReceivedNbrCnInitiated":"0","RRU.PrbTotUlDist.Bin71To80Percentage":"0","L1M.PHR1.Bin17To23dBm":"0","L1M.PHR1.BinGreaterThan38":"0","RACH.PreambleA.0":"0","RRU.PrbTotDlDist.BinBelow50Percentage":"1","RRU.PrbAvailDl":"132","RACH.PreambleB.0":"0"}}]}}}']
DEBUG:root:Processing message: {"event":{"commonEventHeader":{"sourceId":"","startEpochMicrosec":1713424500000000,"eventId":"greigns_1713425400_PM15min","reportingEntityId":"","internalHeaderFields":{"collectorTimeStamp":"Tue, 07 16 2024 02:53:49 GMT"},"eventType":"O_RAN_COMPONENT_PM15min","priority":"Low","version":"4.1","reportingEntityName":"node1.cluster.local","sequence":0,"domain":"measurement","lastEpochMicrosec":1713425400000000,"eventName":"measurement_O_RAN_COMPONENT_PM15min","vesEventListenerVersion":"7.2.1","sourceName":"greigns"},"measurementFields":{"measurementInterval":234,"measurementFieldsVersion":"4.0","additionalFields":{"src_id":"gNB_DU","ran_id":"ran1"},"additionalMeasurements":[{"name":"pm_data","hashMap":{"RRU.PrbTotDlDist.Bin61To70Percentage":"0","L1M.PHR1.BinMinus11ToMinus5dBm":"0","RRU.PrbTotUlDist.Bin50To60Percentage":"0","RRU.PrbTotDlDist.Bin71To80Percentage":"0","RRU.PrbTotUlDist.BinAbove98Percentage":"0","L1M.PHR1.BinMinus25ToMinus19dBm":"0","RRU.PrbTotUlDist.BinBelow50Percentage":"1","RACH.PreambleDed.0":"0","RRU.PrbTotUlDist.Bin94To96Percentage":"0","RRU.PrbTotDlDist.Bin97To98Percentage":"0","RRU.PrbTotUlDist.Bin81To85Percentage":"0","L1M.PHR1.Bin3To9dBm":"0","RACH.PreambleDedCell":"0","RRU.PrbTotDlDist.Bin86To90Percentage":"0","RRU.PrbTotUlDist.Bin86To90Percentage":"0","RRU.PrbTotDl":"0","RRU.PrbTotDlDist.BinAbove98Percentage":"0","RRU.PrbTotUlDist.Bin91To93Percentage":"0","RACH.PreambleBCell":"0","RRU.PrbTotUl":"1","RRU.PrbTotDlDist.Bin50To60Percentage":"0","L1M.PHR1.BinLessThanMinus32dBm":"0","RRU.PrbTotUlDist.Bin61To70Percentage":"0","L1M.PHR1.Bin24To31dBm":"0","L1M.PHR1.Bin32To37dBm":"0","RACH.PreambleACell":"0","L1M.PHR1.BinMinus4To2dBm":"0","RRU.PrbTotDlDist.Bin91To93Percentage":"0","RRU.PrbTotUlDist.Bin97To98Percentage":"0","L1M.PHR1.BinMinus32ToMinus26dBm":"0","RRU.PrbTotDlDist.Bin81To85Percentage":"0","L1M.PHR1.Bin10To16dBm":"0","RRU.PrbTotDlDist.Bin94To96Percentage":"0","RRU.PrbAvailUl":"78","L1M.PHR1.BinMinus18ToMinus12dBm":"0","PAG.ReceivedNbrCnInitiated":"0","RRU.PrbTotUlDist.Bin71To80Percentage":"0","L1M.PHR1.Bin17To23dBm":"0","L1M.PHR1.BinGreaterThan38":"0","RACH.PreambleA.0":"0","RRU.PrbTotDlDist.BinBelow50Percentage":"1","RRU.PrbAvailDl":"132","RACH.PreambleB.0":"0"}}]}}}
```

#### dmaap receives gNB_CU_PM and stores it in influxDB successful result
```bash!
DEBUG:root:Sending message to InfluxDB: ran1_gNB_DU_PM,name=pm_data L1M.PHR1.Bin10To16dBm=0i,L1M.PHR1.Bin17To23dBm=0i,L1M.PHR1.Bin24To31dBm=0i,L1M.PHR1.Bin32To37dBm=0i,L1M.PHR1.Bin3To9dBm=0i,L1M.PHR1.BinGreaterThan38=0i,L1M.PHR1.BinLessThanMinus32dBm=0i,L1M.PHR1.BinMinus11ToMinus5dBm=0i,L1M.PHR1.BinMinus18ToMinus12dBm=0i,L1M.PHR1.BinMinus25ToMinus19dBm=0i,L1M.PHR1.BinMinus32ToMinus26dBm=0i,L1M.PHR1.BinMinus4To2dBm=0i,RACH.PreambleA.0=0i,RACH.PreambleACell=0i,RACH.PreambleB.0=0i,RACH.PreambleBCell=0i,RACH.PreambleDed.0=0i,RACH.PreambleDedCell=0i,RRU.PrbAvailDl=132i,RRU.PrbAvailUl=78i,RRU.PrbTotDl=0i,RRU.PrbTotDlDist.Bin50To60Percentage=0i,RRU.PrbTotDlDist.Bin61To70Percentage=0i,RRU.PrbTotDlDist.Bin71To80Percentage=0i,RRU.PrbTotDlDist.Bin81To85Percentage=0i,RRU.PrbTotDlDist.Bin86To90Percentage=0i,RRU.PrbTotDlDist.Bin91To93Percentage=0i,RRU.PrbTotDlDist.Bin94To96Percentage=0i,RRU.PrbTotDlDist.Bin97To98Percentage=0i,RRU.PrbTotDlDist.BinAbove98Percentage=0i,RRU.PrbTotDlDist.BinBelow50Percentage=1i,RRU.PrbTotUl=1i,RRU.PrbTotUlDist.Bin50To60Percentage=0i,RRU.PrbTotUlDist.Bin61To70Percentage=0i,RRU.PrbTotUlDist.Bin71To80Percentage=0i,RRU.PrbTotUlDist.Bin81To85Percentage=0i,RRU.PrbTotUlDist.Bin86To90Percentage=0i,RRU.PrbTotUlDist.Bin91To93Percentage=0i,RRU.PrbTotUlDist.Bin94To96Percentage=0i,RRU.PrbTotUlDist.Bin97To98Percentage=0i,RRU.PrbTotUlDist.BinAbove98Percentage=0i,RRU.PrbTotUlDist.BinBelow50Percentage=1i
```

## Hands on Trying
`testing.py`:
```python=
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
```
output:
```jsonld!
{
    "event": {
        "commonEventHeader": {
            "domain": "measurement",
            "eventId": "f2030d4z-8f0e-11eb-8dcd-0242ac130003",
            "eventName": "oran_pm",
            "eventType": "PM",
            "sequence": 0,
            "priority": "Low",
            "reportingEntityId": "",
            "reportingEntityName": "node1.cluster.local",
            "sourceId": "",
            "sourceName": "BBU_greigns",
            "startEpochMicrosec": 1721070900000000,
            "lastEpochMicrosec": 1721071800000000,
            "internalHeaderFields": {
                "intervalStartTime": "Mon, 15 Jul 2024 19:15:00 GMT",
                "intervalEndTime": "Mon, 15 Jul 2024 19:30:00 GMT"
            },
            "version": "4.1",
            "vesEventListenerVersion": "7.2.1"
        },
        "measurementFields": {
            "additionalFields": {
                "ran_id": "ran1",
                "src_id": "gNB_RU"
            },
            "additionalMeasurements": [
                {
                    "name": "pm_data",
                    "hashMap": {
                        "num_of_socket": "4",
                        "total_current": "10.5",
                        "total_powerload": "23270",
                        "socket_id_1": "0",
                        "socket_voltage_1": "386519.04",
                        "socket_current_1": "5862",
                        "socket_powerload_1": "188984852.48",
                        "socket_id_2": "1",
                        "socket_voltage_2": "386519.04",
                        "socket_current_2": "5862",
                        "socket_powerload_2": "188984852.48",
                        "socket_id_3": "2",
                        "socket_voltage_3": "386519.04",
                        "socket_current_3": "5862",
                        "socket_powerload_3": "188984852.48",
                        "socket_id_4": "3",
                        "socket_voltage_4": "386519.04",
                        "socket_current_4": "5862",
                        "socket_powerload_4": "188984852.48"
                    }
                }
            ],
            "measurementInterval": 15,
            "measurementFieldsVersion": "4.0"
        }
    }
}
```
curl command:
```bash
curl -i -k -u sample1:sample1 -X POST -d '{
    "event": {
        "commonEventHeader": {
            "domain": "measurement",
            "eventId": "f2030d4z-8f0e-11eb-8dcd-0242ac130003",
            "eventName": "oran_pm",
            "eventType": "PM",
            "sequence": 0,
            "priority": "Low",
            "reportingEntityId": "",
            "reportingEntityName": "node1.cluster.local",
            "sourceId": "",
            "sourceName": "BBU_greigns",
            "startEpochMicrosec": 1721070900000000,
            "lastEpochMicrosec": 1721071800000000,
            "internalHeaderFields": {
                "intervalStartTime": "Mon, 15 Jul 2024 19:15:00 GMT",
                "intervalEndTime": "Mon, 15 Jul 2024 19:30:00 GMT"
            },
            "version": "4.1",
            "vesEventListenerVersion": "7.2.1"
        },
        "measurementFields": {
            "additionalFields": {
                "ran_id": "ran1",
                "src_id": "gNB_RU"
            },
            "additionalMeasurements": [
                {
                    "name": "pm_data",
                    "hashMap": {
                        "num_of_socket": "4",
                        "total_current": "10.5",
                        "total_powerload": "23270",
                        "socket_id_1": "0",
                        "socket_voltage_1": "386519.04",
                        "socket_current_1": "5862",
                        "socket_powerload_1": "188984852.48",
                        "socket_id_2": "1",
                        "socket_voltage_2": "386519.04",
                        "socket_current_2": "5862",
                        "socket_powerload_2": "188984852.48",
                        "socket_id_3": "2",
                        "socket_voltage_3": "386519.04",
                        "socket_current_3": "5862",
                        "socket_powerload_3": "188984852.48",
                        "socket_id_4": "3",
                        "socket_voltage_4": "386519.04",
                        "socket_current_4": "5862",
                        "socket_powerload_4": "188984852.48"
                    }
                }
            ],
            "measurementInterval": 15,
            "measurementFieldsVersion": "4.0"
        }
    }
}' --header "Content-Type: application/json" http://192.168.0.237:30417/eventListener/v7
```
InfluxDB:
![image](https://hackmd.io/_uploads/H1xFTqXuC.png)
Grafana:
![image](https://hackmd.io/_uploads/HJwklimO0.png)
