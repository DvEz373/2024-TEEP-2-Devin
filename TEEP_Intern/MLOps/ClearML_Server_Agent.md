# ClearML
## Introduction
ClearML is an open source platform that automates and simplifies developing and managing machine learning solutions for thousands of data science teams all over the world. It is designed as an end-to-end MLOps and LLMOps suite allowing you to focus on developing your ML code and automation, while ClearML ensures your work is reproducible and scalable.

## Prerequisite from the References
1. Set up a Kubernetes cluster - For setting up Kubernetes on various platforms refer to the Kubernetes [getting started guide](https://kubernetes.io/docs/setup).
2. Set up a single node LOCAL Kubernetes on laptop / desktop - For setting up Kubernetes on your laptop/desktop, [kind](https://kind.sigs.k8s.io/) is recommended.
3. Install helm - Helm is a tool for managing Kubernetes charts. Charts are packages of pre-configured Kubernetes resources. To install Helm, refer to the [Helm installation guide](https://helm.sh/docs/using_helm.html#installing-helm) in the Helm documentation. Ensure that the helm binary is in the PATH of your shell.
4. Make an account in ClearML first to be able to get the API credentials.
![image](https://hackmd.io/_uploads/BkPb9rJKC.png)


## ClearML-Server Installation and Deployment
You will create a multi-node Kubernetes cluster using Helm, and then install ClearML in your cluster. For deployment instructions with up-to-date Helms charts, see the [clearml-helm-charts repository](https://github.com/allegroai/clearml-helm-charts/tree/main/charts/clearml#local-environment).
### Helm Charts Installation
#### Helm Repo
```bash
helm repo add allegroai https://allegroai.github.io/clearml-helm-charts
helm repo update
```
output:
```bash
root@node1:~# helm repo add allegroai https://allegroai.github.io/clearml-helm-charts
"allegroai" already exists with the same configuration, skipping
root@node1:~# helm repo update
Hang tight while we grab the latest from your chart repositories...

...Successfully got an update from the "winlab" chart repository
...Successfully got an update from the "nfs-subdir-external-provisioner" chart repository
...Successfully got an update from the "allegroai" chart repository
Update Complete. ⎈Happy Helming!⎈
```
#### ClearML Server Ecosystem
```bash
helm install clearml allegroai/clearml
```
output:
```bash
root@node1:~# helm install clearml allegroai/clearml
W0725 03:30:56.446297 1257431 warnings.go:70] spec.template.spec.containers[0].env[13].name: duplicate name "CLEARML__secure__auth__token_secret"
NAME: clearml
LAST DEPLOYED: Thu Jul 25 03:30:54 2024
NAMESPACE: default
STATUS: deployed
REVISION: 1
NOTES:
1. Get the application URL:
  export NODE_PORT=$(kubectl get --namespace default -o jsonpath="{.spec.ports[0].nodePort}" services clearml)
  export NODE_IP=$(kubectl get nodes --namespace default -o jsonpath="{.items[0].status.addresses[0].address}")
  echo http://$NODE_IP:$NODE_PORT
```

## Check Deployment
### Get Pods
```bash
kubectl get pods -A
```
output:
```
root@node1:~# kubectl get pods -A
NAMESPACE        NAME                                                READY   STATUS      RESTARTS        AGE
default          clearml-agent-5db8888b74-z5wd6                      1/1     Running     0               20m
default          clearml-apiserver-6d4c8cbdb8-jprrt                  1/1     Running     0               19m
default          clearml-apiserver-asyncdelete-55bff77dd7-xg4pp      1/1     Running     0               19m
default          clearml-elastic-master-0                            1/1     Running     0               19m
default          clearml-fileserver-7898b4cc8c-2fv5m                 1/1     Running     0               19m
default          clearml-mongodb-6dc769c4d8-qrz9b                    1/1     Running     0               19m
default          clearml-redis-master-0                              1/1     Running     0               19m
default          clearml-webserver-68dd544849-rds8v                  1/1     Running     0               19m
default          hello-world-rapp-58f767549d-xnw8d                   1/1     Running     0               45h
default          nfs-subdir-external-provisioner-546d9f945-cm9w9     1/1     Running     0               17h
default          quick-check-rapp-59c9fc5c8d-b9vtn                   1/1     Running     0               45h
```
### Get URL
```bash
export NODE_PORT=$(kubectl get --namespace default -o jsonpath="{.spec.ports[0].nodePort}" services clearml)
export NODE_IP=$(kubectl get nodes --namespace default -o jsonpath="{.items[0].status.addresses[0].address}")
echo http://$NODE_IP:$NODE_PORT
```
output (Problem):
```bash
root@node1:~# export NODE_PORT=$(kubectl get --namespace default -o jsonpath="{.spec.ports[0].nodePort}" services clearml)
Error from server (NotFound): services "clearml" not found
root@node1:~# export NODE_IP=$(kubectl get nodes --namespace default -o jsonpath="{.items[0].status.addresses[0].address}")
root@node1:~# echo http://$NODE_IP:$NODE_PORT
http://192.168.0.237:
```
Troubleshoot:
```bash
root@node1:~# kubectl get services --all-namespaces | grep clearml
default       clearml-apiserver                       NodePort    10.233.13.105   <none>        8008:30008/TCP                                 31m
default       clearml-elastic-master                  ClusterIP   10.233.34.84    <none>        9200/TCP,9300/TCP                              31m
default       clearml-elastic-master-headless         ClusterIP   None            <none>        9200/TCP,9300/TCP                              31m
default       clearml-fileserver                      NodePort    10.233.43.215   <none>        8081:30081/TCP                                 31m
default       clearml-mongodb                         ClusterIP   10.233.46.136   <none>        27017/TCP                                      31m
default       clearml-redis-headless                  ClusterIP   None            <none>        6379/TCP                                       31m
default       clearml-redis-master                    ClusterIP   10.233.12.51    <none>        6379/TCP                                       31m
default       clearml-webserver                       NodePort    10.233.15.146   <none>        8080:30080/TCP                                 31m
```
```bash
export NODE_PORT=$(kubectl get --namespace default -o jsonpath="{.spec.ports[0].nodePort}" services clearml-webserver)
export NODE_IP=$(kubectl get nodes --namespace default -o jsonpath="{.items[0].status.addresses[0].address}")
echo http://$NODE_IP:$NODE_PORT
```
output URL:
```bash
http://192.168.0.237:30080
```
result:
![image](https://hackmd.io/_uploads/Hyn3yLkY0.png)
Full Name: **AIMLFW-SMO**

## ClearML-Agent Installation and Deployment
A ClearML Agent is always related to a ClearML server ecosystem (by default using the app.clear.ml hosted server, but can be on the same or different Kubernetes cluster or a single server installation).

In the ClearML UI, go to Settings > Workspace and click Create New Credentials. The dialog that pops up displays the new credentials.

In the Helm chart install command below:
* Set `ACCESSKEY` to the new credentials' `access_key` value
* Set `SECRETKEY` to the new credentials' `secret_key` value
* Set `APISERVERURL` to the new credentials' `api_server` value
* Set `FILESSERVERURL` to the new credentials' `files_server` value
* Set `WEBSERVERURL` to the new credentials' `web_server` value

For example after creating credentials it will show:
For local Python:
```bash
api {
  web_server: http://192.168.0.237:30080/
  api_server: http://192.168.0.237:30008
  files_server: http://192.168.0.237:30081
  credentials {
    "access_key" = "H6SR4BLLTME81X09REWVH7PXMSBZK9"
    "secret_key" = "2QQhstAS3LJTb8TDH4eMjd5XmOh8IeBl4AYNt2U6LW5NBSKy-niGGA7EgV3gxF243co"
  }
}
```
For Jupyter Notebook:
```bash
%env CLEARML_WEB_HOST=http://192.168.0.237:30080/
%env CLEARML_API_HOST=http://192.168.0.237:30008
%env CLEARML_FILES_HOST=http://192.168.0.237:30081
%env CLEARML_API_ACCESS_KEY=H6SR4BLLTME81X09REWVH7PXMSBZK9
%env CLEARML_API_SECRET_KEY=2QQhstAS3LJTb8TDH4eMjd5XmOh8IeBl4AYNt2U6LW5NBSKy-niGGA7EgV3gxF243co
```
Command:
```bash
helm install clearml-agent allegroai/clearml-agent --set clearml.agentk8sglueKey=ACCESSKEY --set clearml.agentk8sglueSecret=SECRETKEY --set agentk8sglue.apiServerUrlReference=APISERVERURL --set agentk8sglue.fileServerUrlReference=FILESERVERURL --set agentk8sglue.webServerUrlReference=WEBSERVERURL
```
output:
```bash
root@node1:~# helm install clearml-agent allegroai/clearml-agent --set clearml.agentk8sglueKey=H6SR4BLLTME81X09REWVH7PXMSBZK9 --set clearml.agentk8sglueSecret=2QQhstAS3LJTb8TDH4eMjd5XmOh8IeBl4AYNt2U6LW5NBSKy-niGGA7EgV3gxF243co --set agentk8sglue.apiServerUrlReference=http://192.168.0.237:30008 --set agentk8sglue.fileServerUrlReference=http://192.168.0.237:30081 --set agentk8sglue.webServerUrlReference=http://192.168.0.237:30080/
NAME: clearml-agent
LAST DEPLOYED: Thu Jul 25 04:26:26 2024
NAMESPACE: default
STATUS: deployed
REVISION: 1
TEST SUITE: None
NOTES:
Glue Agent deployed.
```

## Install ClearML Python Libraries
```bash
python3 --version
pip install clearml
```

## References
* https://clear.ml/docs/latest/docs/deploying_clearml/clearml_server_kubernetes_helm
* https://github.com/allegroai/clearml-helm-charts/blob/main/INSTALL.md
* https://clear.ml/docs/latest/docs/