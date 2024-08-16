# Show the Data on SMO InfluxDB and Grafana
# Deployment of dmaap-InfluxDB-adapter, InfluxDB and Grafana
## Prerequisite
Finished the installation of ONAP SMO.
## Deploy
### Helm repo add and install
```
helm repo add winlab https://harbor.winfra.cs.nycu.edu.tw/chartrepo/winlab-oran
helm install --namespace=o1ves o1ves winlab/o1ves-visualization --create-namespace
```
### Get the Helm repo compressed package
```
helm pull winlab/o1ves-visualization
tar -zxvf o1ves-visualization-<version>.tgz
```
## Edit the values.yaml file
```bash
helm show values winlab/o1ves-visualization > values.yaml
```
If you have edited the value.yaml file, you need to re-upload the pod or delete it and redeploy it.
```bash
## Upgrade
helm upgrade --namespace=o1ves o1ves winlab/o1ves-visualization --create-namespace -f values.yaml

## Redeploy
helm uninstall --namespace o1ves o1ves  
kubectl delete ns o1ves
sudo rm -r /dockerdata-nfs/o1ves-*
helm install --namespace=o1ves o1ves winlab/o1ves-visualization --create-namespace -f values.yaml
```

Test using ves to send events to influxdb
```bash
curl -X POST \
   -H 'Content-Type: application/json' \
   -u sample1:sample1 \
   -d @file.json \
   http://192.168.0.237:30001/eventListener/v7
```
output:
```bash
Warning: Couldn't read data from file "file.json", this makes an empty POST.
<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="description" content="InfluxDB is a time series platform, purpose-built by InfluxData for storing metrics and events, provides real-time visibility into stacks, sensors, and systems."><title>InfluxDB</title><base href="/"><link rel="shortcut icon" href="/favicon.ico"></head><body><div id="react-root" data-basepath=""></div><script src="/6588f709b0.js"></script></body></html>
```

Check whether influxdb-adapter is receiving:
```
kubectl get pods -n o1ves
```
output:
```
NAME                                            READY   STATUS      RESTARTS       AGE
o1ves-dmaap-influxdb-adapter-7bf778b965-b2j9t   1/1     Running     5 (3h3m ago)   4h14m
o1ves-grafana-5cbb656595-lrx9t                  1/1     Running     0              4h14m
o1ves-grafana-datasource-provisioning-hqv2q     0/1     Completed   0              4h14m
o1ves-influxdb2-0                               1/1     Running     0              4h14m
o1ves-influxdb2-config-2tgfn                    0/1     Completed   0              4h14m
```
```
kubectl logs -n o1ves o1ves-dmaap-influxdb-adapter-7bf778b965-b2j9t
```
output:
```
WARNING:root:Topic unauthenticated.VES_MEASUREMENT_OUTPUT not exists
DEBUG:root:Pull response: None
DEBUG:root:Pulling messages from topic unauthenticated.VES_MEASUREMENT_OUTPUT...
WARNING:root:Topic unauthenticated.VES_MEASUREMENT_OUTPUT not exists
DEBUG:root:Pull response: None
DEBUG:root:Pulling messages from topic unauthenticated.VES_MEASUREMENT_OUTPUT...
```
**question**
The above result shows that the topic cannot be found.
-> After sending the packet once using the curl command, it will automatically create the topic.

Reference:
[dmaap API](https://docs.onap.org/projects/onap-dmaap-messagerouter-messageservice/en/latest/offeredapis/api.html)
Our `values.yaml` files can fill in our own rules for capturing data and transfer them to influxDB. The above API files can let us know `topic` what we currently have and can create `topic` and use them.

Use K8s instructions to know the dmaap IP:
```bash
kubectl get svc -A
```
see this part:
```bash
onap          message-router                          ClusterIP   10.233.10.242   <none>        3904/TCP                                       23h
```
```bash
curl -X GET http://10.233.10.242:3904/topics
```
output:
```bash
{"topics": [
    "POLICY-PDP-PAP",
    "__strimzi_store_topic",
    "unauthenticated.dmaapmed.json",
    "__strimzi-topic-operator-kstreams-topic-store-changelog",
    "policy.clamp-runtime-acm",
    "unauthenticated.SEC_FAULT_OUTPUT"
]}
```

Use `echo` the command to confirm whether there is a value
```bash
echo <content> | jq '<path to value>'
```

## InfluxDB, Grafana Web UI and Set InfluxDB Data Source

### InfluxDB
![image](https://hackmd.io/_uploads/SyRPW_RvA.png)
username: admin
password:
```bash
kubectl get secret -n o1ves o1ves-influxdb2-auth -o json
echo enVqWmJqNDRheGdrdVRzWEkyOTJQQU1uQkYxNTNMWng= | base64 -d
```

### Grafana Web UI 
![image](https://hackmd.io/_uploads/ByPHzuRD0.png)
username: admin
password: smo

### Configure Grafana to connect to InfluxDB
1. Step 1:
Home -> Administration -> Data sources, you will see the default influxdb after entering.
2. Step 2: 
Check settings
Query Language: Flux
URL: http://o1ves-influxdb2.o1ves
Auth
Basic auth: Disable
InfluxDB Details
Organization: influxdata
Token: my-token
![image](https://hackmd.io/_uploads/Syvs9Wzd0.png)

3. In InfluxDB, click the admin icon->About->Name to know the name of the organization.
![image](https://hackmd.io/_uploads/Bk-Oo-z_0.png)

4. Verify that the connection between influxdb and grafana is OK.
    InfluxDB:
    ```bash
    curl -i http://192.168.0.237:30001/ping
    ```
    output:
    ```bash
    HTTP/1.1 204 No Content
    X-Influxdb-Build: OSS
    X-Influxdb-Version: v2.3.0+SNAPSHOT.090f681737
    Date: Mon, 15 Jul 2024 02:34:46 GMT
    ```
    Grafana:
    ```bash
    curl -i http://192.168.0.237:30000/ping
    ```
    output:
    ```bash
    HTTP/1.1 302 Found
    Cache-Control: no-store
    Content-Type: text/html; charset=utf-8
    Location: /login
    Set-Cookie: redirect_to=%2Fping; Path=/; HttpOnly; SameSite=Lax
    X-Content-Type-Options: nosniff
    X-Frame-Options: deny
    X-Xss-Protection: 1; mode=block
    Date: Mon, 15 Jul 2024 02:39:19 GMT
    Content-Length: 29

    <a href="/login">Found</a>.
    ```
