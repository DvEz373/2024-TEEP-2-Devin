# SMO VES
## SMO VES Collector Install
source:
* https://docs.o-ran-sc.org/en/latest/projects.html#service-managerment-and-orgestration-smo
* https://wiki.o-ran-sc.org/pages/viewpage.action?pageId=35881888
cd 
### Install SMO/VES
```bash
git clone "https://gerrit.o-ran-sc.org/r/smo/ves" && (cd "ves" && mkdir -p `git rev-parse --git-dir`/hooks/ && curl -Lo `git rev-parse --git-dir`/hooks/commit-msg https://gerrit.o-ran-sc.org/r/tools/hooks/commit-msg && chmod +x `git rev-parse --git-dir`/hooks/commit-msg)

cd ves

docker-compose build  // Start building and running
docker-compose up -d  // Use docker-compose down to stop the docker containers
```

### Install Certification
```bash
mkdir ~/ves-certificate  // Create a directory to store the key

openssl genrsa -out vescertificate.key 2048  // Generate a 2048-bit RSA private key
openssl req -new -key vescertificate.key -out vescertificate.csr  // Create a certificate signing request (CSR) using the private key
openssl x509 -req -days 365 -in vescertificate.csr -signkey vescertificate.key -out vescertificate.crt  // Generate a self-signed certificate valid for 365 days
```
Check if installation is successful:
```bash
docker-compose ps
```
output:
```bash
root@node1:~/ves# docker-compose ps
         Name                      Command             State                            Ports
----------------------------------------------------------------------------------------------------------------------
smo-collector            /bin/bash /opt/smo/start.sh   Up       0.0.0.0:9999->9999/tcp,:::9999->9999/tcp
smo-dmaap-adapter        /bin/bash /opt/smo/start.sh   Up       0.0.0.0:5000->5000/tcp,:::5000->5000/tcp
smo-grafana              /run.sh                       Up       0.0.0.0:3000->3000/tcp,:::3000->3000/tcp
smo-influxdb             /entrypoint.sh influxd        Up       0.0.0.0:8086->8086/tcp,:::8086->8086/tcp
smo-influxdb-connector   /bin/bash /opt/smo/start.sh   Up       0.0.0.0:9990->9990/tcp,:::9990->9990/tcp
smo-kafdrop              /kafdrop.sh                   Up       0.0.0.0:29000->9000/tcp,:::29000->9000/tcp
smo-kafka                /etc/confluent/docker/run     Up       0.0.0.0:29092->29092/tcp,:::29092->29092/tcp, 9092/tcp
smo-post-config          /bin/bash /opt/smo/start.sh   Exit 0
smo-zookeeper            /etc/confluent/docker/run     Up       2181/tcp, 2888/tcp, 3888/tcp
```
## SMO VES Collector Testing
```bash
git clone "https://gerrit.o-ran-sc.org/r/oam" && (cd "oam" && mkdir -p `git rev-parse --git-dir`/hooks/ && curl -Lo `git rev-parse --git-dir`/hooks/commit-msg https://gerrit.o-ran-sc.org/r/tools/hooks/commit-msg && chmod +x `git rev-parse --git-dir`/hooks/commit-msg)

cd /oam/code/client-scripts-ves-v7  // Enter the directory to modify the config file
```
Modify the config file: `sudo nano config`:
```bash
################################################################################
# DCAE VES Collector communication end point
# urlVes=https://smo.o-ran-sc.org:8443/eventListener/v7
urlVes=https://192.168.0.237:9999/eventListener/v7
basicAuthVes=user:password

################################################################################

```
Execute the `_exampl.sh` file: `./_example.sh`
result: There will be 202 success and 500 failure, and some screenshots.

Modify the `config.yaml` file: `sudo nano config.yaml`:
```bash
################################################################################
# DCAE VES Collector communication end point
vesEndpoint:
  # url: https://localhost:8443/eventListener/v7
  url: https://192.168.0.237:9999/eventListener/v7
  username: user
  password: password
  verify: False

################################################################################
```
checking results:
```bash
python3 sendVesHeartbeat.py
```

## SMO VES Client Install
[integration-simulators-nf-simulator](https://github.com/onap/integration-simulators-nf-simulator-ves-client)
```bash
git clone https://github.com/onap/integration-simulators-nf-simulator-ves-client
cd integration-simulators-nf-simulator-ves-client
docker-compose up -d
mvn clean install -P docker
```
Error:
```bash
Pulling ves-client (onap/org.onap.integration.nfsimulator.vesclient:)...
ERROR: manifest for onap/org.onap.integration.nfsimulator.vesclient:latest not found: manifest unknown: manifest unknown
```
Troubleshoot: Modify `nano docker-compose.yml` file
After, go to the docker website to search for `onap/org.onap.integration.nfsimulator.vesclientavailable` versions. **Add version 1.0.1**
```bash
  ves-client:
    image: onap/org.onap.integration.nfsimulator.vesclient:1.0.1
    ports:
      - "5000:5000"
    networks:
      - nf-simulator-network
    environment:
      USE_CERTIFICATE_FOR_AUTHORIZATION: "false"
    volumes:
      - ./logs:/var/log
      - ./templates:/app/templates
      - ./store:/app/store
      - ./src/main/resources/application.properties:/app/application.properties
    restart: on-failure
    depends_on:
      - mongo
      - mongo-express
```
output:
```bash
Status: Downloaded newer image for onap/org.onap.integration.nfsimulator.vesclient:1.0.1
Creating integration-simulators-nf-simulator-ves-client_mongo-express_1 ... done
Creating integration-simulators-nf-simulator-ves-client_mongo_1         ... done
Creating integration-simulators-nf-simulator-ves-client_ves-client_1    ...
Creating integration-simulators-nf-simulator-ves-client_ves-client_1    ... error

ERROR: for integration-simulators-nf-simulator-ves-client_ves-client_1  Cannot start service ves-client: driver failed programming external connectivity on endpoint integration-simulators-nf-simulator-ves-client_ves-client_1 (f0585b3e642278d09abfe7c6cb972b24816c86279f818d1ff81b6d7557ec1ba4): Bind for 0.0.0.0:5000 failed: port is already allocated

ERROR: for ves-client  Cannot start service ves-client: driver failed programming external connectivity on endpoint integration-simulators-nf-simulator-ves-client_ves-client_1 (f0585b3e642278d09abfe7c6cb972b24816c86279f818d1ff81b6d7557ec1ba4): Bind for 0.0.0.0:5000 failed: port is already allocated
ERROR: Encountered errors while bringing up the project.
```
```bash
root@node1:~/integration-simulators-nf-simulator-ves-client# mvn clean install -P docker
[INFO] Scanning for projects...
Downloading from central: https://repo.maven.apache.org/maven2/org/onap/oparent/oparent/2.1.0/oparent-2.1.0.pom
[ERROR] [ERROR] Some problems were encountered while processing the POMs:
[FATAL] Non-resolvable parent POM for org.onap.integration.simulators.nf-simulator.ves-client:vesclient:1.0.1-SNAPSHOT: Could not find artifact org.onap.oparent:oparent:pom:2.1.0 in central (https://repo.maven.apache.org/maven2) and 'parent.relativePath' points at wrong local POM @ line 27, column 13
 @
[ERROR] The build could not read 1 project -> [Help 1]
[ERROR]
[ERROR]   The project org.onap.integration.simulators.nf-simulator.ves-client:vesclient:1.0.1-SNAPSHOT (/root/integration-simulators-nf-simulator-ves-client/pom.xml) has 1 error
[ERROR]     Non-resolvable parent POM for org.onap.integration.simulators.nf-simulator.ves-client:vesclient:1.0.1-SNAPSHOT: Could not find artifact org.onap.oparent:oparent:pom:2.1.0 in central (https://repo.maven.apache.org/maven2) and 'parent.relativePath' points at wrong local POM @ line 27, column 13 -> [Help 2]
[ERROR]
[ERROR] To see the full stack trace of the errors, re-run Maven with the -e switch.
[ERROR] Re-run Maven using the -X switch to enable full debug logging.
[ERROR]
[ERROR] For more information about the errors and possible solutions, please read the following articles:
[ERROR] [Help 1] http://cwiki.apache.org/confluence/display/MAVEN/ProjectBuildingException
[ERROR] [Help 2] http://cwiki.apache.org/confluence/display/MAVEN/UnresolvableModelException
```

## SMO O1 Interface Install
source: https://wiki.o-ran-sc.org/pages/viewpage.action?pageId=35881890

### prerequisites
* docker
* docker-compose
* java,version 11 or newer

### Install O1 interface
```bash
unzip o1-netconf.zip  // Download the file from the website and unzip it

cd client
docker-compose up -d  // Run the service in detached mode
```
Enter `docker-compose ps`, check docker status.
result:
```bash
root@node1:~/client# docker-compose ps
 Name               Command               State                                         Ports
------------------------------------------------------------------------------------------------------------------------------------
sdnr     /bin/sh -c /opt/onap/sdnc/ ...   Up      0.0.0.0:8101->8101/tcp,:::8101->8101/tcp, 0.0.0.0:8181->8181/tcp,:::8181->8181/tcp
sdnrdb   /tini -- /usr/local/bin/do ...   Up      9200/tcp, 9300/tcp
```

### Access details
Access the GUI and RESTCONF interface using the following URLs, credentials are common for both of them.
* username:admin 
* password:Kp8bJ4SXszM0WXlhak3eHlcse2gAw84vaoGGmJvUy2U
GUI: `http://192.168.0.237:8181/odlux/index.html`
Restconf: `http://192.168.0.237:8181/apidoc/explorer/index.html`

### Use GUI let netconf client connect to netconf server result
[Official Documents](https://docs.o-ran-sc.org/projects/o-ran-sc-oam/en/latest/overview.html)
1. Enter the page->connect->Add
2. Enter:
    * name
    * The netconf server IP you want to connect to 
    * The port of the target machine netconf
    * username/password (Use ssh to enter netconf username/password)
    * ![image](https://hackmd.io/_uploads/HkfKAKNt0.png)
3. Click connect->connection status log to observe whether the target machine is connected. (Still Mounted) ![image](https://hackmd.io/_uploads/Hy_s0FNtR.png)

## SMO O1 interface test
source: https://wiki.o-ran-sc.org/display/SMO/How+to+test+the+O1+interface

### prerequisite
* docker
* docker-compose

### Automated test-suite
Test-suite does the following steps
1. Brings up simulators(RU & DU)
2. Brings up SDNR
3. Add simulators to SDNR
4. Checks connectivity status by fetching the capabilities
5. Updates DU and RU config and prints the output Tear down the services

```bash
git clone -b dawn https://gerrit.o-ran-sc.org/r/smo/o1.git
cd o1/
./run_tests.sh
```
result:
```bash
SDNR is up and running

RU is up.

DU is up.

Adding DU simulator
Successfully added device DU

Checking DU simulator

DU simulator is alive.


Adding RU Simulator\n
Successfully added device RU

Checking RU simulator connection
RU simulator is alive.


RU cofig before update
RU config check before update succeeded.


Updating RU config
Successfully updated RU config.


RU config afer update.
RU config after update succeeded.


DU config before update.
DU config before update succeeded.

Updating DU config
Successfully updated DU config.

DU cofig afer update
DU config after update succeeded.

Stopping sdnr   ... done
Stopping sdnrdb ... done
Removing sdnr   ... done
Removing sdnrdb ... done
Removing network smo_integration
Stopping tests_ntsim-ng-o-du_1 ... done
Stopping tests_ntsim-ng-o-ru_1 ... done
Removing tests_ntsim-ng-o-du_1 ... done
Removing tests_ntsim-ng-o-ru_1 ... done
Removing network tests_default

Tests completed
```

To modify the `.env` file, there is a configuration error somewhere.
Enter the following path to `ls -a` view the `.env` hidden file and enter edit mode `nano .env`
Port 10004 should be changed to 10002.
```bash
cd ~/o1/client/tests
ls -a
nano .env
```
change:
```bash
DOCKER_REPO=nexus3.o-ran-sc.org:10002/o-ran-sc/
NTS_MANAGER_PORT=8300
NTS_BUILD_VERSION=1.3.3
```