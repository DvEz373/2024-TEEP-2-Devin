# The Installation of Near-RT RIC

- [The Installation of Near-RT RIC](#the-installation-of-near-rt-ric)
  - [Introduction](#introduction)
  - [Environment](#environment)
  - [1. Install The Docker, Kubernetes and Helm 3](#1-install-the-docker-kubernetes-and-helm-3)
    - [1.1. Open Terminal](#11-open-terminal)
    - [1.2. Become root user:](#12-become-root-user)
    - [1.3. Install Dependent Tools](#13-install-dependent-tools)
    - [1.4. Download the source code of RIC Platform](#14-download-the-source-code-of-ric-platform)
    - [1.5. Execute the Installation Script of the Docker, Kubernetes and Helm 3](#15-execute-the-installation-script-of-the-docker-kubernetes-and-helm-3)
    - [1.6. Check the Status of Kubernetes deployment](#16-check-the-status-of-kubernetes-deployment)
    - [1.7. Check the version of Docker, Kubernetes and Helm](#17-check-the-version-of-docker-kubernetes-and-helm)
  - [2. Install the Near-RT RIC Platform](#2-install-the-near-rt-ric-platform)
    - [2.1. Add the ric-common templates](#21-add-the-ric-common-templates)
    - [2.2. Edit Deployment Configuration](#22-edit-deployment-configuration)
      - [2.2.1. Modify the code of xApp Manager](#221-modify-the-code-of-xapp-manager)
        - [2.2.1.1. Modify the log-level](#2211-modify-the-log-level)
      - [2.2.2 Modify the code of A1 Mediator](#222-modify-the-code-of-a1-mediator)
        - [2.2.2.1 Modify the Log-Level](#2221-modify-the-log-level)
        - [2.2.2.2. Component Connection](#2222-component-connection)
      - [2.2.3. Modify the code of E2 Termination (Error Occured, SKIP!)](#223-modify-the-code-of-e2-termination-error-occured-skip)
      - [2.2.4. Modify the code of Subcription Manager](#224-modify-the-code-of-subcription-manager)
        - [2.2.4.1. Modify the log-level](#2241-modify-the-log-level)
        - [2.2.4.2. Component Connection](#2242-component-connection)
      - [2.2.5. Modify the code of Routing Manager](#225-modify-the-code-of-routing-manager)
        - [2.2.5.1. Routing Path Configuration](#2251-routing-path-configuration)
      - [2.2.6. Modify the code of Alarm Manager](#226-modify-the-code-of-alarm-manager)
        - [2.2.6.1 Component Connection](#2261-component-connection)
      - [2.2.7 Modify the code of O1 Mediator](#227-modify-the-code-of-o1-mediator)
        - [2.2.7.1 Component Connection](#2271-component-connection)
    - [2.3. Install nfs for InfluxDB](#23-install-nfs-for-influxdb)
    - [2.4 Execute the Installation Script of Near-RT RIC](#24-execute-the-installation-script-of-near-rt-ric)
    - [2.5. Check the Status of Near-RT RIC deployment](#25-check-the-status-of-near-rt-ric-deployment)
  - [3. Install the DMS Tool](#3-install-the-dms-tool)
    - [3.1. Install the DMS tool](#31-install-the-dms-tool)


## Introduction
This markdown guide consist of the step by step installation of Near Real Time RAN Intelligent Contoller (Near-RT RIC). This guide is based on this [HackMD](https://hackmd.io/@Whale4878/SJFSuRrca)

## Environment
- **Hardware requests:**
    - RAM : 8G RAM
    - CPU : 6 core
    - Disk : 40G
- **Installation Environment:**
    - Host : AMD Server
    - Hypervisor：-
    - VM：Ubuntu 20.04 LTS (Focal Fossa)
- **Platform Environment:**
    - Kubernetes：1.16.0
    - Helm：3.5.4
    - Docker：20.10.21

## 1. Install The Docker, Kubernetes and Helm 3
### 1.1. Open Terminal

### 1.2. Become root user:
All the commands need to be executed as root.
```bash
sudo -i
```

### 1.3. Install Dependent Tools
```bash
apt-get update

## Install the Dependent Tools
apt-get install -y git vim curl net-tools openssh-server python3-pip nfs-common
```
Output:
```bash
root@ubuntu:~# apt-get install -y git vim curl net-tools openssh-server python3-pip nfs-common
Reading package lists... Done
Building dependency tree... Done
Reading state information... Done
net-tools is already the newest version (1.60+git20181103.0eebece-1ubuntu5).
curl is already the newest version (7.81.0-1ubuntu1.15).
curl set to manually installed.
git is already the newest version (1:2.34.1-1ubuntu1.10).
git set to manually installed.
openssh-server is already the newest version (1:8.9p1-3ubuntu0.6).
vim is already the newest version (2:8.2.3995-1ubuntu2.15).
vim set to manually installed.
.
.
.
Running kernel seems to be up-to-date.

Restarting services...
Service restarts being deferred:
 /etc/needrestart/restart.d/dbus.service
 systemctl restart networkd-dispatcher.service
 systemctl restart systemd-logind.service
 systemctl restart unattended-upgrades.service
 systemctl restart user@1000.service

No containers need to be restarted.

No user sessions are running outdated binaries.

No VM guests are running outdated hypervisor (qemu) binaries on this host.
```

### 1.4. Download the source code of RIC Platform
```bash
cd ~
git clone https://gerrit.o-ran-sc.org/r/ric-plt/ric-dep -b i-release
```
[I Release URL](https://gerrit.o-ran-sc.org/r/gitweb?p=ric-plt/ric-dep.git;a=shortlog;h=refs/heads/i-release)

Output:
```bash
root@ubuntu:~# cd ~
git clone https://gerrit.o-ran-sc.org/r/ric-plt/ric-dep -b i-release
Cloning into 'ric-dep'...
remote: Total 2199 (delta 0), reused 2199 (delta 0)
Receiving objects: 100% (2199/2199), 879.62 KiB | 1.20 MiB/s, done.
Resolving deltas: 100% (906/906), done.
.
.
.
root@ubuntu:~# ll
total 32
drwx------  5 root root 4096 Mar 18 15:39 ./
drwxr-xr-x 19 root root 4096 Mar 15 08:22 ../
-rw-------  1 root root  210 Mar 17 03:33 .bash_history
-rw-r--r--  1 root root 3106 Oct 15  2021 .bashrc
-rw-r--r--  1 root root  161 Jul  9  2019 .profile
drwxr-xr-x 11 root root 4096 Mar 18 15:39 ric-dep/
drwx------  3 root root 4096 Mar 15 08:27 snap/
drwx------  2 root root 4096 Mar 15 08:27 .ssh/
-rw-r--r--  1 root root    0 Mar 15 14:27 .sudo_as_admin_successful
```

### 1.5. Execute the Installation Script of the Docker, Kubernetes and Helm 3

1. Add repository alternative:
    ```bash
    nano root/etc/apt/sources.list
    ```
    adding to source: `deb https://mirrors.aliyun.com/kubernetes/apt kubernetes-xenial main`
2. Continue the command:
    ```bash
    curl https://mirrors.aliyun.com/kubernetes/apt/doc/apt-key.gpg | gpg --dearmor > /usr/share/keyrings/EXAMPLE.gpg

    echo "deb [signed-by=/usr/share/keyrings/EXAMPLE.gpg] https://mirrors.aliyun.com/kubernetes/apt stable main" || sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

    sudo apt-get update

    cd ric-dep/bin

    ./install_k8s_and_helm.sh
    ```
    Output:
    ```bash
    root@ubuntu:~# cd ric-dep/bin
    ./install_k8s_and_helm.sh
    + KUBEV=1.16.0
    + KUBECNIV=0.7.5
    + HELMV=3.5.4
    + DOCKERV=20.10.21
    + echo running ./install_k8s_and_helm.sh
    running ./install_k8s_and_helm.sh
    + getopts :k:d:e:n:c o
    + [[ 3.5.4 == 2.* ]]
    + set -x
    + export DEBIAN_FRONTEND=noninteractive
    + DEBIAN_FRONTEND=noninteractive
    ++ hostname -I
    ++ hostname
    + echo '192.168.0.155  ubuntu'
    + printenv
    SHELL=/bin/bash
    SUDO_GID=1000
    SUDO_COMMAND=/bin/bash
    SUDO_USER=ubuntu
    PWD=/root/ric-dep/bin
    LOGNAME=root
    HOME=/root
    LANG=en_US.UTF-8
    .
    .
    .
    + echo '> waiting for 0/8 pods running in namespace [kube-system] with keyword [Running]'
    > waiting for 0/8 pods running in namespace [kube-system] with keyword [Running]
    + '[' 0 -lt 8 ']'
    + sleep 5
    .
    .
    .
    + '[' '' == teep-ric ']'
    + echo 'Done with master node setup'
    Done with master node setup
    + [[ ! -z '' ]]
    + [[ ! -z '' ]]
    + [[ ! -z '' ]]
    + [[ 1 -gt 100 ]]
    + [[ 1 -gt 100 ]]
    ```

### 1.6. Check the Status of Kubernetes deployment
```bash
kubectl get pods -A
```

Output:
```bash
root@teep-ric:~/ric-dep/bin# kubectl get pods -A
NAMESPACE     NAME                               READY   STATUS    RESTARTS   AGE
kube-system   coredns-787d4945fb-5f5zs           1/1     Running   0          39s
kube-system   coredns-787d4945fb-fx56v           1/1     Running   0          39s
kube-system   etcd-teep-ric                      1/1     Running   4          53s
kube-system   kube-apiserver-teep-ric            1/1     Running   3          53s
kube-system   kube-controller-manager-teep-ric   1/1     Running   3          52s
kube-system   kube-flannel-ds-m6slx              1/1     Running   0          39s
kube-system   kube-proxy-7m487                   1/1     Running   0          39s
kube-system   kube-scheduler-teep-ric            1/1     Running   3          53s
```

### 1.7. Check the version of Docker, Kubernetes and Helm
It should be:
Name | Version | command |
 ----------- | ----------- | ----------- |
Helm | 3.5.4 | helm version
Kubernetes | 1.16.0	| kubectl version
Docker | 20.10.21 | docker version

* Check Helm and Kubernetes version
```bash
helm version
kubectl version
```
* Check Docker version
```bash
docker version
```

## 2. Install the Near-RT RIC Platform
### 2.1. Add the ric-common templates
```bash
./install_common_templates_to_helm.sh
```

Output:
```bash
root@teep-ric:~/ric-dep/bin# ./install_common_templates_to_helm.sh
Installing servecm (Chart Manager) and common templates to helm3
Installed plugin: servecm
/root/.cache/helm/repository
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100 15.0M  100 15.0M    0     0  3460k      0  0:00:04  0:00:04 --:--:-- 4315k
linux-386/
linux-386/chartmuseum
linux-386/LICENSE
linux-386/README.md
servecm not yet running. sleeping for 2 seconds
nohup: appending output to 'nohup.out'
servcm up and running
/root/.cache/helm/repository
Successfully packaged chart and saved it to: /tmp/ric-common-3.3.2.tgz
Error: no repositories configured
"local" has been added to your repositories
checking that ric-common templates were added
NAME                    CHART VERSION   APP VERSION     DESCRIPTION
local/ric-common        3.3.2                           Common templates for inclusion in other charts
```

Command:
```bash
./setup-ric-common-template
```

Output:
```bash
root@teep-ric:~/ric-dep/bin# ./setup-ric-common-template
Cloning into '../dep'...
remote: Counting objects: 318, done
remote: Finding sources: 100% (6989/6989)
remote: Total 6989 (delta 2787), reused 6952 (delta 2787)
Receiving objects: 100% (6989/6989), 3.81 MiB | 20.00 KiB/s, done.
Resolving deltas: 100% (2787/2787), done.
.
.
.
+ NONRTRIC_COMMON_CHART_VERSION=2.0.0
+ helm package -d /tmp /root/ric-dep/dep/bin/../ric-common/Common-Template/helm/nonrtric-common
Successfully packaged chart and saved it to: /tmp/nonrtric-common-2.0.0.tgz
+ cp /tmp/nonrtric-common-2.0.0.tgz /root/.cache/helm/repository/local/
+ helm repo index /root/.cache/helm/repository/local/
+ helm repo remove local
"local" has been removed from your repositories
+ helm repo add local http://127.0.0.1:8879/charts
"local" has been added to your repositories
```

### 2.2. Edit Deployment Configuration
#### 2.2.1. Modify the code of xApp Manager
##### 2.2.1.1. Modify the log-level
command:
```bash
sudo nano ~/ric-dep/helm/appmgr/resources/appmgr.yaml
```
Add loglevel “DEBUG”：<br>
Add loglevel : 4
```bash
"xapp":
  #Namespace to install xAPPs
  "namespace": __XAPP_NAMESPACE__
  "tarDir": "/tmp"
  "schema": "descriptors/schema.json"
  "config": "config/config-file.json"
  "tmpConfig": "/tmp/config-file.json"
  "loglevel" :  4  
```

#### 2.2.2 Modify the code of A1 Mediator
##### 2.2.2.1 Modify the Log-Level
Step 1：Modify the loglevel.txt section

command:
```bash
sudo nano ~/ric-dep/helm/a1mediator/templates/config.yaml
```

Change `log-level: {{ .Values.loglevel }}` to `log-level: {{ .Values.a1mediator.loglevel }}`

Output:
```bash
  loglevel.txt: |
    log-level: {{ .Values.a1mediator.loglevel }}
```

Step 2：Change loglevel from INFO to DEBUG & change Component Connection

command :
```bash
sudo nano ~/ric-dep/helm/a1mediator/values.yaml
```

Change `loglevel from INFO` to `DEBUG & add a1ei: ecs_ip_port: "http://<ecs_host>:<ecs_port>"`

Output:
```bash
  rmr_timeout_config:
    a1_rcv_retry_times: 20
    ins_del_no_resp_ttl: 5
    ins_del_resp_ttl: 10
  loglevel: "DEBUG"
  a1ei:
    ecs_ip_port: "http://<ecs_host>:<ecs_port>"
```

##### 2.2.2.2. Component Connection
Step 1: Add ENV for A1EI
```bash
sudo nano ~/ric-dep/helm/a1mediator/templates/env.yaml
```
Add `ECS_SERVICE_HOST: {{ .Values.a1mediator.a1ei.ecs_ip_port }}`

Output:
```bash
  INSTANCE_DELETE_NO_RESP_TTL: "{{ .Values.a1mediator.rmr_timeout_config.ins_del_no_resp_ttl }}"
  INSTANCE_DELETE_RESP_TTL: "{{ .Values.a1mediator.rmr_timeout_config.ins_del_resp_ttl }}"
  CONFIG_MAP_NAME: "/opt/route/loglevel.txt"
  ECS_SERVICE_HOST: {{ .Values.a1mediator.a1ei.ecs_ip_port }}
```

#### 2.2.3. Modify the code of E2 Termination (Error Occured, SKIP!)

#### 2.2.4. Modify the code of Subcription Manager
##### 2.2.4.1. Modify the log-level
Change level from 3(Info) to 4(Debug)：
```bash
sudo nano ~/ric-dep/helm/submgr/templates/configmap.yaml
```

Output:
```bash
 submgrcfg: |
    "local":
      "host": ":8080"
    "logger":
      "level": 4
    "rmr":
      "protPort" : "tcp:4560"
      "maxSize": 8192
      "numWorkers": 1
```

##### 2.2.4.2. Component Connection
Step 1：Add new port for subscription in service file
```bash
sudo nano ~/ric-dep/helm/submgr/templates/service-http.yaml
```
Add Line 11 to 14:
```bash
spec:
  selector:
    app: {{ include "common.namespace.platform" . }}-{{ include "common.name.submgr" . }}
    release: {{ .Release.Name }}
  clusterIP: None
  ports:
  - name: http
    port: {{ include "common.serviceport.submgr.http" . }}
    protocol: TCP
    targetPort: http
  - name: subscription
    port: 8088
    protocol: TCP
    targetPort: 8088
```
Step 2：Add new port for subscription in deployment file
```bash
sudo nano ~/ric-dep/helm/submgr/templates/deployment.yaml
```
Add Line from 9 to 11:
```bash
containers:
          ...
          envFrom:
            - configMapRef:
                name: {{ include "common.configmapname.submgr" . }}-env
            - configMapRef:
                name: {{ include "common.configmapname.dbaas" . }}-appconfig
          ports:
            - name: subscription
              containerPort: 8088
              protocol: TCP
	        ...
```

#### 2.2.5. Modify the code of Routing Manager
##### 2.2.5.1. Routing Path Configuration
Add A1EI Msgtype and A1EI Routes：
```bash
sudo nano ~/ric-dep/helm/rtmgr/templates/config.yaml
```
Add Line from 3 to 7 & 12 to 13:
```bash
       "messagetypes": [
          ...
          "A1_EI_QUERY_ALL=20013",
          "A1_EI_QUERY_ALL_RESP=20014",
          "A1_EI_CREATE_JOB=20015",
          "A1_EI_CREATE_JOB_RESP=20016",
          "A1_EI_DATA_DELIVERY=20017",
          ]
          ...
      "PlatformRoutes": [
         ...
         { 'messagetype': 'A1_EI_QUERY_ALL','senderendpoint': '', 'subscriptionid': -1, 'endpoint': 'A1MEDIATOR', 'meid': ''},
         { 'messagetype': 'A1_EI_CREATE_JOB','senderendpoint': '', 'subscriptionid': -1, 'endpoint': 'A1MEDIATOR', 'meid': ''},
          ]
```

#### 2.2.6. Modify the code of Alarm Manager
##### 2.2.6.1 Component Connection
Step 1：Change `controls.promAlertManager.address`
```bash
sudo nano ~/ric-dep/helm/alarmmanager/templates/configmap.yaml
```
change `cpro-alertmanager:80` to `r4-infrastructure-prometheus-alertmanager:80`:
```bash
controls": {
        "promAlertManager": {
          "address": "r4-infrastructure-prometheus-alertmanager:80",
          "baseUrl": "api/v2",
          "schemes": "http",
          "alertInterval": 30000
        },
```

Step 2：Add `livenessProbe` and `readinessProbe`
```bash
sudo nano ~/ric-dep/helm/alarmmanager/templates/deployment.yaml
```

Add Line from 10 to 25:
```bash
    spec:
      hostname: {{ include "common.name.alarmmanager" . }}
      imagePullSecrets:
        - name: {{ include "common.dockerregistry.credential" $imagectx }}
      serviceAccountName: {{ include "common.serviceaccountname.alarmmanager" . }}
      containers:
        - name: {{ include "common.containername.alarmmanager" . }}
          image: {{ include "common.dockerregistry.url" $imagectx }}/{{ .Values.alarmmanager.image.name }}:{{ $imagetag }}
          imagePullPolicy: {{ include "common.dockerregistry.pullpolicy" $pullpolicyctx }}
          readinessProbe:
            failureThreshold: 3
            httpGet:
              path: ric/v1/health/ready
              port: 8080
              scheme: HTTP
            initialDelaySeconds: 5
            periodSeconds: 15
          livenessProbe:
            failureThreshold: 3
            httpGet:
              path: ric/v1/health/alive
              port: 8080
              scheme: HTTP
            initialDelaySeconds: 5
            periodSeconds: 15
          ...
```

#### 2.2.7 Modify the code of O1 Mediator
##### 2.2.7.1 Component Connection
Add `livenessProbe` and `readinessProbe`:
```bash
sudo nano ~/ric-dep/helm/o1mediator/templates/deployment.yaml
```

Add Line from 10 to 29:
```bash
spec:
      hostname: {{ include "common.name.o1mediator" . }}
      imagePullSecrets:
        - name: {{ include "common.dockerregistry.credential" $imagectx }}
      serviceAccountName: {{ include "common.serviceaccountname.o1mediator" . }}
      containers:
        - name: {{ include "common.containername.o1mediator" . }}
          image: {{ include "common.dockerregistry.url" $imagectx }}/{{ .Values.o1mediator.image.name }}:{{ .Values.o1mediator.image.tag }}
          imagePullPolicy: {{ include "common.dockerregistry.pullpolicy" $pullpolicyctx }}
          livenessProbe:
            failureThreshold: 3
            httpGet:
              path: ric/v1/health/alive
              port: 8080
              scheme: HTTP
            initialDelaySeconds: 5
            periodSeconds: 15
            successThreshold: 1
            timeoutSeconds: 1
          readinessProbe:
            failureThreshold: 3
            httpGet:
              path: ric/v1/health/ready
              port: 8080
              scheme: HTTP
            initialDelaySeconds: 5
            periodSeconds: 15
            successThreshold: 1
            timeoutSeconds: 1
          ...
```

### 2.3. Install nfs for InfluxDB
```bash
kubectl create ns ricinfra
helm repo add stable https://charts.helm.sh/stable
helm install nfs-release-1 stable/nfs-server-provisioner --namespace ricinfra 
kubectl patch storageclass nfs -p '{"metadata": {"annotations":{"storageclass.kubernetes.io/is-default-class":"true"}}}'
sudo apt install nfs-common
```

Output:
```bash
root@teep-ric:~# kubectl create ns ricinfra
all nfs-release-1 stable/nfs-server-provisioner --namespace ricinfra
kubectl patch storageclass nfs -p '{"metadata": {"annotations":{"storageclass.kubernetes.io/is-default-class":"true"}}}'
sudo apt install nfs-commonnamespace/ricinfra created
root@teep-ric:~# helm repo add stable https://charts.helm.sh/stable
"stable" has been added to your repositories
root@teep-ric:~# helm install nfs-release-1 stable/nfs-server-provisioner --namespace ricinfra
WARNING: This chart is deprecated
NAME: nfs-release-1
LAST DEPLOYED: Tue Apr  2 11:08:00 2024
.
.
.
root@teep-ric:~# kubectl patch storageclass nfs -p '{"metadata": {"annotations":{"storageclass.kubernetes.io/is-default-class":"true"}}}'
storageclass.storage.k8s.io/nfs patched
```

### 2.4 Execute the Installation Script of Near-RT RIC
Find your IP of VM：
```bash
ip a
```

output:
```bash
root@teep-ric:~# ip a
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group default qlen 1000
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
    inet 127.0.0.1/8 scope host lo
       valid_lft forever preferred_lft forever
    inet6 ::1/128 scope host
       valid_lft forever preferred_lft forever
2: ens18: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc fq_codel state UP group default qlen 1000
    link/ether b6:64:fb:a9:11:fe brd ff:ff:ff:ff:ff:ff
    altname enp0s18
    inet 192.168.0.212/24 brd 192.168.0.255 scope global noprefixroute ens18
       valid_lft forever preferred_lft forever
    inet6 fe80::8afa:e23b:85c6:4d3e/64 scope link noprefixroute
       valid_lft forever preferred_lft forever
3: docker0: <NO-CARRIER,BROADCAST,MULTICAST,UP> mtu 1500 qdisc noqueue state DOWN group default
    link/ether 02:42:da:f3:d4:ee brd ff:ff:ff:ff:ff:ff
    inet 172.17.0.1/16 brd 172.17.255.255 scope global docker0
       valid_lft forever preferred_lft forever
4: flannel.1: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1450 qdisc noqueue state UNKNOWN group default
    link/ether ea:49:e0:af:53:f0 brd ff:ff:ff:ff:ff:ff
    inet 10.244.0.0/32 scope global flannel.1
       valid_lft forever preferred_lft forever
    inet6 fe80::e849:e0ff:feaf:53f0/64 scope link
       valid_lft forever preferred_lft forever
```

Modify the IP of RIC and AUX:
```bash
sudo nano ~/ric-dep/RECIPE_EXAMPLE/example_recipe_oran_i_release.yaml
```

output:
```bash
# Change the namespaces using the following options
#  namespace:
#    aux: ricaux
#    platform: ricplt
#    xapp: ricxapp
#    infra: ricinfra

# ricip should be the ingress controller listening IP for the platform cluster
# auxip should be the ingress controller listening IP for the AUX cluster
extsvcplt:
  ricip: "192.168.0.212"
  auxip: "192.168.0.212"

```

Deploy the RIC Platform：
```bash
cd ~/ric-dep/bin
./install -f ../RECIPE_EXAMPLE/example_recipe_oran_i_release.yaml -c "jaegeradapter influxdb"
```
Output:
```bash
root@teep-ric:~/ric-dep/bin# ./install -f ../RECIPE_EXAMPLE/example_recipe_oran_i_release.yaml -c "jaegeradapter influxdb"
namespace/ricplt created
namespace/ricxapp created
nfs storage exist
Deploying RIC infra components [infrastructure dbaas appmgr rtmgr e2mgr e2term a1mediator submgr vespamgr o1mediator alarmmanager jaegeradapter influxdb]
configmap/ricplt-recipe created
Add cluster roles
Hang tight while we grab the latest from your chart repositories...
...Successfully got an update from the "local" chart repository
...Successfully got an update from the "stable" chart repository
Update Complete. ⎈Happy Helming!⎈
Saving 7 charts
.
.
.
InfluxDB 2 is deployed as a StatefulSet on your cluster.

You can access it by using the service name: r4-influxdb-influxdb2

To retrieve the password for the 'admin' user:

  echo $(kubectl get secret r4-influxdb-influxdb2-auth -o "jsonpath={.data['admin-password']}" --namespace ricplt | base64 --decode)

Note: with enabled persistence, admin password is only set once during the initial deployment. The password is not changed when InfluxDB 2 is re-deployed with different password.
```

### 2.5. Check the Status of Near-RT RIC deployment
* Results similar to the output shown below indicate a complete and successful deployment, all are either “Completed” or “Running”, and that none are “Error”, “Pending”, “Evicted”,or “ImagePullBackOff”.
* The status of pods “PodInitializing” & “Init” & “ContainerCreating” mean that the pods are creating now, you need to wait for deploying.
```bash
kubectl get pods -A
```
Output:
```bash
root@teep-ric:~/ric-dep/bin# kubectl get pods -A
NAMESPACE     NAME                                                         READY   STATUS      RESTARTS   AGE
kube-system   coredns-5644d7b6d9-88pl2                                     1/1     Running     0          39m
kube-system   coredns-5644d7b6d9-v9pmm                                     1/1     Running     0          39m
kube-system   etcd-teep-ric                                                1/1     Running     0          37m
kube-system   kube-apiserver-teep-ric                                      1/1     Running     0          37m
kube-system   kube-controller-manager-teep-ric                             1/1     Running     0          38m
kube-system   kube-flannel-ds-dp2hm                                        1/1     Running     0          39m
kube-system   kube-proxy-6zz8v                                             1/1     Running     0          39m
kube-system   kube-scheduler-teep-ric                                      1/1     Running     0          38m
ricinfra      deployment-tiller-ricxapp-68f777c4d4-xw2m4                   1/1     Running     0          12m
ricinfra      nfs-release-1-nfs-server-provisioner-0                       1/1     Running     0          13m
ricinfra      tiller-secret-generator-hsttk                                0/1     Completed   0          12m
ricplt        deployment-ricplt-a1mediator-7d5b85ff7d-nnlmf                1/1     Running     0          10m
ricplt        deployment-ricplt-alarmmanager-5b797c9484-klnvj              1/1     Running     0          9m17s
ricplt        deployment-ricplt-appmgr-77986c9cbb-cxhcr                    1/1     Running     0          11m
ricplt        deployment-ricplt-e2mgr-78c987559f-pcz7j                     1/1     Running     0          10m
ricplt        deployment-ricplt-e2term-alpha-5dc768bcb7-smk8w              1/1     Running     0          10m
ricplt        deployment-ricplt-jaegeradapter-76ddbf9c9-ljhgp              1/1     Running     0          9m
ricplt        deployment-ricplt-rtmgr-78f768474-8bs4p                      1/1     Running     6          11m
ricplt        deployment-ricplt-submgr-547965db4c-7rhct                    1/1     Running     0          10m
ricplt        deployment-ricplt-vespamgr-84f7d87dfb-2tr2v                  1/1     Running     0          9m49s
ricplt        r4-influxdb-influxdb2-0                                      1/1     Running     0          8m52s
ricplt        r4-infrastructure-kong-7995f4679b-pcdkt                      2/2     Running     2          12m
ricplt        r4-infrastructure-prometheus-alertmanager-5798b78f48-5wssd   2/2     Running     0          12m
ricplt        r4-infrastructure-prometheus-server-c8ddcfdf5-bftkp          1/1     Running     0          12m
ricplt        statefulset-ricplt-dbaas-server-0                            1/1     Running     0          11m
```

## 3. Install the DMS Tool
### 3.1. Install the DMS tool
Prepare source code：
```bash
docker run --rm -u 0 -it -d -p 8090:8080 -e DEBUG=1 -e STORAGE=local -e STORAGE_LOCAL_ROOTDIR=/chart -v $(pwd)/charts:/charts chartmuseum/chartmuseum:latest
export CHART_REPO_URL=http://0.0.0.0:8090
git clone https://gerrit.o-ran-sc.org/r/ric-plt/appmgr -b i-release
```
Output:
```bash
root@teep-ric:~/ric-dep/bin# docker run --rm -u 0 -it -d -p 8090:8080 -e DEBUG=1 -e STORAGE=local -e STORAGE_LOCAL_ROOTDIR=/chart -v $(pwd)/charts:/charts chartmuseum/chartmuseum:latest
Unable to find image 'chartmuseum/chartmuseum:latest' locally
latest: Pulling from chartmuseum/chartmuseum
596ba82af5aa: Pull complete
97cda76ac4f8: Pull complete
7cd1b4b8c77a: Pull complete
Digest: sha256:7fb4cd65d68978b1280f39cedc8c4db8c96efe6f622160a109b425a95098615f
Status: Downloaded newer image for chartmuseum/chartmuseum:latest
e9995461ba3d653d45f6c3ffd2dad079bc8c54edf3febd1aeafa9bdad0bed4c7
root@teep-ric:~/ric-dep/bin# export CHART_REPO_URL=http://0.0.0.0:8090
root@teep-ric:~/ric-dep/bin# cd ~
root@teep-ric:~# git clone https://gerrit.o-ran-sc.org/r/ric-plt/appmgr -b i-release
Cloning into 'appmgr'...
remote: Counting objects: 13, done
remote: Total 790 (delta 0), reused 790 (delta 0)
```

Install DMS tool:
```bash
cd appmgr/xapp_orchestrater/dev/xapp_onboarder
apt-get install python3-pip
pip3 uninstall xapp_onboarder
pip3 install ./
chmod 755 /usr/local/bin/dms_cli
ls -la /usr/local/lib/ptyhon3.8
chmod -R 755 /usr/local/lib/python3.8
```
Output:
```bash
root@teep-ric:~# cd appmgr/xapp_orchestrater/dev/xapp_onboarder
root@teep-ric:~/appmgr/xapp_orchestrater/dev/xapp_onboarder# apt-get install python3-pip
Reading package lists... Done
Building dependency tree
Reading state information... Done
python3-pip is already the newest version (20.0.2-5ubuntu1.10).
0 upgraded, 0 newly installed, 0 to remove and 82 not upgraded.
root@teep-ric:~/appmgr/xapp_orchestrater/dev/xapp_onboarder# pip3 uninstall xapp_onboarder
WARNING: Skipping xapp-onboarder as it is not installed.
root@teep-ric:~/appmgr/xapp_orchestrater/dev/xapp_onboarder#
.
.
.
root@teep-ric:~/appmgr/xapp_orchestrater/dev/xapp_onboarder# pip3 install ./
Processing /root/appmgr/xapp_orchestrater/dev/xapp_onboarder
Requirement already satisfied: Click==7.0 in /usr/lib/python3/dist-packages (from xapp-onboarder==1.0.0) (7.0)
Collecting Flask==1.1.1
  Downloading Flask-1.1.1-py2.py3-none-any.whl (94 kB)
     |████████████████████████████████| 94 kB 2.7 MB/s
.
.
.
root@teep-ric:~/appmgr/xapp_orchestrater/dev/xapp_onboarder# pip3 install ./
Processing /root/appmgr/xapp_orchestrater/dev/xapp_onboarder
Requirement already satisfied: Click==7.0 in /usr/lib/python3/dist-packages (from xapp-onboarder==1.0.0) (7.0)
Requirement already satisfied: Flask==1.1.1 in /usr/local/lib/python3.8/dist-packages (from xapp-onboarder==1.0.0) (1.1.1)
Requirement already satisfied: Jinja2==2.11.1 in /usr/local/lib/python3.8/dist-packages (from xapp-onboarder==1.0.0) (2.11.1)
Requirement already satisfied: MarkupSafe==1.1.1 in /usr/local/lib/python3.8/dist-packages (from xapp-onboarder==1.0.0) (1.1.1)
Requirement already satisfied: PyYAML==5.3 in /usr/local/lib/python3.8/dist-packages (from xapp-onboarder==1.0.0) (5.3)
Requirement already satisfied: Werkzeug==0.16.1 in /usr/local/lib/python3.8/dist-packages (from xapp-onboarder==1.0.0) (0.16.1)
Requirement already satisfied: aniso8601==8.0.0 in /usr/local/lib/python3.8/dist-packages (from xapp-onboarder==1.0.0) (8.0.0)
Requirement already satisfied: attrs==19.3.0 in /usr/local/lib/python3.8/dist-packages (from xapp-onboarder==1.0.0) (19.3.0)
Requirement already satisfied: certifi==2019.11.28 in /usr/lib/python3/dist-packages (from xapp-onboarder==1.0.0) (2019.11.28)
Requirement already satisfied: chardet==3.0.4 in /usr/lib/python3/dist-packages (from xapp-onboarder==1.0.0) (3.0.4)
Requirement already satisfied: fire==0.2.1 in /usr/local/lib/python3.8/dist-packages (from xapp-onboarder==1.0.0) (0.2.1)
Requirement already satisfied: flask-restplus==0.13.0 in /usr/local/lib/python3.8/dist-packages (from xapp-onboarder==1.0.0) (0.13.0)
Requirement already satisfied: idna==2.9 in /usr/local/lib/python3.8/dist-packages (from xapp-onboarder==1.0.0) (2.9)
Requirement already satisfied: importlib-metadata==1.5.0 in /usr/local/lib/python3.8/dist-packages (from xapp-onboarder==1.0.0) (1.5.0)
Requirement already satisfied: itsdangerous==1.1.0 in /usr/local/lib/python3.8/dist-packages (from xapp-onboarder==1.0.0) (1.1.0)
Requirement already satisfied: jsonschema==3.2.0 in /usr/local/lib/python3.8/dist-packages (from xapp-onboarder==1.0.0) (3.2.0)
Requirement already satisfied: pyrsistent==0.15.7 in /usr/local/lib/python3.8/dist-packages (from xapp-onboarder==1.0.0) (0.15.7)
Requirement already satisfied: pytz==2019.3 in /usr/lib/python3/dist-packages (from xapp-onboarder==1.0.0) (2019.3)
Requirement already satisfied: requests==2.23.0 in /usr/local/lib/python3.8/dist-packages (from xapp-onboarder==1.0.0) (2.23.0)
Requirement already satisfied: six==1.14.0 in /usr/lib/python3/dist-packages (from xapp-onboarder==1.0.0) (1.14.0)
Requirement already satisfied: termcolor==1.1.0 in /usr/local/lib/python3.8/dist-packages (from xapp-onboarder==1.0.0) (1.1.0)
Requirement already satisfied: urllib3==1.25.8 in /usr/lib/python3/dist-packages (from xapp-onboarder==1.0.0) (1.25.8)
Requirement already satisfied: zipp==3.0.0 in /usr/local/lib/python3.8/dist-packages (from xapp-onboarder==1.0.0) (3.0.0)
Requirement already satisfied: setuptools in /usr/lib/python3/dist-packages (from jsonschema==3.2.0->xapp-onboarder==1.0.0) (45.2.0)
```
