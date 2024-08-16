# <center>🇮🇩 2024-UI-Devin-[Energy Saving in ORAN System] | Naufan Raharya, S.T., M.T., Ph.D.</center>

## Personal Information
* Name: Devin Ezekiel Purba
* Email: ezekiel.devin@gmail.com / devin.ezekiel@ui.ac.id
* Major: Electrical Engineering
* Department: Department of Electrical Engineering
* University: University of Indonesia
* GPA: 3.85/4.00
* Intern Topic: Energy Saving in ORAN System
* Duration:
* Mentor: Kevin
* Portofolio: [Linkedin](https://www.linkedin.com/in/devin-ezekiel/), [CakeResume](https://www.cakeresume.com/me/devin-ezekiel), [Github](https://github.com/DvEz373)
* Calendar:

## Navigation

## System Architechture
![alt text](<sys_arch.png>)

## Road Map 
### Probation Period
1. Technology Background 

   * [x] Networking Programming - API and DB
   * [x] Wireshark and Tshark
   * [x] Networking Programming - IPerf
   * [x] Networking Programming - Ping
   * [x] 5G Core - The study of 5G Core
   * [x] 5G Core - The Installation of 5G Core (free5GC)
   * [x] 5G Core - The Testing of 5G Core (E2E test)
   * [x] 5G ORAN - The Study of ORAN
   * [x] 5G ORAN - The Installation of 5G ORAN
   * [x] 5G ORAN - The Testing of 5G ORAN

2. The Idle Mode Study

   * [x] The Paper study of UE Idle mode
   * [x] The Specification study of UE Idle mode
   * [x] The Study of E2 Protocol
   * [x] The Installation of E2 Protocol
   * [ ] The Testing of E2 Protocol
   * [x] The Study of O1 Protocol
   * [x] The Installation of O1 Protocol
   * [ ] The Testing of O1 Protocol

3. The Energy Saving For ORAN

   * [x] The Testing Environment of ES for ORAN
   * [x] The paper study of UE Idle mode
   * [x] O1 interface install
   * [x] E2 interface install

### Internship Period
- [x] **7/9** study collcet data protocol
    - [x] MQTT、Opendds
    - [x] SNMP、Netconf
    - [x] Restful、VES
- [x] **7/12** build the test environment
    - [x] free5gc [Link](https://free5gc.org/guide/3-install-free5gc/)
    - [x] OAI (DU、CU) [Link](https://gitlab.eurecom.fr/oai/openairinterface5g)
    - [x] SMO [Link](https://hackmd.io/0Cl6tnKHTw-wPo2FOLd4Hw#smo-installation-step)
    - [x] Near RT RIC [Link](https://docs.o-ran-sc.org/projects/o-ran-sc-ric-plt-ric-dep/en/latest/installation-guides.html)
- [x] **7/16** test the interface of module
    - [x] URANSIM connect to free5gc [Link](https://free5gc.org/guide/5-install-ueransim/)
    - [x] OAI connect to free5gc [Link](https://hackmd.io/l4_sVHXRSxiFq68NnPxPkg#OAI-gNB-Installation-Guide)
    - [x] OSC SMO(Non RT RIC) connect to OSC Near RT RIC - A1 [Link](https://hackmd.io/BaJvEp7mQouiGaZQJ3184w#nonrtric-connect-to-real-ric)
    - [x] OSC Non RT RIC connect to rApp - R1 <br>[Link](https://www.youtube.com/watch?v=9xl2ILqVed0&t=806s) <br>[rApp managerment openAPI](https://docs.o-ran-sc.org/projects/o-ran-sc-nonrtric-plt-rappmanager/en/stable/rappmanager-api.html) <br> [SME](https://docs.o-ran-sc.org/projects/o-ran-sc-nonrtric-plt-sme/en/latest/)
- [x] **7/16** show the data on SMO influxDB & grafana [Link](https://hackmd.io/0Cl6tnKHTw-wPo2FOLd4Hw#Deployment-of-dmaap-InfluxDB-adapter-InfluxDB-and-Grafana)
- [x] **7/18** VES <br>[Link](https://docs.onap.org/projects/onap-vnfrqts-requirements/en/latest/Chapter8/ves7_1spec.html#id17)
    - [x] How to collect the data
- [x] **7/23** A1 <br>[A1 Mediator](https://wiki.o-ran-sc.org/display/RICP/A1+Mediator)
    - [x] How to drive policy from Non RT RIC to Near RT RIC
    - [x] How to wrtie the policy
- [ ] **7/23** R1
    - [x] How to write the rApp
    - [ ] what kind of rApp can write  EX: for Qos、abnormal detect
- [ ] **7/23** ClearML
    - [x] Deploy ClearML Server and ClearML Agent in Kubernetes Cluster
    - [ ] Learn how to build and integrate MLOps using ClearML
---

- [ ] combine the AL/ML to do the power saving or traffic sterring.
    - [ ] How to design the framework
    - [ ] Use which AL/ML module . why
    - [ ] Verify the accuracy of the forecast data
    - [ ] Check if RAN control can achieve power saving
- [ ] collect data
    - [ ] How frequently can VES collect data
    - [ ] analyze which protocol collect data performance is good