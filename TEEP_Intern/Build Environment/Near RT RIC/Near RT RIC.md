# Near RT RIC (OSC RIC)
## Introduction
This markdown guide consist of the step by step installation of Near Real Time RAN Intelligent Contoller (Near-RT RIC).
Reference:
https://docs.o-ran-sc.org/projects/o-ran-sc-ric-plt-ric-dep/en/latest/installation-guides.html

## Overview
This section explains the installation of Near Realtime RAN Intelligent Controller Platform only.

## Prerequisites
The steps below assume a clean installation of Ubuntu 20.04 (no k8s, no docker, no helm)

## Environment
Here is the information in a table format:

| **Category**             | **Details**              |
|--------------------------|--------------------------|
| **Hardware Requests**    |                          |
| - RAM                    | 8G RAM                   |
| - CPU                    | 12 core                   |
| - Disk                   | 40G                      |
| **Installation Environment** |                          |
| - Host                   | Intel Server               |
| - Hypervisor             | -                        |
| - VM                     | Ubuntu 20.04 LTS (Focal Fossa) |
| **Platform Environment** |                          |
| - Kubernetes             | 1.28.11                   |
| - Helm                   | 3.14.4                    |
| - Docker                 | 20.10.21                 |

## Initial Prerequisite
### Login as Root
```bash
sudo -i
```

## Installing Near Realtime RIC in RIC Cluster
After the Kubernetes cluster is installed, the next step is to install the (Near Realtime) RIC Platform.

## Getting and Preparing Deployment Scripts
Clone the ric-plt/dep git repository that has deployment scripts and support files on the target VM.
```
git clone "https://gerrit.o-ran-sc.org/r/ric-plt/ric-dep"
```

## Deploying the Infrastructure and Platform Groups
Use the scripts below to install kubernetes, kubernetes-CNI, helm and docker on a fresh Ubuntu 20.04 installation. Note that since May 2022 there’s no need for anything form the repo it/dep anymore.
```
# install kubernetes, kubernetes-CNI, helm and docker
cd ric-dep/bin
./install_k8s_and_helm.sh

# install chartmuseum into helm and add ric-common templates
./install_common_templates_to_helm.sh
```
After the recipes are edited and helm started, the Near Realtime RIC platform is ready to be deployed, but first update the deployment recipe as per instructions in the next section.

## Modify the deployment recipe
Edit the recipe files ./RECIPE_EXAMPLE/example_recipe_latest_stable.yaml (which is a softlink that points to the latest release version). “example_recipe_latest_unstable.yaml points to the latest example file that is under current development.
```
extsvcplt:
  ricip: "192.168.0.16"
  auxip: "192.168.0.16"
```

## Installing the RIC
After updating the recipe you can deploy the RIC with the command below. Note that generally use the latest recipe marked stable or one from a specific release.
```
cd ~/ric-dep/bin
./install -f ../RECIPE_EXAMPLE/example_recipe_oran_i_release.yaml
```

## Checking the Deployment Status
Now check the deployment status after a short wait. Results similar to the output shown below indicate a complete and successful deployment. Check the STATUS column from both kubectl outputs to ensure that all are either “Completed” or “Running”, and that none are “Error” or “ImagePullBackOff”.
```
kubectl get pods -A
```
output:
```bash
root@ubuntu:~/ric-dep/bin# kubectl get pods -A
NAMESPACE      NAME                                                         READY   STATUS      RESTARTS      AGE
kube-flannel   kube-flannel-ds-ldh2z                                        1/1     Running     0             39m
kube-system    coredns-5dd5756b68-cr4gf                                     1/1     Running     0             39m
kube-system    coredns-5dd5756b68-ff6wt                                     1/1     Running     0             39m
kube-system    etcd-ubuntu                                                  1/1     Running     0             39m
kube-system    kube-apiserver-ubuntu                                        1/1     Running     0             39m
kube-system    kube-controller-manager-ubuntu                               1/1     Running     0             39m
kube-system    kube-proxy-b2dfg                                             1/1     Running     0             39m
kube-system    kube-scheduler-ubuntu                                        1/1     Running     0             39m
ricinfra       deployment-tiller-ricxapp-676dfd8664-ddcfh                   1/1     Running     0             3m18s
ricinfra       tiller-secret-generator-4z2nl                                0/1     Completed   0             3m18s
ricplt         deployment-ricplt-a1mediator-64fd4bf64-l89fg                 1/1     Running     0             113s
ricplt         deployment-ricplt-alarmmanager-7d47d8f4d4-9hnrf              1/1     Running     0             56s
ricplt         deployment-ricplt-appmgr-5bdd7cbb54-k54wx                    1/1     Running     0             2m49s
ricplt         deployment-ricplt-e2mgr-b988db566-gqs4z                      1/1     Running     0             2m21s
ricplt         deployment-ricplt-e2term-alpha-75d8ccb646-bttdf              0/1     Running     0             2m7s
ricplt         deployment-ricplt-o1mediator-76c4646878-zrn2d                1/1     Running     0             71s
ricplt         deployment-ricplt-rtmgr-6556c5bc7b-ggxd5                     1/1     Running     2 (55s ago)   2m35s
ricplt         deployment-ricplt-submgr-599754c984-qlsf8                    1/1     Running     0             99s
ricplt         deployment-ricplt-vespamgr-786666549b-clvlv                  1/1     Running     0             85s
ricplt         r4-infrastructure-kong-5986fc7965-qrvsd                      2/2     Running     0             3m18s
ricplt         r4-infrastructure-prometheus-alertmanager-64f9876d6d-9sf5f   2/2     Running     0             3m18s
ricplt         r4-infrastructure-prometheus-server-bcc8cc897-prdfk          1/1     Running     0             3m18s
ricplt         statefulset-ricplt-dbaas-server-0                            1/1     Running     0             3m3s
```

## Checking Container Health
Check the health of the application manager platform component by querying it via the ingress controller using the following command.
```
curl -v http://localhost:32080/appmgr/ric/v1/health/ready
```
output:
```
root@ubuntu:~/ric-dep/bin# curl -v http://localhost:32080/appmgr/ric/v1/health/ready
*   Trying 127.0.0.1:32080...
* TCP_NODELAY set
* Connected to localhost (127.0.0.1) port 32080 (#0)
> GET /appmgr/ric/v1/health/ready HTTP/1.1
> Host: localhost:32080
> User-Agent: curl/7.68.0
> Accept: */*
>
* Mark bundle as not supporting multiuse
< HTTP/1.1 404 Not Found
< Date: Mon, 08 Jul 2024 07:25:31 GMT
< Content-Type: application/json; charset=utf-8
< Connection: keep-alive
< Content-Length: 103
< X-Kong-Response-Latency: 0
< Server: kong/3.6.1
< X-Kong-Request-Id: 6bfdf8292c280e27d87a072f66e7ae73
<
{
  "message":"no Route matched with those values",
  "request_id":"6bfdf8292c280e27d87a072f66e7ae73"
* Connection #0 to host localhost left intact
}
```

## RIC Application
### xApp Onboarding using CLI tool called dms_cli
xApp onboarder provides a cli tool called dms_cli to fecilitate xApp onboarding service to operators. It consumes the xApp descriptor and optionally additional schema file, and produces xApp helm charts.

Below are the sequence of steps to onboard, install and uninstall the xApp.

1. Step 1: (OPTIONAL ) Install python3 and its dependent libraries, if not installed.

2. Step 2: Prepare the xApp descriptor and an optional schema file. xApp descriptor file is a config file that defines the behavior of the xApp. An optional schema file is a JSON schema file that validates the self-defined parameters.

3. Step 3: Before any xApp can be deployed, its Helm chart must be loaded into this private Helm repository.
```
#Create a local helm repository with a port other than 8080 on host
docker run --rm -u 0 -it -d -p 8090:8080 -e DEBUG=1 -e STORAGE=local -e STORAGE_LOCAL_ROOTDIR=/charts -v $(pwd)/charts:/charts chartmuseum/chartmuseum:latest
```
4. Step 4: Set up the environment variables for CLI connection using the same port as used above.
```
#Set CHART_REPO_URL env variable
export CHART_REPO_URL=http://0.0.0.0:8090
```
5. Step 5: Install dms_cli tool
```
#Git clone appmgr
git clone "https://gerrit.o-ran-sc.org/r/ric-plt/appmgr"

#Change dir to xapp_onboarder
cd appmgr/xapp_orchestrater/dev/xapp_onboarder

#If pip3 is not installed, install using the following command
yum install python3-pip

#In case dms_cli binary is already installed, it can be uninstalled using following command
pip3 uninstall xapp_onboarder

#Install xapp_onboarder using following command
pip3 install ./
```
Output:
```
Processing /root/appmgr/xapp_orchestrater/dev/xapp_onboarder
Requirement already satisfied: Click==7.0 in /usr/lib/python3/dist-packages (from xapp-onboarder==1.0.0) (7.0)
Collecting Flask==1.1.1
.
.
.
Successfully built xapp-onboarder PyYAML fire pyrsistent termcolor
ERROR: launchpadlib 1.10.13 requires testresources, which is not installed.
Installing collected packages: itsdangerous, Werkzeug, MarkupSafe, Jinja2, Flask, PyYAML, aniso8601, six, termcolor, fire, pytz, flask-restx, idna, pyrsistent, charset-normalizer, requests, zipp, xapp-onboarder
.
.
.
Successfully installed Flask-1.1.1 Jinja2-2.11.1 MarkupSafe-1.1.1 PyYAML-5.3 Werkzeug-0.16.1 aniso8601-8.0.0 charset-normalizer-3.3.2 fire-0.2.1 flask-restx-1.1.0 idna-2.9 itsdangerous-1.1.0 pyrsistent-0.15.7 pytz-2019.3 requests-2.31.0 six-1.16.0 termcolor-1.1.0 xapp-onboarder-1.0.0 zipp-3.1.0
```
6. Step 6: (OPTIONAL ) If the **host user is non-root user**, after installing the packages, please assign the permissions to the below filesystems
```
#Assign relevant permission for non-root user
sudo chmod 755 /usr/local/bin/dms_cli
sudo chmod -R 755 /usr/local/lib/python3.8
sudo chmod -R 755 /usr/local/lib/python3.8
```
7. Step 7: Onboard your xApp
```
# Make sure that you have the xapp descriptor config file and the schema file at your local file system
dms_cli onboard CONFIG_FILE_PATH SCHEMA_FILE_PATH
OR
dms_cli onboard --config_file_path=CONFIG_FILE_PATH --shcema_file_path=SCHEMA_FILE_PATH

#Example:
dms_cli onboard /files/config-file.json /files/schema.json
OR
dms_cli onboard --config_file_path=/files/config-file.json --shcema_file_path=/files/schema.json
```

8. Step 8: (OPTIONAL) List the helm charts from help repository.
```
#List all the helm charts from help repository
curl -X GET http://localhost:8080/api/charts | jq .

#List details of specific helm chart from helm repository
curl -X GET http://localhost:8080/api/charts/<XAPP_CHART_NAME>/<VERSION>
```

Step 9: (OPTIONAL) Delete a specific Chart Version from helm repository.
```
#Delete a specific Chart Version from helm repository
curl -X DELETE http://localhost:8080/api/charts/<XAPP_CHART_NAME>/<VERSION>
```

Step 10: (OPTIONAL) Download the xApp helm charts.
```
dms_cli download_helm_chart XAPP_CHART_NAME VERSION --output_path=OUTPUT_PATH
OR
dms_cli download_helm_chart --xapp_chart_name=XAPP_CHART_NAME --version=VERSION --output_path=OUTPUT_PATH

Example:
dms_cli download_helm_chart ueec 1.0.0 --output_path=/files/helm_xapp
OR
dms_cli download_helm_chart --xapp_chart_name=ueec --version=1.0.0 --output_path=/files/helm_xapp
```

Step 11: Install the xApp.
```
dms_cli install XAPP_CHART_NAME VERSION NAMESPACE
OR
dms_cli install --xapp_chart_name=XAPP_CHART_NAME --version=VERSION --namespace=NAMESPACE

Example:
dms_cli install ueec 1.0.0 ricxapp
OR
dms_cli install --xapp_chart_name=ueec --version=1.0.0 --namespace=ricxapp
```
#### Install the xApp hw-go
```
dms_cli install --xapp_chart_name=hw-go --version=1.0.0 --namespace=ricxapp
```

Step 12: (OPTIONAL) Install xApp using helm charts by providing the override values.yaml.
```
#Download the default values.yaml
dms_cli download_values_yaml XAPP_CHART_NAME VERSION --output_path=OUTPUT_PATH
OR
dms_cli download_values_yaml --xapp_chart_name=XAPP_CHART_NAME --version=VERSION --output_path=OUTPUT_PATH

Example:
dms_cli download_values_yaml traffic-steering 0.6.0 --output-path=/tmp
OR
dms_cli download_values_yaml --xapp_chart_name=traffic-steering --version=0.6.0 --output-path=/tmp

#Modify values.yaml and provide it as override file
dms_cli install XAPP_CHART_NAME VERSION NAMESPACE OVERRIDEFILE
OR
dms_cli install --xapp_chart_name=XAPP_CHART_NAME --version=VERSION --namespace=NAMESPACE --overridefile=OVERRIDEFILE

Example:
dms_cli install ueec 1.0.0 ricxapp /tmp/values.yaml
OR
dms_cli install --xapp_chart_name=ueec --version=1.0.0 --namespace=ricxapp --overridefile=/tmp/values.yaml
```

Step 13: (OPTIONAL) Uninstall the xApp.
```
dms_cli uninstall XAPP_CHART_NAME NAMESPACE
OR
dms_cli uninstall --xapp_chart_name=XAPP_CHART_NAME --namespace=NAMESPACE

Example:
dms_cli uninstall ueec ricxapp
OR
dms_cli uninstall --xapp_chart_name=ueec --namespace=ricxapp
```

Step 14: (OPTIONAL) Upgrade the xApp to a new version.
```
dms_cli upgrade XAPP_CHART_NAME OLD_VERSION NEW_VERSION NAMESPACE
OR
dms_cli upgrade --xapp_chart_name=XAPP_CHART_NAME --old_version=OLD_VERSION --new_version=NEW_VERSION --namespace=NAMESPACE

Example:
dms_cli upgrade ueec 1.0.0 2.0.0 ricxapp
OR
dms_cli upgrade --xapp_chart_name=ueec --old_version=1.0.0 --new_version=2.0.0 --namespace=ricxapp
```

Step 15: (OPTIONAL) Rollback the xApp to old version.
```
dms_cli rollback XAPP_CHART_NAME NEW_VERSION OLD_VERSION NAMESPACE
OR
dms_cli rollback --xapp_chart_name=XAPP_CHART_NAME --new_version=NEW_VERSION --old_version=OLD_VERSION --namespace=NAMESPACE

Example:
dms_cli rollback ueec 2.0.0 1.0.0 ricxapp
OR
dms_cli rollback --xapp_chart_name=ueec --new_version=2.0.0 --old_version=1.0.0 --namespace=ricxapp
```

Step 16: (OPTIONAL) Check the health of xApp.
```
dms_cli health_check XAPP_CHART_NAME NAMESPACE
OR
dms_cli health_check --xapp_chart_name=XAPP_CHART_NAME --namespace=NAMESPACE

Example:
dms_cli health_check ueec ricxapp
OR
dms_cli health_check --xapp_chart_name=ueec --namespace=ricxapp
```

# OSC RIC (Near RT RIC) - Manual Configuration

reference : 
* https://docs.o-ran-sc.org/projects/o-ran-sc-ric-plt-ric-dep/en/latest/installation-guides.html
* https://hackmd.io/@Whale4878/SJFSuRrca

## 1. Install the Docker, Kubernetes and Helm 3
### 1.2 Become root user : 
```
## Become root user
sudo -i
```
output : 
```
root@ubuntu:~#
```

### 1.3 Install the Dependent Tools
```
apt-get update

## Install the Dependent Tools
apt-get install -y git vim curl net-tools openssh-server python3-pip nfs-common
```

output : 

```
root@ubuntu:~# apt-get update
Hit:1 http://tw.archive.ubuntu.com/ubuntu focal InRelease
Hit:2 http://tw.archive.ubuntu.com/ubuntu focal-updates InRelease
Hit:3 http://tw.archive.ubuntu.com/ubuntu focal-backports InRelease
Hit:4 http://tw.archive.ubuntu.com/ubuntu focal-security InRelease
Hit:5 https://download.docker.com/linux/ubuntu focal InRelease
Hit:6 https://prod-cdn.packages.k8s.io/repositories/isv:/kubernetes:/core:/stable:/v1.28/deb  InRelease
Hit:7 http://ppa.launchpad.net/srslte/releases/ubuntu focal InRelease
Hit:8 https://apt.kitware.com/ubuntu focal InRelease
Hit:9 https://apt.kitware.com/ubuntu focal-rc InRelease
Reading package lists... Done
root@ubuntu:~# apt-get install -y git vim curl net-tools openssh-server python3-pip nfs-common
Reading package lists... Done
Building dependency tree
Reading state information... Done
net-tools is already the newest version (1.60+git20180626.aebd88e-1ubuntu1).
curl is already the newest version (7.68.0-1ubuntu2.22).
git is already the newest version (1:2.25.1-1ubuntu3.13).
nfs-common is already the newest version (1:1.3.4-2.5ubuntu3.7).
openssh-server is already the newest version (1:8.2p1-4ubuntu0.11).
vim is already the newest version (2:8.1.2269-1ubuntu5.23).
python3-pip is already the newest version (20.0.2-5ubuntu1.10).
0 upgraded, 0 newly installed, 0 to remove and 9 not upgraded.
```

### 1.4 Download the source code of RIC Platform
```
cd ~
git clone https://gerrit.o-ran-sc.org/r/ric-plt/ric-dep -b i-release
```
output : 
```
Cloning into 'ric-dep'...
remote: Total 2413 (delta 0), reused 2413 (delta 0)
Receiving objects: 100% (2413/2413), 1.08 MiB | 1.37 MiB/s, done.
Resolving deltas: 100% (983/983), done.
```
### 1.5 Execute the Installation Script of the Docker, Kubernetes and Helm 3
add repository alternative:
```
nano /etc/apt/sources.list
```
adding to sources : `deb https://mirrors.aliyun.com/kubernetes/apt kubernetes-xenial main`

continue command : 
```
curl https://mirrors.aliyun.com/kubernetes/apt/doc/apt-key.gpg | gpg --dearmor > /usr/share/keyrings/EXAMPLE.gpg
echo "deb [signed-by=/usr/share/keyrings/EXAMPLE.gpg] https://mirrors.aliyun.com/kubernetes/apt stable main" || sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
sudo apt-get update
```
output:
```bash
root@ubuntu:~# curl https://mirrors.aliyun.com/kubernetes/apt/doc/apt-key.gpg | gpg --dearmor > /usr/share/keyrings/EXAMPLE.gpg
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100  2659  100  2659    0     0  19129      0 --:--:-- --:--:-- --:--:-- 19129

root@ubuntu:~# echo "deb [signed-by=/usr/share/keyrings/EXAMPLE.gpg] https://mirrors.aliyun.com/kubernetes/apt stable main" || sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
deb [signed-by=/usr/share/keyrings/EXAMPLE.gpg] https://mirrors.aliyun.com/kubernetes/apt stable main

root@ubuntu:~# sudo apt-get update
Hit:1 http://tw.archive.ubuntu.com/ubuntu focal InRelease
Hit:2 http://tw.archive.ubuntu.com/ubuntu focal-updates InRelease
Hit:3 http://tw.archive.ubuntu.com/ubuntu focal-backports InRelease
Hit:4 http://tw.archive.ubuntu.com/ubuntu focal-security InRelease
Hit:5 https://download.docker.com/linux/ubuntu focal InRelease
Get:6 https://mirrors.aliyun.com/kubernetes/apt kubernetes-xenial InRelease [8,993 B]
Hit:7 https://prod-cdn.packages.k8s.io/repositories/isv:/kubernetes:/core:/stable:/v1.28/deb  InRelease
Hit:8 http://ppa.launchpad.net/srslte/releases/ubuntu focal InRelease
Err:6 https://mirrors.aliyun.com/kubernetes/apt kubernetes-xenial InRelease
  The following signatures couldn't be verified because the public key is not available: NO_PUBKEY B53DC80D13EDEF05
Hit:9 https://apt.kitware.com/ubuntu focal InRelease
Hit:10 https://apt.kitware.com/ubuntu focal-rc InRelease
Reading package lists... Done
W: GPG error: https://mirrors.aliyun.com/kubernetes/apt kubernetes-xenial InRelease: The following signatures couldn't be verified because the public key is not available: NO_PUBKEY B53DC80D13EDEF05
E: The repository 'https://mirrors.aliyun.com/kubernetes/apt kubernetes-xenial InRelease' is not signed.
N: Updating from such a repository can't be done securely, and is therefore disabled by default.
N: See apt-secure(8) manpage for repository creation and user configuration details.
```

```
cd ~/ric-dep/bin
./install_k8s_and_helm.sh
```

output : 
```bash
root@ubuntu:~/ric-dep/bin# ./install_k8s_and_helm.sh
+ KUBEV=1.16.0
+ KUBECNIV=0.7.5
+ HELMV=3.5.4
+ DOCKERV=20.10.21
+ echo running ./install_k8s_and_helm.sh
running ./install_k8s_and_helm.sh
+ getopts :k:d:e:n:c o
.
.
.
Done with master node setup
+ [[ ! -z '' ]]
+ [[ ! -z '' ]]
+ [[ ! -z '' ]]
+ [[ 1 -gt 100 ]]
+ [[ 1 -gt 100 ]]
```
### 1.6 Check the Status of Kubernetes deployment

```
kubectl get pods -A

```

output : 
```
root@ubuntu:~/ric-dep/bin# kubectl get pods -A
NAMESPACE     NAME                             READY   STATUS    RESTARTS   AGE
kube-system   coredns-5644d7b6d9-4hzkc         1/1     Running   0          2m25s
kube-system   coredns-5644d7b6d9-j8wvt         1/1     Running   0          2m25s
kube-system   etcd-ubuntu                      1/1     Running   0          93s
kube-system   kube-apiserver-ubuntu            1/1     Running   0          86s
kube-system   kube-controller-manager-ubuntu   1/1     Running   0          97s
kube-system   kube-flannel-ds-rmwf2            1/1     Running   0          2m25s
kube-system   kube-proxy-kjjmm                 1/1     Running   0          2m25s
kube-system   kube-scheduler-ubuntu            1/1     Running   0          101s
```

## 2. Install the Near-RT RIC Platform
### 2.1 Add the ric-common templates
command:
```
./install_common_templates_to_helm.sh
```

output:

```
Installing servecm (Chart Manager) and common templates to helm3
Error: plugin already exists
/root/.cache/helm/repository
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100 15.0M  100 15.0M    0     0  14.2M      0  0:00:01  0:00:01 --:--:-- 14.2M
linux-386/
linux-386/chartmuseum
linux-386/LICENSE
linux-386/README.md
servecm not yet running. sleeping for 2 seconds
nohup: appending output to 'nohup.out'
servcm up and running
/root/.cache/helm/repository
Successfully packaged chart and saved it to: /tmp/ric-common-3.3.2.tgz
"local" has been removed from your repositories
"local" has been added to your repositories
checking that ric-common templates were added
NAME                    CHART VERSION   APP VERSION     DESCRIPTION
local/ric-common        3.3.2                           Common templates for inclusion in other charts
```

command:
```
./setup-ric-common-template
```

output:
```
Cloning into '../dep'...
remote: Counting objects: 543, done
remote: Finding sources: 100% (7214/7214)
remote: Total 7214 (delta 2920), reused 7167 (delta 2920)
Receiving objects: 100% (7214/7214), 3.85 MiB | 4.15 MiB/s, done.
Resolving deltas: 100% (2920/2920), done.
.
.
.
+ cp /tmp/aux-common-3.0.0.tgz /root/.cache/helm/repository/local/
++ cat /root/ric-dep/dep/bin/../ric-common/Common-Template/helm/nonrtric-common/Chart.yaml
++ grep version
++ awk '{print $2}'
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

### 2.2 Edit Deployment Configuration
#### 2.2.1 Modify the code of xApp Manager
##### 2.2.1.1 Modify the Log-Level
command : 
```
sudo nano ~/ric-dep/helm/appmgr/resources/appmgr.yaml
```
Add loglevel “DEBUG”：
Add loglevel : 4

```
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
**Step 1：Modify the loglevel.txt section**

command : 
```
sudo nano ~/ric-dep/helm/a1mediator/templates/config.yaml
```

Change log-level: {{ .Values.loglevel }} to log-level: {{ .Values.a1mediator.loglevel }}

output : 
```
  loglevel.txt: |
    log-level: {{ .Values.a1mediator.loglevel }}
```

**Step 2：Change loglevel from INFO to DEBUG & change Component Connection**

command : 
```
sudo nano ~/ric-dep/helm/a1mediator/values.yaml
```
Change loglevel from INFO to DEBUG & add a1ei: ecs_ip_port: "http://<ecs_host>:<ecs_port>

output: 
```
  rmr_timeout_config:
    a1_rcv_retry_times: 20
    ins_del_no_resp_ttl: 5
    ins_del_resp_ttl: 10
  loglevel: "DEBUG"
  a1ei:
    ecs_ip_port: "http://<ecs_host>:<ecs_port>"
```
#### 2.2.2.2 Component Connection

**Step 1：Add ENV for A1EI**
```
sudo nano ~/ric-dep/helm/a1mediator/templates/env.yaml
```
Add ECS_SERVICE_HOST: {{ .Values.a1mediator.a1ei.ecs_ip_port }}

output: 
```
  INSTANCE_DELETE_NO_RESP_TTL: "{{ .Values.a1mediator.rmr_timeout_config.ins_del_no_resp_ttl }}"
  INSTANCE_DELETE_RESP_TTL: "{{ .Values.a1mediator.rmr_timeout_config.ins_del_resp_ttl }}"
  CONFIG_MAP_NAME: "/opt/route/loglevel.txt"
  ECS_SERVICE_HOST: {{ .Values.a1mediator.a1ei.ecs_ip_port }}
```

#### 2.2.3 Modify the code of E2 Termination(Error occurred, Skipped!!)

#### 2.2.4 Modify the code of Subscription Manager
##### 2.2.4.1 Modify the Log-Level
Change level from 3(Info) to 4(Debug)：
```
sudo nano ~/ric-dep/helm/submgr/templates/configmap.yaml
```

output:
```
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

#### 2.2.4.2 Component Connection

Step 1：Add new port for subscription in service file

```
sudo nano ~/ric-dep/helm/submgr/templates/service-http.yaml
```

Add Line 11 to 14 
```bash=
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
```
sudo nano ~/ric-dep/helm/submgr/templates/deployment.yaml
```
Add Line from 9 to 11
```bash=
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

#### 2.2.5 Modify the code of Routing Manager
##### 2.2.5.1 Routing Path Configuration
Add A1EI Msgtype and A1EI Routes：
```
sudo nano ~/ric-dep/helm/rtmgr/templates/config.yaml
```
Add Line from 3 to 7 & 12 to 13
```bash=
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
#### 2.2.6 Modify the code of Alarm Manager
##### 2.2.6.1 Component Connection
Step 1：Change controls.promAlertManager.address
```
sudo nano ~/ric-dep/helm/alarmmanager/templates/configmap.yaml
```

change cpro-alertmanager:80 to r4-infrastructure-prometheus-alertmanager:80

```
controls": {
        "promAlertManager": {
          "address": "r4-infrastructure-prometheus-alertmanager:80",
          "baseUrl": "api/v2",
          "schemes": "http",
          "alertInterval": 30000
        },
```
Step 2：Add livenessProbe and readinessProbe

```
sudo nano ~/ric-dep/helm/alarmmanager/templates/deployment.yaml

```
Add Line from 10 to 25
```bash=
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
Add livenessProbe and readinessProbe：
```
sudo nano ~/ric-dep/helm/o1mediator/templates/deployment.yaml
```

Add Line from 10 to 29

```bash=
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

### 2.3 Install nfs for InfluxDB

```
kubectl create ns ricinfra
helm repo add stable https://charts.helm.sh/stable
helm install nfs-release-1 stable/nfs-server-provisioner --namespace ricinfra 
kubectl patch storageclass nfs -p '{"metadata": {"annotations":{"storageclass.kubernetes.io/is-default-class":"true"}}}'
sudo apt install nfs-common
```
output : 
```
root@ubuntu:~/ric-dep/bin# kubectl create ns ricinfra
namespace/ricinfra created
root@ubuntu:~/ric-dep/bin# helm repo add stable https://charts.helm.sh/stable
"stable" already exists with the same configuration, skipping
root@ubuntu:~/ric-dep/bin# helm install nfs-release-1 stable/nfs-server-provisioner --namespace ricinfra
WARNING: This chart is deprecated
NAME: nfs-release-1
LAST DEPLOYED: Wed Jul 10 03:55:03 2024
NAMESPACE: ricinfra
STATUS: deployed
REVISION: 1
TEST SUITE: None
NOTES:
The NFS Provisioner service has now been installed.

A storage class named 'nfs' has now been created
and is available to provision dynamic volumes.

You can use this storageclass by creating a `PersistentVolumeClaim` with the
correct storageClassName attribute. For example:

    ---
    kind: PersistentVolumeClaim
    apiVersion: v1
    metadata:
      name: test-dynamic-volume-claim
    spec:
      storageClassName: "nfs"
      accessModes:
        - ReadWriteOnce
      resources:
        requests:
          storage: 100Mi
root@ubuntu:~/ric-dep/bin# kubectl patch storageclass nfs -p '{"metadata": {"annotations":{"storageclass.kubernetes.io/is-default-class":"true"}}}'
storageclass.storage.k8s.io/nfs patched
root@ubuntu:~/ric-dep/bin# sudo apt install nfs-common
Reading package lists... Done
Building dependency tree
Reading state information... Done
nfs-common is already the newest version (1:1.3.4-2.5ubuntu3.7).
0 upgraded, 0 newly installed, 0 to remove and 13 not upgraded.
```

### 2.4 Execute the Installation Script of Near-RT RIC
Find your IP of VM：
```
ip a
```

output:

```
root@teep-ric:~# ip a
2: ens18: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc fq_codel state UP group default qlen 1000
    link/ether bc:24:11:87:c5:1f brd ff:ff:ff:ff:ff:ff
    inet 192.168.0.16/24 brd 192.168.0.255 scope global dynamic ens18
       valid_lft 71858sec preferred_lft 71858sec
    inet6 fe80::be24:11ff:fe87:c51f/64 scope link
       valid_lft forever preferred_lft forever
```

Modify the IP of RIC and AUX：:
```
sudo nano ~/ric-dep/RECIPE_EXAMPLE/example_recipe_oran_i_release.yaml
```
output:
```
# Change the namespaces using the following options
#  namespace:
#    aux: ricaux
#    platform: ricplt
#    xapp: ricxapp
#    infra: ricinfra

# ricip should be the ingress controller listening IP for the platform cluster
# auxip should be the ingress controller listening IP for the AUX cluster
extsvcplt:
  ricip: "192.168.0.16"
  auxip: "192.168.0.16"

```
Deploy the RIC Platform：
```
cd ~/ric-dep/bin
./install -f ../RECIPE_EXAMPLE/example_recipe_oran_i_release.yaml -c "jaegeradapter influxdb"

```
output:
```
root@ubuntu:~/ric-dep/bin# ./install -f ../RECIPE_EXAMPLE/example_recipe_oran_i_release.yaml -c "jaegeradapter influxdb"
namespace/ricplt created
namespace/ricxapp created
nfs storage exist
Deploying RIC infra components [infrastructure dbaas appmgr rtmgr e2mgr e2term a1mediator submgr vespamgr o1mediator alarmmanager jaegeradapter influxdb]
configmap/ricplt-recipe created
.
.
.
NAME: r4-influxdb
LAST DEPLOYED: Wed Jul 10 04:01:01 2024
NAMESPACE: ricplt
STATUS: deployed
REVISION: 1
TEST SUITE: None
NOTES:
InfluxDB 2 is deployed as a StatefulSet on your cluster.

You can access it by using the service name: r4-influxdb-influxdb2

To retrieve the password for the 'admin' user:

  echo $(kubectl get secret r4-influxdb-influxdb2-auth -o "jsonpath={.data['admin-password']}" --namespace ricplt | base64 --decode)

Note: with enabled persistence, admin password is only set once during the initial deployment. The password is not changed when InfluxDB 2 is re-deployed with different password.
```

### 2.5. Check the Status of Near-RT RIC deployment

* Results similar to the output shown below indicate a complete and successful deployment, all are either “Completed” or “Running”, and that none are “Error”, “Pending”, “Evicted”,or “ImagePullBackOff”.
* The status of pods “PodInitializing” & “Init” & “ContainerCreating” mean that the pods are creating now, you need to wait for deploying.

```
kubectl get pods -A
```

Output:
```
root@ubuntu:~/ric-dep# kubectl get pods -A
NAMESPACE     NAME                                                         READY   STATUS      RESTARTS   AGE
kube-system   coredns-5644d7b6d9-6phtx                                     1/1     Running     2          20d
kube-system   coredns-5644d7b6d9-bmm8d                                     1/1     Running     2          20d
kube-system   etcd-ubuntu                                                  1/1     Running     5          20d
kube-system   kube-apiserver-ubuntu                                        1/1     Running     4          20d
kube-system   kube-controller-manager-ubuntu                               1/1     Running     11         20d
kube-system   kube-flannel-ds-j8lb9                                        1/1     Running     2          20d
kube-system   kube-proxy-c2qwx                                             1/1     Running     2          20d
kube-system   kube-scheduler-ubuntu                                        1/1     Running     9          20d
ricinfra      deployment-tiller-ricxapp-68f777c4d4-w65tn                   1/1     Running     0          42h
ricinfra      tiller-secret-generator-k864p                                0/1     Completed   0          42h
ricplt        deployment-ricplt-a1mediator-7d5b85ff7d-cdcl8                1/1     Running     0          42h
ricplt        deployment-ricplt-alarmmanager-6bd5fccfc8-gmm9v              1/1     Running     0          42h
ricplt        deployment-ricplt-appmgr-77986c9cbb-gmvnb                    1/1     Running     0          42h
ricplt        deployment-ricplt-e2mgr-78c987559f-2n5nf                     1/1     Running     2          42h
ricplt        deployment-ricplt-e2term-alpha-5dc768bcb7-8swlk              1/1     Running     0          42h
ricplt        deployment-ricplt-o1mediator-97fb6759b-2jj8j                 1/1     Running     0          42h
ricplt        deployment-ricplt-rtmgr-78f768474-9dtmg                      1/1     Running     1          42h
ricplt        deployment-ricplt-submgr-547965db4c-wph5t                    1/1     Running     0          42h
ricplt        deployment-ricplt-vespamgr-84f7d87dfb-qd4mp                  1/1     Running     0          42h
ricplt        r4-infrastructure-kong-7995f4679b-7cb98                      2/2     Running     2          42h
ricplt        r4-infrastructure-prometheus-alertmanager-5798b78f48-gj569   2/2     Running     0          42h
ricplt        r4-infrastructure-prometheus-server-c8ddcfdf5-z9tkd          1/1     Running     0          42h
ricplt        statefulset-ricplt-dbaas-server-0                            1/1     Running     0          42h
```

## 3. Install the DMS Tool

### 3.1 Install the DMS tool

Prepare source code：
```
docker run --rm -u 0 -it -d -p 8090:8080 -e DEBUG=1 -e STORAGE=local -e STORAGE_LOCAL_ROOTDIR=/chart -v $(pwd)/charts:/charts chartmuseum/chartmuseum:latest
export CHART_REPO_URL=http://0.0.0.0:8090
git clone https://gerrit.o-ran-sc.org/r/ric-plt/appmgr -b i-release
```
output:
```
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

Install DMS tool：

```
cd appmgr/xapp_orchestrater/dev/xapp_onboarder
apt-get install python3-pip
pip3 uninstall xapp_onboarder
pip3 install ./
chmod 755 /usr/local/bin/dms_cli
ls -la /usr/local/lib/python3.8
chmod -R 755 /usr/local/lib/python3.8
```

output:
```
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