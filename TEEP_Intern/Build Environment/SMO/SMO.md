# OSC SMO (ONAP)

- [OSC SMO (ONAP)](#osc-smo-onap)
  - [Introduction](#introduction)
  - [Environment](#environment)
    - [Mininum Requirement](#mininum-requirement)
      - [Hardware](#hardware)
      - [Software](#software)
  - [Used Hardware Specifications](#used-hardware-specifications)
    - [Prerequisite](#prerequisite)
      - [0. Log in as root](#0-log-in-as-root)
      - [1. Install Kubernetes with kubespray](#1-install-kubernetes-with-kubespray)
    - [Deployment](#deployment)
      - [1. Download the IT/dep repository from gerrit](#1-download-the-itdep-repository-from-gerrit)
      - [2. Setup Helm Charts](#2-setup-helm-charts)
      - [3. Deploy Components](#3-deploy-components)
    - [Deployment of dmaap-InfluxDB-adapter, InfluxDB and Grafana](#deployment-of-dmaap-influxdb-adapter-influxdb-and-grafana)
      - [1. Helm repository addition and installation](#1-helm-repository-addition-and-installation)
      - [2. Edit the values.yaml file](#2-edit-the-valuesyaml-file)
      - [3. Delete](#3-delete)
      - [4. If you edit the values.yaml , you need to upgrade the pod or delete and redeploy.](#4-if-you-edit-the-valuesyaml--you-need-to-upgrade-the-pod-or-delete-and-redeploy)
      - [Problem](#problem)
    - [Result](#result)
      - [Pods](#pods)
      - [InfluxDB](#influxdb)
      - [Grafana](#grafana)
  - [Troubleshooting for CrashLoopBackOff dmaap-influxdb](#troubleshooting-for-crashloopbackoff-dmaap-influxdb)


## Introduction
This markdown guide consist of the step by step installation of O-RAN Service Community Service Management and Orchestration. This guide is based on this [HackMD](https://hackmd.io/@H141319/ByOoZCmDa)

## Environment
### Mininum Requirement
#### Hardware
```
6 or more CPU cores
28+ GB of RAM
50 GB of Disk 
```
#### Software
```
Ubuntu 22.04 server
Kubernetes v1.27.5 
python3 3.10.12 # Version should upper or equal to 3.9
SMO Release J (onap_upgrade provide by NYCU)
Non-RT RIC Release H
```

## Used Hardware Specifications
```
32 CPU cores (4 Sockets, 8 Cores)
50 GiB of RAM
100 GiB of Disk
```

### Prerequisite
#### 0. Log in as root
```bash
sudo -i
```

#### 1. Install Kubernetes with kubespray
command:
```bash
python3 --version # Version should upper or equal to 3.9
apt install -y python3-pip
```

output:
```bash
root@teep-template:~# python3 --version # Version should upper or equal to 3.9
apt install -y python3-pip
Python 3.10.12
Reading package lists... Done
Building dependency tree... Done
Reading state information... Done
python3-pip is already the newest version (22.0.2+dfsg-1ubuntu0.4).
0 upgraded, 0 newly installed, 0 to remove and 99 not upgraded.
```

command:
```bash
git clone https://github.com/kubernetes-sigs/kubespray -b release-2.23
cd kubespray 
pip install -r requirements.txt
```

output:
```bash
root@teep-template:~/kubespray# pip install -r requirements.txt
Requirement already satisfied: ansible==7.6.0 in /usr/local/lib/python3.10/dist-packages (from -r requirements.txt (line 1)) (7.6.0)
Requirement already satisfied: cryptography==41.0.1 in /usr/local/lib/python3.10/dist-packages (from -r requirements.txt (line 2)) (41.0.1)
Requirement already satisfied: jinja2==3.1.2 in /usr/local/lib/python3.10/dist-packages (from -r requirements.txt (line 3)) (3.1.2)
Requirement already satisfied: jmespath==1.0.1 in /usr/local/lib/python3.10/dist-packages (from -r requirements.txt (line 4)) (1.0.1)
Requirement already satisfied: MarkupSafe==2.1.3 in /usr/local/lib/python3.10/dist-packages (from -r requirements.txt (line 5)) (2.1.3)
Requirement already satisfied: netaddr==0.8.0 in /usr/local/lib/python3.10/dist-packages (from -r requirements.txt (line 6)) (0.8.0)
Requirement already satisfied: pbr==5.11.1 in /usr/local/lib/python3.10/dist-packages (from -r requirements.txt (line 7)) (5.11.1)
Requirement already satisfied: ruamel.yaml==0.17.31 in /usr/local/lib/python3.10/dist-packages (from -r requirements.txt (line 8)) (0.17.31)
Requirement already satisfied: ruamel.yaml.clib==0.2.7 in /usr/local/lib/python3.10/dist-packages (from -r requirements.txt (line 9)) (0.2.7)
Requirement already satisfied: ansible-core~=2.14.6 in /usr/local/lib/python3.10/dist-packages (from ansible==7.6.0->-r requirements.txt (line 1)) (2.14.15)
Requirement already satisfied: cffi>=1.12 in /usr/local/lib/python3.10/dist-packages (from cryptography==41.0.1->-r requirements.txt (line 2)) (1.16.0)
Requirement already satisfied: packaging in /usr/local/lib/python3.10/dist-packages (from ansible-core~=2.14.6->ansible==7.6.0->-r requirements.txt (line 1)) (24.0)
Requirement already satisfied: resolvelib<0.9.0,>=0.5.3 in /usr/local/lib/python3.10/dist-packages (from ansible-core~=2.14.6->ansible==7.6.0->-r requirements.txt (line 1)) (0.8.1)
Requirement already satisfied: PyYAML>=5.1 in /usr/lib/python3/dist-packages (from ansible-core~=2.14.6->ansible==7.6.0->-r requirements.txt (line 1)) (5.4.1)
Requirement already satisfied: pycparser in /usr/local/lib/python3.10/dist-packages (from cffi>=1.12->cryptography==41.0.1->-r requirements.txt (line 2)) (2.22)
```

command:
```bash
sed -i 's/\(kube_version: \)[^"]*/\1v1.27.5/' inventory/local/group_vars/k8s_cluster/k8s-cluster.yml
ansible-playbook -i inventory/local/hosts.ini --become --become-user=root cluster.yml
```

output:
```bash
root@teep-template:~/kubespray# sed -i 's/\(kube_version: \)[^"]*/\1v1.27.5/' inventory/local/group_vars/k8s_cluster/k8s-cluster.yml
ansible-playbook -i inventory/local/hosts.ini --become --become-user=root cluster.yml
[WARNING]: Skipping callback plugin 'ara_default', unable to load

PLAY [Check Ansible version] ***********************************************************************************
Jumat 19 April 2024  20:27:25 +0700 (0:00:00.015)       0:00:00.015 ***********

TASK [Check 2.14.0 <= Ansible version < 2.15.0] ****************************************************************
ok: [localhost] => {
    "changed": false,
    "msg": "All assertions passed"
}
Jumat 19 April 2024  20:27:25 +0700 (0:00:00.044)       0:00:00.060 ***********
```

command:
```bash
mkdir -p ~/.kube/config
sudo cp /etc/kubernetes/admin.conf ~/.kube/config
```

### Deployment
#### 1. Download the IT/dep repository from gerrit
command:
```bash
cd ~
git clone https://gerrit.o-ran-sc.org/r/it/dep.git -b master --recursive
```

output:
```bash
root@teep-template:~/kubespray# cd ~
git clone https://gerrit.o-ran-sc.org/r/it/dep.git -b master --recursive
Cloning into 'dep'...
remote: Counting objects: 427, done
remote: Finding sources: 100% (424/424)
Receiving objects:   5% (405/7203), 131.97 KiB | 19.00 KiB/s
```

#### 2. Setup Helm Charts
Execute the following commands being logged as root:
```bash
cd dep
##Setup ChartMuseum
./smo-install/scripts/layer-0/0-setup-charts-museum.sh

##Setup HELM3
./smo-install/scripts/layer-0/0-setup-helm3.sh

## Build ONAP/ORAN charts
./smo-install/scripts/layer-1/1-build-all-charts.sh
```

output:
```bash
[a1policymanagement]
make[1]: Entering directory '/root/dep/smo-install/onap_oom/kubernetes'
Hang tight while we grab the latest from your chart repositories...
2024-04-19T22:19:41.063+0700    INFO    [56] Request served     {"path": "/index.yaml", "comment": "", "clientIP": "127.0.0.1", "method": "GET", "statusCode": 200, "latency": "1.297377ms", "reqID": "cdf9f448-11ab-4187-99f2-5c3e3c732079"}
...Successfully got an update from the "local" chart repository
Update Complete. ⎈Happy Helming!⎈
Saving 3 charts
Downloading common from repo http://localhost:18080
2024-04-19T22:19:41.088+0700    INFO    [57] Request served     {"path": "/charts/common-13.0.2.tgz", "comment": "", "clientIP": "127.0.0.1", "method": "GET", "statusCode": 200, "latency": "471.474µs", "reqID": "88f85d36-10c1-458f-b53f-f6f59cf62302"}
Downloading repositoryGenerator from repo http://localhost:18080
2024-04-19T22:19:41.094+0700    INFO 
.
.
.
5360-9b7e-490c-9abf-cdb888df5cb4"}
Deleting outdated charts
Skipping linting of a1policymanagement
Pushing a1policymanagement-13.0.0.tgz to local...
2024-04-19T22:19:41.526+0700    INFO    [60] Request served     {"path": "/api/charts", "comment": "", "clientIP": "127.0.0.1", "method": "POST", "statusCode": 201, "latency": "22.081585ms", "reqID": "2c689f9e-4893-4d4d-9c15-82d6a397b31b"}
Done.
^Cmake[1]: *** [Makefile:84: package-a1policymanagement] Interrupt
make: *** [Makefile:52: a1policymanagement] Interrupt

root@teep-template:~/dep#
```

#### 3. Deploy Components
Execute the following commands being logged as root:
```bash
./smo-install/scripts/layer-2/2-install-oran.sh
```
**Important!: Wait until all the pods are running, then continue!**
Check pods:
```
kubectl get pods -A
```
### Deployment of dmaap-InfluxDB-adapter, InfluxDB and Grafana

#### 1. Helm repository addition and installation
```bash
helm repo add winlab https://harbor.winfra.cs.nycu.edu.tw/chartrepo/winlab-oran
helm install --namespace=o1ves o1ves winlab/o1ves-visualization --create-namespace
```

output:
```bash
root@node1:~# helm repo add winlab https://harbor.winfra.cs.nycu.edu.tw/chartrepo/winlab-oran
"winlab" has been added to your repositories
root@node1:~# helm repo add winlab https://harbor.winfra.cs.nycu.edu.tw/chartrepo/winlab-oran
helm install --namespace=o1ves o1ves winlab/o1ves-visualization --create-namespace
"winlab" already exists with the same configuration, skipping


NAME: o1ves
LAST DEPLOYED: Wed May  8 12:58:59 2024
NAMESPACE: o1ves
STATUS: deployed
REVISION: 1
NOTES:
o1ves-visualization has been installed. Check its status by running:
  kubectl --namespace o1ves get pods -l "release=o1ves"
```

#### 2. Edit the values.yaml file
```bash
helm show values winlab/o1ves-visualization > values.yaml
```
edit values.yaml from:
```bash
fullnameOverride: o1ves

grafana:
  fullnameOverride: o1ves-grafana
  enabled: true
  defaultDashboardsTimezone: Asia/Taipei
  adminPassword: smo
  service:
    type: NodePort
    nodePort: 30000
  persistence:
    enabled: true
    storageClassName: "local-storage-grafana"
    size: 10Gi

influxdb2:
  fullnameOverride: o1ves-influxdb2
  enabled: true
  persistence:
    enabled: true
    storageClass: "local-storage-influxdb2"
    accessMode: ReadWriteOnce
    size: 50Gi
    mountPath: /var/lib/influxdb2
    subPath: ""
  image:
    repository: influxdb
    tag: 2.3.0-alpine
    pullPolicy: IfNotPresent

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
    - topic: unauthenticated.SEC_FAULT_OUTPUT
      rules:
        - bucket: influxdb
          measurement: fault
          matches: 
            - key: event.commonEventHeader.domain
              value: fault
          tags:
            - key: type
              value: test
            - key: sourceId
              field: event.commonEventHeader.sourceId
          fields:
            - key: faultFieldsVersion
              field: event.faultFields.faultFieldsVersion
              type: string

buckets:
  - name: influxdb

image:
  pullPolicy: IfNotPresent
```
into:
```bash
fullnameOverride: o1ves

grafana:
  fullnameOverride: o1ves-grafana
  enabled: true
  defaultDashboardsTimezone: Asia/Taipei
  adminPassword: smo
  service:
    type: NodePort
    nodePort: 30000
  persistence:
    enabled: true
    storageClassName: "local-storage-grafana"
    size: 10Gi

influxdb2:
  fullnameOverride: o1ves-influxdb2
  enabled: true
  persistence:
    enabled: true
    storageClass: "local-storage-influxdb2"
    accessMode: ReadWriteOnce
    size: 50Gi
    mountPath: /var/lib/influxdb2
    subPath: ""
  image:
    repository: influxdb
    tag: 2.3.0-alpine
    pullPolicy: IfNotPresent
  service:
    type: NodePort
    port: 80
    targetPort: 8086
    nodePort: 30001
    annotations: {}
    labels: {}
    portName: http

dmaap-influxdb-adapter:
  image:
    pullPolicy: Always
  logLevel: DEBUG
  rules:
    - topic: unauthenticated.VES_MEASUREMENT_OUTPUT
      rules:
        - bucket: my-bucket
          measurement: slice-measurement
          matches:
            - key: event.commonEventHeader.domain
              value: stndDefined
          tags:
            - key: vendor
              value: ntust-taiwan-lab
            - key: sourceName
              field: event.commonEventHeader.sourceName
          fields:
            - key: avg-throughput-downlink
              field: event.stndDefinedFields.data.measurements[0].value
              type: int
            - key: ue-avg-mcs-index
              field: event.stndDefinedFields.data.measurements[1].value
              type: float

buckets:
  - name: my-bucket

image:
  pullPolicy: IfNotPresent
```

#### 3. Delete
```bash
helm uninstall --namespace o1ves o1ves  
kubectl delete ns o1ves
sudo rm -r /dockerdata-nfs/o1ves-*
```
output:
```bash
root@node1:~# helm uninstall --namespace o1ves o1ves
kubectl delete ns o1ves
sudo rm -r /dockerdata-nfs/o1ves-*
These resources were kept due to the resource policy:
[PersistentVolumeClaim] o1ves-influxdb2

release "o1ves" uninstalled
namespace "o1ves" deleted
```

#### 4. If you edit the values.yaml , you need to upgrade the pod or delete and redeploy.
```bash
## Upgrade
helm upgrade --namespace=o1ves o1ves winlab/o1ves-visualization --create-namespace -f value2.yml

## Redeploy
helm uninstall --namespace o1ves o1ves  
kubectl delete ns o1ves
sudo rm -r /dockerdata-nfs/o1ves-*
helm install --namespace=o1ves o1ves winlab/o1ves-visualization --create-namespace -f values.yaml
```

output:
```bash
root@node1:~# ## Upgrade
helm upgrade --namespace=o1ves o1ves winlab/o1ves-visualization --create-namespace -f value2.yml

## Redeploy
helm uninstall --namespace o1ves o1ves
kubectl delete ns o1ves
sudo rm -r /dockerdata-nfs/o1ves-*
helm install --namespace=o1ves o1ves winlab/o1ves-visualization --create-namespace -f values.yaml
Error: open value2.yml: no such file or directory
Error: uninstall: Release not loaded: o1ves: release: not found
Error from server (NotFound): namespaces "o1ves" not found
rm: cannot remove '/dockerdata-nfs/o1ves-*': No such file or directory
NAME: o1ves
LAST DEPLOYED: Wed May  8 13:07:22 2024
NAMESPACE: o1ves
STATUS: deployed
REVISION: 1
NOTES:
o1ves-visualization has been installed. Check its status by running:
  kubectl --namespace o1ves get pods -l "release=o1ves"
```
#### Problem
Assuming that Jiaotong University shuts down the Docker Server, the above resources will not be deployed, and the resources have been git pushed to its own git hub.
```bash
git clone https://github.com/Hsukevin121/o1ves-visualization.git
kubectl create namespace o1ves
helm install --namespace=o1ves o1ves o1ves-visualization/o1ves-visualization --create-namespace -f values.yaml
```

### Result
#### Pods
```
root@node1:~# kubectl get pods -A
NAMESPACE        NAME                                                READY   STATUS             RESTARTS           AGE
kube-system      calico-kube-controllers-794577df96-986br            1/1     Running            7 (6d20h ago)      8d
kube-system      calico-node-v2tmx                                   1/1     Running            2 (6d20h ago)      8d
kube-system      coredns-5c469774b8-cbmtf                            1/1     Running            2 (6d20h ago)      8d
kube-system      dns-autoscaler-5cc59c689b-9rvk6                     1/1     Running            2 (6d20h ago)      8d
kube-system      kube-apiserver-node1                                1/1     Running            4 (6d20h ago)      8d
kube-system      kube-controller-manager-node1                       1/1     Running            17 (6d20h ago)     8d
kube-system      kube-proxy-r4cq8                                    1/1     Running            2 (6d20h ago)      8d
kube-system      kube-scheduler-node1                                1/1     Running            13 (6d20h ago)     8d
kube-system      nodelocaldns-jjzgq                                  1/1     Running            4 (6d20h ago)      8d
nonrtric         a1-sim-osc-0-7d8f49d4b8-8mltz                       1/1     Running            2 (6d20h ago)      7d21h
nonrtric         a1-sim-osc-1-7b6dd4675c-jt5qz                       1/1     Running            2 (6d20h ago)      7d21h
nonrtric         a1-sim-std-0-666d947c7c-hfc6j                       1/1     Running            2 (6d20h ago)      7d21h
nonrtric         a1-sim-std-1-f8778bf66-j67ts                        1/1     Running            2 (6d20h ago)      7d21h
nonrtric         a1-sim-std2-0-79cfbc9fdd-ttfzf                      1/1     Running            2 (6d20h ago)      7d21h
nonrtric         a1-sim-std2-1-9fcdcbc9c-7vndt                       1/1     Running            2 (6d20h ago)      7d21h
nonrtric         capifcore-5845ccc68-79tc5                           1/1     Running            4 (6d20h ago)      7d21h
nonrtric         controlpanel-c4f5c58f8-ssmdf                        1/1     Running            5 (6d20h ago)      7d21h
nonrtric         dmaapadapterservice-0                               1/1     Running            4 (6d20h ago)      7d21h
nonrtric         dmaapmediatorservice-0                              1/1     Running            3 (6d20h ago)      7d21h
nonrtric         helmmanager-0                                       1/1     Running            7 (6d20h ago)      7d21h
nonrtric         informationservice-0                                1/1     Running            9 (6d20h ago)      7d21h
nonrtric         nonrtricgateway-d46cf479c-82kdc                     1/1     Running            7 (6d20h ago)      7d21h
nonrtric         odu-app-b7f7f9f56-695jc                             1/1     Running            2 (6d20h ago)      7d21h
nonrtric         odu-app-ics-version-7df48b8d5d-bfwhv                1/1     Running            2 (6d20h ago)      7d21h
nonrtric         oran-nonrtric-kong-5d878fb6df-9kbzx                 0/2     Init:1/2           2                  7d21h
nonrtric         oran-nonrtric-kong-init-migrations-dffjk            0/1     Completed          0                  7d21h
nonrtric         oran-nonrtric-postgresql-0                          1/1     Running            2 (6d20h ago)      7d21h
nonrtric         oru-app-98d99c694-tkxkl                             1/1     Running            2 (6d20h ago)      7d21h
nonrtric         policymanagementservice-0                           1/1     Running            9 (6d20h ago)      7d21h
nonrtric         rappcatalogueservice-7cc75f77dc-bs22x               1/1     Running            4 (6d20h ago)      7d21h
nonrtric         rappmanager-0                                       1/1     Running            6 (6d20h ago)      7d21h
nonrtric         servicemanager-566b96b854-49rxz                     1/1     Running            3 (6d20h ago)      7d21h
nonrtric         topology-7d78f99678-jv7nb                           1/1     Running            9 (6d20h ago)      7d21h
o1ves            o1ves-dmaap-influxdb-adapter-9555f7c6b-zvw9t        0/1     CrashLoopBackOff   1968 (2m50s ago)   7d21h
o1ves            o1ves-grafana-5cbb656595-rqbph                      1/1     Running            2 (6d20h ago)      7d21h
o1ves            o1ves-grafana-datasource-provisioning-9hwmz         0/1     Completed          0                  7d21h
o1ves            o1ves-influxdb2-0                                   1/1     Running            8 (6d20h ago)      7d21h
o1ves            o1ves-influxdb2-config-qdzjh                        0/1     Completed          0                  7d21h
onap             onap-dcae-ves-collector-8b767f86f-p94jr             1/1     Running            1 (6d21h ago)      7d21h
onap             onap-mariadb-galera-0                               2/2     Running            8 (6d20h ago)      7d21h
onap             onap-message-router-0                               2/2     Running            5 (6d20h ago)      7d21h
onap             onap-nengdb-init-config-job-ql5pn                   0/1     Completed          0                  7d21h
onap             onap-network-name-gen-5cf7bdc944-g2m2n              1/1     Running            3 (6d20h ago)      7d21h
onap             onap-policy-apex-pdp-55694fc89-44frg                1/1     Running            3 (6d21h ago)      7d21h
onap             onap-policy-api-6799979dd7-p7sg8                    1/1     Running            7 (6d20h ago)      7d21h
onap             onap-policy-clamp-ac-a1pms-ppnt-557bd5b778-fgmp2    1/1     Running            4 (6d20h ago)      7d21h
onap             onap-policy-clamp-ac-http-ppnt-99dc78cb7-vxnvn      1/1     Running            3 (6d20h ago)      7d21h
onap             onap-policy-clamp-ac-k8s-ppnt-5599cf945b-hgcw5      1/1     Running            3 (6d20h ago)      7d21h
onap             onap-policy-clamp-ac-kserve-ppnt-584c884bf8-v7rhq   1/1     Running            6 (6d20h ago)      7d21h
onap             onap-policy-clamp-ac-pf-ppnt-7f5b54df6d-s754n       1/1     Running            3 (6d20h ago)      7d21h
onap             onap-policy-clamp-runtime-acm-c48d847f5-h9vjt       1/1     Running            6 (6d20h ago)      7d21h
onap             onap-policy-galera-config-rhnxc                     0/1     Completed          0                  7d21h
onap             onap-policy-galera-init-jlt6z                       0/1     Completed          0                  7d21h
onap             onap-policy-mariadb-0                               2/2     Running            10 (6d20h ago)     7d21h
onap             onap-policy-pap-6c7b78f655-wvp9d                    1/1     Running            2 (6d21h ago)      7d21h
onap             onap-sdnc-0                                         1/1     Running            5 (6d20h ago)      7d21h
onap             onap-sdnc-ansible-server-78dd459b84-v4pzl           1/1     Running            3 (6d21h ago)      7d21h
onap             onap-sdnc-dbinit-job-qlc69                          0/1     Completed          0                  7d21h
onap             onap-sdnc-dgbuilder-7bcf65ff78-4fvss                1/1     Running            2 (6d20h ago)      7d21h
onap             onap-sdnc-dmaap-listener-64cd9f4d5b-chlmm           1/1     Running            1 (6d21h ago)      7d21h
onap             onap-sdnc-sdnrdb-init-job-qzft9                     0/1     Completed          0                  7d21h
onap             onap-sdnc-web-5cd4697dc-xg9b6                       1/1     Running            2 (6d21h ago)      7d21h
onap             onap-sdnrdb-coordinating-only-567cf48d7-xd5kk       2/2     Running            4 (6d20h ago)      7d21h
onap             onap-sdnrdb-master-0                                1/1     Running            2 (6d20h ago)      7d21h
onap             onap-strimzi-entity-operator-864cb5b89d-lrjrm       3/3     Running            12 (6d20h ago)     7d21h
onap             onap-strimzi-kafka-0                                1/1     Running            2 (6d20h ago)      7d21h
onap             onap-strimzi-zookeeper-0                            1/1     Running            3 (6d20h ago)      7d21h
strimzi-system   strimzi-cluster-operator-64f9bf48c9-qswll           1/1     Running            7 (6d20h ago)      7d21h
```

#### InfluxDB
http:/<host_ip>/:30001
Here we use http://192.168.0.237:30001
username and password : (admin/)
Use this command to find the password:
```bash
kubectl get secret -n o1ves o1ves-influxdb2-auth -o json
```

find the password then echo:
```bash
echo enVqWmJqNDRheGdrdVRzWEkyOTJQQU1uQkYxNTNMWng= | base64 -d
```

If InfluxDB port didn't open, you can refer this:
```bash
kubectl edit svc -n o1ves o1ves-influxdb2

# line 33 add: nodePort:30001
# line 41 type change to NodePort
```

![image](https://hackmd.io/_uploads/rJmnRJSDC.png)

#### Grafana
http:/<host_ip>/:30000
Comment
Suggest edit
Here we use http://192.168.0.237:30000

username and password : (admin/smo)

![image](https://hackmd.io/_uploads/rJijAyrw0.png)

## Troubleshooting for CrashLoopBackOff dmaap-influxdb
```bash
sudo nano /etc/sysctl.conf

fs.inotify.max_user_instances = 16384

sudo sysctl -p

## Redeploy
helm uninstall --namespace o1ves o1ves  
kubectl delete ns o1ves
sudo rm -r /dockerdata-nfs/o1ves-*

cd dep
./smo-install/scripts/uninstall-all.sh

##Setup ChartMuseum
./smo-install/scripts/layer-0/0-setup-charts-museum.sh

##Setup HELM3
./smo-install/scripts/layer-0/0-setup-helm3.sh

## Build ONAP/ORAN charts
./smo-install/scripts/layer-1/1-build-all-charts.sh

./smo-install/scripts/layer-2/2-install-oran.sh

```

Result:
```bash
root@node1:~/dep# kubectl get pods -A
NAMESPACE        NAME                                                READY   STATUS      RESTARTS        AGE
kube-system      calico-kube-controllers-794577df96-986br            1/1     Running     7 (10d ago)     11d
kube-system      calico-node-v2tmx                                   1/1     Running     2 (10d ago)     11d
kube-system      coredns-5c469774b8-cbmtf                            1/1     Running     2 (10d ago)     11d
kube-system      dns-autoscaler-5cc59c689b-9rvk6                     1/1     Running     2 (10d ago)     11d
kube-system      kube-apiserver-node1                                1/1     Running     4 (10d ago)     11d
kube-system      kube-controller-manager-node1                       1/1     Running     17 (10d ago)    11d
kube-system      kube-proxy-r4cq8                                    1/1     Running     2 (10d ago)     11d
kube-system      kube-scheduler-node1                                1/1     Running     13 (10d ago)    11d
kube-system      nodelocaldns-jjzgq                                  1/1     Running     4 (10d ago)     11d
nonrtric         a1-sim-osc-0-7d8f49d4b8-q5mhs                       1/1     Running     0               4h59m
nonrtric         a1-sim-osc-1-7b6dd4675c-9jnzs                       1/1     Running     0               4h59m
nonrtric         a1-sim-std-0-666d947c7c-8cnrb                       1/1     Running     0               4h59m
nonrtric         a1-sim-std-1-f8778bf66-jr7bm                        1/1     Running     0               4h59m
nonrtric         a1-sim-std2-0-79cfbc9fdd-vmdkc                      1/1     Running     0               4h59m
nonrtric         a1-sim-std2-1-9fcdcbc9c-vp7xf                       1/1     Running     0               4h59m
nonrtric         capifcore-5845ccc68-bbw4x                           1/1     Running     0               4h59m
nonrtric         controlpanel-c4f5c58f8-l9x7t                        1/1     Running     0               4h59m
nonrtric         dmaapadapterservice-0                               1/1     Running     0               4h59m
nonrtric         dmaapmediatorservice-0                              1/1     Running     0               4h59m
nonrtric         helmmanager-0                                       1/1     Running     0               4h59m
nonrtric         informationservice-0                                1/1     Running     0               4h59m
nonrtric         nonrtricgateway-d46cf479c-lndt9                     1/1     Running     0               4h59m
nonrtric         odu-app-b7f7f9f56-pkcdt                             1/1     Running     0               4h59m
nonrtric         odu-app-ics-version-7df48b8d5d-g7tps                1/1     Running     0               4h59m
nonrtric         oran-nonrtric-kong-5d878fb6df-tfbzx                 2/2     Running     0               4h59m
nonrtric         oran-nonrtric-kong-init-migrations-mq5nq            0/1     Completed   0               4h59m
nonrtric         oran-nonrtric-postgresql-0                          1/1     Running     0               4h59m
nonrtric         oru-app-98d99c694-d5jj2                             1/1     Running     0               4h59m
nonrtric         policymanagementservice-0                           1/1     Running     0               4h59m
nonrtric         rappcatalogueservice-7cc75f77dc-kpdmn               1/1     Running     0               4h59m
nonrtric         rappmanager-0                                       1/1     Running     0               4h59m
nonrtric         servicemanager-566b96b854-gmrdd                     1/1     Running     0               4h59m
nonrtric         topology-7d78f99678-sh45m                           1/1     Running     0               4h59m
o1ves            o1ves-dmaap-influxdb-adapter-9555f7c6b-79kzw        1/1     Running     3 (4h47m ago)   4h49m
o1ves            o1ves-grafana-5cbb656595-9sx52                      1/1     Running     0               4h49m
o1ves            o1ves-grafana-datasource-provisioning-xgl5p         0/1     Completed   0               4h49m
o1ves            o1ves-influxdb2-0                                   1/1     Running     0               4h49m
o1ves            o1ves-influxdb2-config-22rb8                        0/1     Completed   0               4h49m
onap             onap-dcae-ves-collector-8b767f86f-4fzql             1/1     Running     0               5h1m
onap             onap-mariadb-galera-0                               2/2     Running     0               5h1m
onap             onap-message-router-0                               2/2     Running     0               5h1m
onap             onap-nengdb-init-config-job-wt8gq                   0/1     Completed   0               4h59m
onap             onap-network-name-gen-5cf7bdc944-57dx8              1/1     Running     1 (4h59m ago)   4h59m
onap             onap-policy-apex-pdp-55694fc89-z4qlz                1/1     Running     0               5h
onap             onap-policy-api-6799979dd7-zjc5d                    1/1     Running     0               5h
onap             onap-policy-clamp-ac-a1pms-ppnt-557bd5b778-bqslf    1/1     Running     0               5h
onap             onap-policy-clamp-ac-http-ppnt-99dc78cb7-ltvxv      1/1     Running     0               5h
onap             onap-policy-clamp-ac-k8s-ppnt-5599cf945b-wks5j      1/1     Running     0               5h
onap             onap-policy-clamp-ac-kserve-ppnt-584c884bf8-4rgxt   1/1     Running     0               5h
onap             onap-policy-clamp-ac-pf-ppnt-7f5b54df6d-wczh7       1/1     Running     0               5h
onap             onap-policy-clamp-runtime-acm-c48d847f5-n6q5h       1/1     Running     0               5h
onap             onap-policy-galera-config-p6djt                     0/1     Completed   0               5h
onap             onap-policy-galera-init-kth6s                       0/1     Completed   0               5h
onap             onap-policy-mariadb-0                               2/2     Running     0               5h
onap             onap-policy-pap-6c7b78f655-qdxqd                    1/1     Running     0               5h
onap             onap-sdnc-0                                         1/1     Running     0               4h59m
onap             onap-sdnc-ansible-server-78dd459b84-rxxjl           1/1     Running     0               4h59m
onap             onap-sdnc-dbinit-job-f8dw4                          0/1     Completed   0               4h59m
onap             onap-sdnc-dgbuilder-7bcf65ff78-5bzmk                1/1     Running     0               4h59m
onap             onap-sdnc-dmaap-listener-64cd9f4d5b-pc64g           1/1     Running     0               4h59m
onap             onap-sdnc-sdnrdb-init-job-vpf7m                     0/1     Completed   0               4h59m
onap             onap-sdnc-web-5cd4697dc-ds27h                       1/1     Running     0               4h59m
onap             onap-sdnrdb-coordinating-only-567cf48d7-rgnh8       2/2     Running     0               4h59m
onap             onap-sdnrdb-master-0                                1/1     Running     0               4h59m
onap             onap-strimzi-entity-operator-864cb5b89d-2xtc4       3/3     Running     0               5h1m
onap             onap-strimzi-kafka-0                                1/1     Running     0               5h2m
onap             onap-strimzi-zookeeper-0                            1/1     Running     0               5h2m
strimzi-system   strimzi-cluster-operator-64f9bf48c9-hglq7           1/1     Running     0               5h2m
```