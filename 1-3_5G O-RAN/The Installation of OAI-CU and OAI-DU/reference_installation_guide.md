:::info
[TOC]
:::


[O-RAN架構概述](https://docs.o-ran-sc.org/en/latest/architecture/architecture.html)

![o-ran-architecture](https://hackmd.io/_uploads/S1jZ4mrRp.png)
# SMO background
O1：服務管理和編排框架中的管理實體與O-RAN被管理元素之間的接口，用於**操作**和**管理**，透過該接口實現**FCAPS**管理、軟體管理、文件管理。
:::info
FCAPS是故障、配置、審計、性能、安全
:::

O1*：服務管理和編排框架與支援 O-RAN 虛擬網路功能的基礎架構管理框架之間的介面。

- SMO的功能目前分為3類
    - 非 RT RIC 相關 SMOS
    - O-Cloud管理和編排相關的SMOS
    - RAN NF OAM 相關的 SMOS
![image](https://hackmd.io/_uploads/SJf54bfGC.png)

---
## VES collector call flow & response
![image](https://hackmd.io/_uploads/SJI2XpugR.png)

[Service Exceptions](https://docs.onap.org/projects/onap-vnfrqts-requirements/en/latest/Chapter8/ves7_1spec.html#service-exceptions)
![image](https://hackmd.io/_uploads/SJglE6Oe0.png)
[Policy Exceptions](https://docs.onap.org/projects/onap-vnfrqts-requirements/en/latest/Chapter8/ves7_1spec.html#policy-exceptions)
![image](https://hackmd.io/_uploads/ryZW46uxA.png)
[response](https://docs.onap.org/projects/onap-vnfrqts-requirements/en/latest/Chapter8/ves7_1spec.html#http-status-codes)
![image](https://hackmd.io/_uploads/ryUUUaugC.png)



---


O1/VES支援SMO的監控事項，下圖顯示各module間如何與SMO中的O1/VES互動。
![image](https://hackmd.io/_uploads/rkqa35Hpa.png)
事件由VES Agent處理，將其轉換為VES的形式並傳送給VES Collector。VRE Collector將事件儲存在influxDB中或儲存在Elasticsearch引擎和/或Kafka匯流排中，然後Grafana或任何其他的應用程式取得數據後，對數據進行必要的分析。
![image](https://hackmd.io/_uploads/ByYdacB6p.png)


![image](https://hackmd.io/_uploads/S1Cz-oSTp.png)


![image](https://hackmd.io/_uploads/H1WNBora6.png)

![image](https://hackmd.io/_uploads/S1UuBsBpa.png)

![image](https://hackmd.io/_uploads/HyT4wsB6p.png)

![image](https://hackmd.io/_uploads/SkcCDiSap.png)

![image](https://hackmd.io/_uploads/r1x1MlkyA.png)
[參考網址](https://wiki.o-ran-sc.org/display/OAM/OAM+Architecture?preview=/3605245/20875810/o-ran-architecture.png)

![image](https://hackmd.io/_uploads/rJlyQG11A.png)
[參考網址](https://hackmd.io/@thc1006/S1UNcWlO9#O1-%E7%B5%84%E4%BB%B6%E6%9E%B6%E6%A7%8B-O1-Component-Architecture%EF%BC%9A)

[O-RAN OAM Fault Supervision Management Services（故障監視管理服務）](https://hackmd.io/@thc1006/B1WmiOX92)

[VES是件監聽器](https://docs.onap.org/projects/onap-vnfrqts-requirements/en/latest/Chapter8/ves_7_2/ves_event_listener_7_2.html)

[Docker初學資源](https://hackmd.io/@thc1006/rku088xM5#Docker%E5%88%9D%E5%AD%B8%E8%B3%87%E6%BA%90)

[Minikube k8s Web UI 可以做到的事~](https://hackmd.io/@thc1006/H1NNU12Vc)

[NETCONF-netopeer2 connect](https://docs.opendaylight.org/projects/netconf/en/latest/user-guide.html#netconf-connector-netopeer)






---

ONAP部屬架構
![image](https://hackmd.io/_uploads/HyVayYSRT.png)




# smo installation step
:::info
- reference : 
[ONAP - Based [I] SMO Deployment - HeidHung stud notes](https://hackmd.io/@H141319/ByOoZCmDa#ONAP---Based-I-SMO-Deployment)
[SMO version](https://wiki.o-ran-sc.org/pages/viewpage.action?pageId=53870899)
[F Release Docker Image List](https://wiki.o-ran-sc.org/display/IAT/F+Release+Docker+Image+List)

還在閱讀
[SMO Operating - Non RT RIC Dashboard](https://hackmd.io/@4G7xxurNQEGA3Apb11YQJg/HyhsgMVfi?utm_source=preview-mode&utm_medium=rec)
[smo dashboard](https://hackmd.io/@4G7xxurNQEGA3Apb11YQJg/rJvOYqzGj#clone-the-git)

:::
## Minimum Requirements
:::success
### hareware

官方文件
![image](https://hackmd.io/_uploads/ryIHVqJRa.png)

自己hareware配置
```
CPU : 32 core
RAM : 32 GB
Disk : 100GB
```
### software
```
Ubuntu 22.04 server
Kubernetes v1.27.5 
python3 3.10.12 # Version should upper or equal to 3.9
```

:::

## Prerequisite
### 1.Install Kubernetes with kubespray
進入root權限，路徑為 `cd ~/`
![image](https://hackmd.io/_uploads/B1fT8cyC6.png)

```=
python3 --version # Version should upper or equal to 3.9
apt install -y python3-pip

git clone https://github.com/kubernetes-sigs/kubespray -b release-2.23
cd kubespray 
pip install -r requirements.txt

sed -i 's/\(kube_version: \)[^"]*/\1v1.27.5/' inventory/local/group_vars/k8s_cluster/k8s-cluster.yml
ansible-playbook -i inventory/local/hosts.ini --become --become-user=root cluster.yml

mkdir ~/.kube/config
sudo cp /etc/kubernetes/admin.conf ~/.kube/config
```
## Deployment
在root權限下執行，路徑 `cd ~/`
![image](https://hackmd.io/_uploads/SJTwwq10T.png)
### 1.Download the IT/dep repository from gerrit
```=
# Latest version
cd ~
git clone https://gerrit.o-ran-sc.org/r/it/dep.git -b master --recursive
```
### 2.Setup Helm Charts
```
cd dep
##Setup ChartMuseum
./smo-install/scripts/layer-0/0-setup-charts-museum.sh

##Setup HELM3
./smo-install/scripts/layer-0/0-setup-helm3.sh

## Build ONAP/ORAN charts
./smo-install/scripts/layer-1/1-build-all-charts.sh
``` 
### 3.Deploy components
```=
./smo-install/scripts/layer-2/2-install-oran.sh
```

### 4.Wait for pod finished
```=
kubectl get pods -n onap && kubectl get pods -n nonrtric
```
:::danger
第三步部署如果沒成功。
- 解決方案 : 
    - 可能為docker拉取速度不足，需要註冊docker hub帳號，然後docker拉取速度會加快，目前成功下載。
    - 註冊網頁:https://hub.docker.com/
    - 安裝docker:`sudo apt install docker.io`
    - 使用 docker 命令来登录 Docker Hub 了:`docker login`
    - 登出:`docker logout`，需要在另一台操作時需要先登出。
:::

---
# SMO VES collector install
[Service Managerment and Orgestration(SMO)](https://docs.o-ran-sc.org/en/latest/projects.html#service-managerment-and-orgestration-smo)
[How to install the VES Collector](https://wiki.o-ran-sc.org/pages/viewpage.action?pageId=35881888)
## 安裝smo/ves
```=
git clone "https://gerrit.o-ran-sc.org/r/smo/ves" && (cd "ves" && mkdir -p `git rev-parse --git-dir`/hooks/ && curl -Lo `git rev-parse --git-dir`/hooks/commit-msg https://gerrit.o-ran-sc.org/r/tools/hooks/commit-msg && chmod +x `git rev-parse --git-dir`/hooks/commit-msg)

cd ves

docker-compose build //開始建置、執行
docker-compose up -d  //docker-compose down 讓docker停止
```
## 安裝證書
```=
mkdir ~/ves-certificate //建立存放key資料夾

openssl genrsa -out vescertificate.key 2048
openssl req -new -key vescertificate.key -out vescertificate.csr
openssl x509 -req -days 365 -in vescertificate.csr -signkey vescertificate.key -out vescertificate.crt
```


輸入`docker-compose ps`，觀察是否成功安裝。
![image](https://hackmd.io/_uploads/H1nJZ7eCp.png)

---

# SMO VES collcetor test
[How to test the VES interface](https://wiki.o-ran-sc.org/pages/viewpage.action?pageId=35881892)
[VES 回報文件&spec](https://docs.onap.org/projects/onap-dcaegen2/en/montreal/sections/apis/ves.html)

```=
git clone "https://gerrit.o-ran-sc.org/r/oam" && (cd "oam" && mkdir -p `git rev-parse --git-dir`/hooks/ && curl -Lo `git rev-parse --git-dir`/hooks/commit-msg https://gerrit.o-ran-sc.org/r/tools/hooks/commit-msg && chmod +x `git rev-parse --git-dir`/hooks/commit-msg)

cd /oam/code/client-scripts-ves-v7 //進入文件修該config檔
```
修改config文件:`sudo nano config`
after : 
![image](https://hackmd.io/_uploads/BJ2CZEeCp.png)

執行_exampl.sh文件 : `./_example.sh`
result : 會有202成功和500失敗，部分截圖。
![image](https://hackmd.io/_uploads/SymtG4lCp.png)
![image](https://hackmd.io/_uploads/S193f4eRp.png)

修改config.yaml文件:`sudo nano config.yaml`
after : 
![image](https://hackmd.io/_uploads/ryn2QVxCa.png)

result
![image](https://hackmd.io/_uploads/ryMP7EgCa.png)

## VES collector 資料收集 spec 要求
reference : 
[Common Event Format](https://docs.onap.org/projects/onap-vnfrqts-requirements/en/latest/Chapter8/ves7_1spec.html#common-event-format)
[Field Block Versions](https://docs.onap.org/projects/onap-vnfrqts-requirements/en/latest/Chapter8/ves7_1spec.html#field-block-versions)

- 發送消息時，需要`commomEventHeader`以及`commomEventHeader`裡面需要的參數。
[DataType-event](https://docs.onap.org/projects/onap-vnfrqts-requirements/en/latest/Chapter8/ves7_1spec.html#datatype-event)

![image](https://hackmd.io/_uploads/SJ2mGaveR.png)

[Datatype: commonEventHeader](https://docs.onap.org/projects/onap-vnfrqts-requirements/en/latest/Chapter8/ves7_1spec.html#datatype-commoneventheader)

部分截圖，可以查看`commomEventHeader`中必要參數，消息才可以順利發出。
![image](https://hackmd.io/_uploads/S1nDm6wl0.png)

- example : 根節點為`event`，並且一定要有`commonEventHeader`送出消息才會成功。

![image](https://hackmd.io/_uploads/rk-HU6PeC.png)









---

# SMO VES client install
[integration-simulators-nf-simulator](https://github.com/onap/integration-simulators-nf-simulator-ves-client)
```=
git clone https://github.com/onap/integration-simulators-nf-simulator-ves-client

docker-compose up -d

mvn clean install -P docker
```

:::danger
### 1
進入file執行`docker-compose up -d`，會出現找不到文件指令。
![image](https://hackmd.io/_uploads/r1sNdqBCp.png)

修改`nano docker-compose.yml`檔案
![image](https://hackmd.io/_uploads/rysju9HAp.png)

after，去docker網站搜尋`onap/org.onap.integration.nfsimulator.vesclient`可用版本
![image](https://hackmd.io/_uploads/SyBlKcHRp.png)
### 2
![image](https://hackmd.io/_uploads/r1akcqS0p.png)

:::






---

# SMO O1 interface insatll
[How to install the O1 interface](https://wiki.o-ran-sc.org/pages/viewpage.action?pageId=35881890)

## prerequisites
- docker
- docker-compose
- java,version 11 or newer
## 安裝O1 interface
```=
unzip o1-netconf.zip //網站上有檔案，下載後解壓縮。

cd client
docker-compose up -d //執行服務
```
輸入`docker-compose ps`，檢查docker status。
result : 
![image](https://hackmd.io/_uploads/r1xtavWAa.png)

:::success
Access details
Access the GUI and RESTCONF interface using the following URLs, credentials are common for both of them.

username:admin password:Kp8bJ4SXszM0WXlhak3eHlcse2gAw84vaoGGmJvUy2U

GUI: http://<host_ip>:8181/odlux/index.html
Restconf: http://<host_ip>:8181/apidoc/explorer/index.html

:::
### Use GUI let netconf client  connect to netconf server  result
:::warning
[官方文件](https://docs.o-ran-sc.org/projects/o-ran-sc-oam/en/latest/overview.html)

#### result
![image](https://hackmd.io/_uploads/H1NjiKMJ0.png)

#### step
- 進入頁面->connect->Add
![image](https://hackmd.io/_uploads/ry0mptGkR.png)
- 輸入
    - 名稱
    - 想連接的 netconf server IP
    - 目標機器netconf的port
    - username/password (使用ssh進入netconf的使用者名稱/密碼)
![image](https://hackmd.io/_uploads/HJhUpKGk0.png)
- 點選connect->connection status log 可以觀察目標機器是否為連線狀態。
![image](https://hackmd.io/_uploads/rkl440tM1A.png)

:::

# SMO O1 interface test

[How to test the O1 interface](https://wiki.o-ran-sc.org/display/SMO/How+to+test+the+O1+interface)

## prerequisite
- docker
- docker-compose

## Automated test-suite
- Test-suite does the following steps
    1. Brings up simulators(RU & DU)
    2. Brings up SDNR
    3. Add simulators to SDNR
    4. Checks connectivity status by fetching the capabilities
    5. Updates DU and RU config and prints the output Tear down the services

```=
git clone -b dawn https://gerrit.o-ran-sc.org/r/smo/o1.git
cd o1/
./run_tests.sh
```

result
![image](https://hackmd.io/_uploads/H1qShOWAp.png)

![image](https://hackmd.io/_uploads/Ske53d-Ap.png)

:::danger
要修改.env文件，有地方配置錯誤。
進入以下路徑輸入`ls -a`查看.env隱藏文件，並進入編輯模式`nano .env`
![image](https://hackmd.io/_uploads/rkGLFd-A6.png)

port 10004要修改成10002。
![image](https://hackmd.io/_uploads/Sk2eqdb0a.png)

:::

# Deployment of dmaap-InfluxDB-adapter, InfluxDB and Grafana

## pre-Request
- Finished the installation of ONAP SMO.

## Deploy
- Helm repo add and install
```=
helm repo add winlab https://harbor.winfra.cs.nycu.edu.tw/chartrepo/winlab-oran
helm install --namespace=o1ves o1ves winlab/o1ves-visualization --create-namespace
```
- 獲取 Helm repo 壓縮包
```=
helm pull winlab/o1ves-visualization
tar -zxvf o1ves-visualization-<version>.tgz
```
## 編輯values.yaml 文件
```=
helm show values winlab/o1ves-visualization > values.yaml
```
![image](https://hackmd.io/_uploads/HklOoSfORT.png)
:::info
- Modify the rules.
- Add buckets to automatically create influxdb buckets.
:::

example `values.yaml`:
```yaml=
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

修改部份:`dmaap-influxdb-adapter`改為以下
```yaml=
dmaap-influxdb-adapter:
  image:
    pullPolicy: Always
  logLevel: DEBUG
  rules:
    - topic: unauthenticated.VES_MEASUREMENT_OUTPUT
      rules:
        - bucket: <my-bucket> //儲存庫名稱
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
  - name: <my-bucket>
```

:::warning
如果有編輯valuse.yaml檔案，需要重新upload the pod 或是刪除後重新佈署。
```=
## Upgrade
helm upgrade --namespace=o1ves o1ves winlab/o1ves-visualization --create-namespace -f value2.yml

## Redeploy
helm uninstall --namespace o1ves o1ves  
kubectl delete ns o1ves
sudo rm -r /dockerdata-nfs/o1ves-*
helm install --namespace=o1ves o1ves winlab/o1ves-visualization --create-namespace -f values.yaml
```

測試使用ves送出event給influxdb
```=
curl -X POST \
   -H 'Content-Type: application/json' \
   -u sample1:sample1 \
   -d @file.json \
   http://<influxdb主機IP>:<influxdb port>/eventListener/v7
```
result
![image](https://hackmd.io/_uploads/H14utGdAa.png)

查看**influxdb-adapter**是否有接收
```=
kubectl logs -n o1ves <名稱>
```
![image](https://hackmd.io/_uploads/ryJRFfdC6.png)

result
![image](https://hackmd.io/_uploads/HJQNqMO0p.png)

### 問題
上面result結果顯示找不到topic。

reference : 
[dmaap API](https://docs.onap.org/projects/onap-dmaap-messagerouter-messageservice/en/latest/offeredapis/api.html)
我們`values.yaml`檔案可以填寫自己抓取資料的規則，並轉傳給influxdb，以上API 文件可以讓我們知道`topic`目前有哪些，並可以建立`topic`做使用。

#### 使用K8s指令知道 dmaap IP
```
kubectl get svc -A
```
result : 
![image](https://hackmd.io/_uploads/SkZ-hbKg0.png)
```
curl -X GET http://10.233.31.103:3904/topics
```
result : 
![image](https://hackmd.io/_uploads/SkkVnWtx0.png)

#### 使用`echo`指令確認是否有值
- example

規則為 : 
![image](https://hackmd.io/_uploads/B1X06MFlA.png)

**要注意如果是字段名要加入" "括號起來，不然會被當作路徑。**

部分截圖 : 
.會被當作路徑，導致出錯抓不到預定想要得到的值，所以如果有.需要用""刮起來。
![image](https://hackmd.io/_uploads/rkbKRzYgR.png)

![image](https://hackmd.io/_uploads/BJz1yXFgC.png)


```
echo <內容> | jq '<要取得的值路徑>'
```

:::

# InfluxDB, Grafana Web UI and Set InfluxDB Data Source

## InfluxDB Web UI
- http://<server-ip/>:30001
![image](https://hackmd.io/_uploads/HkG3qMOCp.png)

username : admin
password需要輸入以下command去解碼獲得:
```=
kubectl get secret -n o1ves o1ves-influxdb2-auth -o json

echo <admin-password 紅色標記部份> | base64 -d 
```
![image](https://hackmd.io/_uploads/SJ84jzdCp.png)

正確密碼:
![image](https://hackmd.io/_uploads/HkzhjzuR6.png)

result:
![image](https://hackmd.io/_uploads/Sk6bhzuA6.png)

## Grafana Web UI
- http://<server-ip/>:30000
![image](https://hackmd.io/_uploads/SyDD2f_0T.png)

username : admin
password : smo

![image](https://hackmd.io/_uploads/HJAF2z_0T.png)

### 配置Grafana與influxdb相連
#### step 1
Home -> Administration -> Data sources，進入後會看到預設的influxdb。

![image](https://hackmd.io/_uploads/SJpSTf_A6.png)

![image](https://hackmd.io/_uploads/SkTq6GORp.png)

#### step 2
- 檢查設定
    - Query Language: Flux
    - URL: http://o1ves-influxdb2.o1ves
    - Auth
        - Basic auth: Disable
    - InfluxDB Details
        - Organization: influxdata
        - Token: my-token

![image](https://hackmd.io/_uploads/H1iPyvtCT.png)

![image](https://hackmd.io/_uploads/SJuqkwtCp.png)

![image](https://hackmd.io/_uploads/Hkra1wK0a.png)

:::warning
可能遇到的問題 :
**influxDB Web UI** 查看
API token
![image](https://hackmd.io/_uploads/HJqdxDtRa.png)

---


click admin圖示 -> 關於 -> Name，可以知道organization的名稱是甚麼。
![image](https://hackmd.io/_uploads/SyTTbvFC6.png)

---

驗證influxdb和grafana之間連接是沒問題的。
```
curl -i http://<InfluxDB_IP>:<InfluxDB_Port>/ping
```

result
![image](https://hackmd.io/_uploads/HkDJmwFRp.png)

:::



