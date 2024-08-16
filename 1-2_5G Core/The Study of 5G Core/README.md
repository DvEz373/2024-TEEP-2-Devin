# 5G Core - The Study of 5G Core
- [5G Core - The Study of 5G Core](#5g-core---the-study-of-5g-core)
  - [1. 5G Core](#1-5g-core)
    - [1.1. What is 5G Core](#11-what-is-5g-core)
    - [1.2. Difference Between 5G Network and 5GC Network Architechture](#12-difference-between-5g-network-and-5gc-network-architechture)
    - [1.3. Main Components in 5G Core](#13-main-components-in-5g-core)
    - [1.4. User Plane Function (UPF)](#14-user-plane-function-upf)
    - [1.5. Unified Data Repository (UDR)](#15-unified-data-repository-udr)
    - [1.6. Unified Data Management (UDM)](#16-unified-data-management-udm)
    - [1.7. Access and Mobility Management Function (AMF)](#17-access-and-mobility-management-function-amf)
    - [1.8. Authentication Server Function (AUSF)](#18-authentication-server-function-ausf)
    - [1.9. Session Management Function (SMF)](#19-session-management-function-smf)
    - [1.10. Network Slice Selection Function (NSSF)](#110-network-slice-selection-function-nssf)
    - [1.11. Network Exposure Function (NEF)](#111-network-exposure-function-nef)
    - [1.12. NF Repository Function (NRF)](#112-nf-repository-function-nrf)
    - [1.13. Policy Control function (PCF)](#113-policy-control-function-pcf)
    - [1.14. Application Function (AF)](#114-application-function-af)
    - [1.15. Data Network (DN)](#115-data-network-dn)

## 1. 5G Core
![image](https://hackmd.io/_uploads/H15Xrc1Fa.png)

### 1.1. What is 5G Core
<div class="text-justify">

The 5G core network is a cloud-aligned, service-based architecture that encompasses all 5G functions and interactions such as authentication, security, session management and traffic aggregation from end devices. It is completely software-based and native to the cloud, which allows for higher deployment agility and flexibility similar to the cloud. The 5G core network is designed to support the network functions of the 5G network, therefore, the 3GPP standard was developed which was named 5G core, it has the capability to control and manage network functions. The 5G core network architecture emphasizes the use of Network Function Virtualization (NFV) with virtualized software functions deployed using the Multi-access Edge Computing (MEC) infrastructure, which is central to 5G architectural principles. 

</div>

### 1.2. Difference Between 5G Network and 5GC Network Architechture
<div class="text-justify">
    
The 5G network consists of two primary components: the 5G access network (5G-AN) and the 5G core network (5GC). The 5G core network, also known as 5GC, is a key part of the 5G system and enables advanced functionality. It is based on a cloud-aligned, service-based architecture (SBA) that supports authentication, security, session management, and aggregation of traffic from connected devices. The 5G core emphasizes virtualization and cloud-native software design, allowing for greater flexibility and decentralization of network functions. On the other hand, the ordinary 5G network, which includes the 5G access network, is responsible for connecting user equipment (UE) to the core network and providing access to 5G services. It is important to note that the 5G core network is a fundamental part of the 5G system, enabling the advanced capabilities of 5G, while the ordinary 5G network encompasses the access network and user equipment, facilitating connectivity and access to 5G services.
For a more detailed comparison, the 5G core network (5GC) architecture differs from the ordinary 5G network in the following ways:
* **Service-Based Architecture (SBA)**: The 5GC is based on a cloud-aligned, service-based architecture (SBA) that spans across all 5G functions and interactions, emphasizing modularity, reusability, and virtualized software functions deployed using the MEC (Multi-Access Edge Computing) infrastructure.
* **Virtualization and Cloud-Native Design**: The 5GC leverages virtualization and cloud-native software design at unprecedented levels, allowing for greater flexibility, decentralization of network functions, and the ability to run independently on off-the-shelf server hardware.
* **Network Slicing**: The 5GC enables network slicing, allowing for the creation of multiple logical "slices" of functionality optimized for specific applications, such as high bandwidth, low latency, or massive IoT (Internet of Things) devices.
</div>

### 1.3. Main Components in 5G Core
<div class="text-justify">
    
![image](https://hackmd.io/_uploads/H1YLBcyKT.png)
1. **User Plane Function (UPF)**: responsible for packet forwarding and routing, as well as traffic management and optimization.
2. **Unified Data Repository (UDR)**: responsible for managing the registration of network functions that serve the User Equipment (UE). It stores the Authentication Management Functions (AMFs) for the UE, as well as Session Management Functions (SMFs) per Packet Data Unit (PDU) session.
3. **Unified Data Management (UDM)**: responsible for managing network user data, similar to the 4G network’s Home Subscriber Service (HSS), however, it is specifically built for 5G and is cloud-based. It can be paired with the User Data Repository (UDR) that stores user data such as customer profiles, authentication information, and encryption keys.
4. **Access and Mobility Management Function (AMF)**: responsible for managing the mobility of the UE, as well as the establishment and release of connections between the UE and the network.
5. **Authentication Server Function (AUSF)**: responsible for authenticating the UE and generating the security keys used for encryption and decryption.
6. **Session Management Function (SMF)**: responsible for managing the UE's data sessions, including the establishment, modification, and termination of sessions.
7. **Network Slice Selection Function (NSSF)**: responsible for selecting the appropriate network slice for the UE based on the service requirements.
8. **Network Exposure Function (NEF)**: responsible for exposing network services to authorized third-party applications.
9. **NF Repository Function (NRF)**: responsible for maintaining a repository of network functions and their associated metadata.
10. **Policy Control function (PCF)**: responsible for enforcing policies related to Quality of Service (QoS), charging, and access control.
11. **Application Function (AF)**: responsible for providing network services to third-party applications.
12. **Data network (DN)**: responsible for providing operator services, Internet access, or 3rd party services.

The 5G core network has numerous essential functions for mobile networking like mobile management, subscriber data management, authorization, authentication policy management, and more. The key advantages of 5G technology are faster data transmission speeds of up to multi-Gigabit/s, greater capacity to support a large number of IoT devices per square kilometer and lower latency of down to single-digit milliseconds, which is critical for applications such as connected vehicles in ITS applications and autonomous vehicles where near instantaneous response is necessary. 

</div>

### 1.4. User Plane Function (UPF)
![image](https://hackmd.io/_uploads/SyyUOaEY6.png)
<div class="text-justify">
    
The User Plane Function (UPF) is a fundamental component of the 3GPP's New Radio (NR) mobile core infrastructure system architecture and is a primary network function (NF) of the 5G core network (5GC). It is responsible for processing all network data and plays a crucial role in enabling low latency and high throughput in the 5G network. The UPF is part of the Service-Based Architecture (SBA) in the 5G Core and is designed to work with cloud-native technologies.
Key responsibilities of the UPF include:
1. **Radio Access Network (RAN)/Data Network (DN) interconnect**: The UPF connects the RAN and the DN, enabling seamless communication between the two networks.
2. **Packet inspection and application detection**: The UPF inspects packets and detects various applications, ensuring that only authorized applications are allowed to access the network.
3. **Packet routing and data forwarding**: The UPF is responsible for routing and forwarding data packets between the RAN and the DN, ensuring efficient and reliable data transmission.
4. **Quality of Service (QoS) management and usage reporting**: The UPF manages QoS parameters and provides usage reports, ensuring that the network meets the required performance standards.
5. **Interconnection to the Data Network**: The UPF interconnects the 5G network with the data network, enabling seamless communication between the two networks.
6. **Policy enforcement and data buffering**: The UPF enforces policies and manages data buffering, ensuring that network resources are used efficiently and effectively.

The UPF is designed to work with cloud-native technologies and can be deployed close to the edge or in central data centers. This deployment approach enables multi-access edge computing (MEC), which delivers resources at the edge to support new low-latency, ultra-reliable, and mass-volume 5G applications. The UPF is also responsible for the most accurate application classification on the market, with broad protocol/application coverage and unique coverage of IoT/IIoT, M2M/SCADA, and Cloud/SaaS apps.
</div>

### 1.5. Unified Data Repository (UDR)
![image](https://hackmd.io/_uploads/HyWjup4Fp.png)
<div class="text-justify">
    
The Unified Data Repository (UDR) is a centralized database in the 5G Core network that stores various types of data related to user subscriptions, including subscription data, policy data, structured data for exposure, and application data. It is similar to the 4G Home Subscriber Service (HSS) but is cloud-native and designed for 5G. The UDR works in conjunction with the Unified Data Management (UDM) and other network functions, such as the Access and Mobility Management Function (AMF), Session Management Function (SMF), Authentication Server Function (AUSF), and Policy Control Function (PCF).

Key features and functions of the UDR include:
1. **Storage and retrieval of subscription data**: The UDR stores and manages subscription-related information, such as customer authentication information and encryption keys for the information.
2. **Storage and retrieval of policy data**: The UDR stores and retrieves policy data, which is used to manage user sessions on the network and allocate IP addresses.
3. **Storage and retrieval of structured data for exposure**: The UDR stores and retrieves structured data for exposure, which can be used for various 5G applications and services.
4. **Storage and retrieval of application data**: The UDR stores and retrieves application data, including Packet Flow Descriptions (PFDs) for application request information for multiple users.
5. **Subscription to notification and notification of subscribed data changes**: The UDR supports notifications and data changes, allowing network functions to stay updated on user subscription data.
6. **Flexible URI support**: Users can define new URIs for any resource at runtime for basic CRUD (Create, Read, Update, Delete) operations on the resource.
7. **Support for multi-keys**: The UDR supports multiple keys for a subscriber, providing flexibility in defining new keys.
8. **Runtime schema validation**: Users can modify and validate the schema in use for data storage without service restart, allowing for schema versioning.
9. **Provisioning support via REST/JSON**: The UDR provides provisioning APIs for creating subscribers and adding PCF data.

The UDR is an essential component of the 5G Core network, providing a centralized and efficient way to manage user data and enable secure network access.
</div>

### 1.6. Unified Data Management (UDM)
![image](https://hackmd.io/_uploads/r10d_6NY6.png)
<div class="text-justify">
    
Unified Data Management (UDM) is a centralized way to control network user data in the 5G Core network. It is similar to the 4G network's Home Subscriber Service (HSS) but is cloud-native and designed for 5G. The UDM manages access authorization, user registration, and data network information. It works in conjunction with the Unified Data Repository (UDR), which stores user data such as customer authentication information and encryption keys for the information. The UDM resides on the control plane and utilizes microservices to communicate between the user plane and the UDR (when it is a stateless architecture). The UDM generates authentication credentials used during the authentication process, authorizes network access and roaming based on user subscriptions, and handles subscription management and privacy protection by SUCI to SUPI. The UDM also handles inter- and intra-RAT mobility. The UDM offers services to the Access and Mobility Management Function (AMF), Session Management Function (SMF), Short Message Service Function (SMSF), Authentication Server Function (AUSF), and more, via the Nudm service-based interface. The UDM is a critical component of the 5G Core network, providing a centralized and efficient way to manage user data and enable secure network access.
</div>

### 1.7. Access and Mobility Management Function (AMF)
![image](https://hackmd.io/_uploads/r1TTda4ta.png)
<div class="text-justify">

The Access and Mobility Management Function (AMF) is a control plane function in the 5G core network that handles connection and management mobility. It is responsible for managing access and mobility for 5G devices and interacts with other network functions such as the User Plane Function (UPF), Session Management Function (SMF), and Authentication Server Function (AUSF). The main functions and responsibilities of AMF are:
1. **Registration Management**: This allows 5G devices to register with the network and assigns them a unique temporary identifier called 5G-GUTI.
2. **Reachability Management**: AMF is responsible for tracking the location of 5G devices and managing their mobility, ensuring that devices maintain connectivity as they move through different areas of the network.
3. **Connection Management**: AMF manages the establishment and release of PDU sessions, working in conjunction with the SMF.
4. **Mobility Management**: AMF is responsible for managing handovers between gNodeBs (gNBs) within the Next Generation Radio Access Network (NG-RAN). It also performs access management functions such as authentication, authorization, and accounting (AAA) for 5G devices, verifying their identity and determining whether they are authorized to access the network.
5. **Security and Access Management**: AMF works with AUSF and UDM to authenticate and authorize users, enforcing security policies and ensuring that devices are charged appropriately for their usage.
6. **Network Optimization**: AMF plays a key role in optimizing the 5G network for performance and efficiency, monitoring network usage and adapting network resources to meet the network's needs.
The AMF is a critical component in the 5G core network, managing access, mobility, and security for 5G devices while interacting with other network functions to ensure seamless and secure network access.
</div>

### 1.8. Authentication Server Function (AUSF)
![image](https://hackmd.io/_uploads/S1cHtpNK6.png)
<div class="text-justify">
    
The Authentication Server Function (AUSF) is a critical component of the 5G network architecture, responsible for validating the identity of a user and providing access to the network resources based on their security level. The AUSF plays a crucial role in ensuring the security and reliability of the 5G network by performing the following functions:
1. **Authentication**: The AUSF authenticates the user's identity, ensuring that only authorized users can access the network resources.
2. **Authorization**: It authorizes the user's access to the network resources based on their security level, ensuring compliance with the network's security and privacy policies.
3. **Security Management**: The AUSF monitors the network for security threats and vulnerabilities, taking appropriate measures to ensure that the network is secure and protected from cyber-attacks and other security threats.
4. **Key Management**: It generates and distributes cryptographic keys to the user and the network elements, ensuring the confidentiality and integrity of the user's data.
5. **UE Policy Control**: The AUSF controls the policies that govern the user's access to the network resources, ensuring compliance with the network's security and privacy policies, and preventing unauthorized access and data breaches.
6. **Support for 5G Authentication and Authorization**: One of the primary functions of the AUSF is to support 5G authentication and authorization. When a subscriber attempts to connect to the 5G network, the AUSF verifies their identity and ensures that they have the proper authorization.

The AUSF receives authentication requests from the Access and Mobility Management Function (AMF) and validates network responses to determine whether the authentication was successful. It is also responsible for the security procedure for SIM authentication using the 5G-AKA authentication method.
AUSF is a key element in 5G mobile networks, providing authentication and authorization services to ensure secure and authorized access to the network resources.
</div>

### 1.9. Session Management Function (SMF)
![image](https://hackmd.io/_uploads/BJm_t6EFT.png)
<div class="text-justify">
    
5G Session Management Function (SMF) is a critical component of the 5G core network that performs several fundamental tasks, including:
1. **PDU Session Management**: SMF is responsible for managing the Protocol Data Unit (PDU) sessions between user devices and the network, including their establishment, modification, and release.
2. **IP Address Allocation**: SMF manages the allocation of IP addresses for user devices.
3. **GTP-U Tunnel Management**: SMF is responsible for managing the GTP-U tunnels between user devices and the network.
4. **Downlink Notification Management**: SMF manages the downlink notifications between user devices and the network.
5. **Policy Integration**: SMF interacts with other network functions such as Access and Mobility Management Function (AMF), Policy Control Function (PCF), and User Plane Function (UPF) to establish and manage sessions.
6. **Network Slicing Support**: SMF supports the concept of network slicing, where multiple logical networks can be created on top of a single physical network infrastructure.
7. **Mobility Management**: SMF provides support for mobility management, including handovers between 5G cells and inter-system handovers between 5G and other access technologies.
8. **Security Functions**: SMF is responsible for providing security functions such as encryption and decryption of user data and for enforcing security policies.
9. **Deployment Support**: SMF supports different deployment scenarios, including centralized and distributed deployment models.
10. **Traffic Steering and Offloading**: SMF supports different types of traffic steering and traffic offloading mechanisms, including the authentication of devices connecting to the network.

SMF is designed to be highly scalable and resilient, with the ability to handle a large number of sessions simultaneously and to provide redundancy and failover mechanisms. It can be implemented as a standalone function or as a combined function with other network elements.
</div>

### 1.10. Network Slice Selection Function (NSSF)
![image](https://hackmd.io/_uploads/rkhx96VKp.png)
<div class="text-justify">
    
The Network Slice Selection Function (NSSF) is a critical component of the 5G core network that enables the selection of the Network Slice instances that will serve a particular device. It works together with the Network Repository Function (NRF) to support network slicing capabilities. The NSSF provides network slice information to the Access and Mobility Management Function (AMF) and determines the Allowed Network Slice Selection Assistance Information (NSSAI) that is used to redirect traffic to an intended network slice. It also enables the NSSF to provide the AMF the Allowed NSSAI and the Configured NSSAI for the Network Slice Selection Service. The NSSF is designed to be highly scalable and resilient, with the ability to handle a large number of sessions simultaneously and to provide redundancy and failover mechanisms. It can be implemented as a standalone function or as a combined function with other network elements.
</div>

### 1.11. Network Exposure Function (NEF)
![image](https://hackmd.io/_uploads/Sy6imfSt6.png)
<div class="text-justify">
    
The Network Exposure Function (NEF) is a critical component of the 5G core network that enables third-party applications to access network services and resources. It acts as an interface between network functions and external applications, allowing developers to create innovative services and utilize network resources. Some key functionalities and features of NEF include:
1. **Secure API Exposure**: NEF securely exposes 3GPP Network Function (NF) events and capabilities, such as Application Function (AF) and Edge Computing, to external applications.
2. **Service-Based Architecture**: It is explicitly designed as part of the Core Service-Based Architecture on 5G, allowing external applications to communicate with the 5G Core via APIs.
3. **Network Slicing Support**: NEF plays a role in network slicing, allowing third-party applications to request and utilize network slices with specific requirements, such as low latency for IoT devices or high bandwidth for multimedia services.
4. **Security and Privacy Controls**: NEF provides access to network analytics and insights, allowing developers to optimize their applications and services. It also enables the integration of third-party applications with edge computing resources, reducing latency and improving real-time performance.
5. **Multi-Cloud Experience and Multi-Deployment Options**: NEF supports multiple cloud partners and can be easily deployed independently or adjacent to other solutions, maximizing opportunities based on the evolution stage.
6. **Openness and Integration**: NEF enables the integration and trade of partners and cloud players, providing a cloud-based, microservices-built set of functionalities that delivers the benefits of both internal and external network services and capabilities.

NEF is designed to be highly scalable and resilient, with the ability to handle a large number of sessions simultaneously and to provide redundancy and failover mechanisms. It can be implemented as a standalone function or as a combined function with other network elements.
</div>

### 1.12. NF Repository Function (NRF)
![image](https://hackmd.io/_uploads/H1iyEMBt6.png)
<div class="text-justify">
    
The Network Repository Function (NRF) is a crucial component of the 5G core network that serves as a centralized repository for all the 5G network functions (NFs). It allows 5G NFs to register and discover each other via a standards-based API[1]. The NRF plays a key role in facilitating service discovery and enabling dynamic network function selection. Its main functions include:
1. **Service Discovery and Registration**: NRF serves as a repository for information about network services and functions available within the 5G Core network. Network functions and services register their capabilities and addresses with the NRF during the network's initialization or when they come into existence.
2. **Resource Exposure and Capability Advertisement**: Each network function provides information about its capabilities, supported features, and available resources to the NRF. This information includes details like the supported network slice types and available Quality of Service (QoS).
3. **Load Balancing and Redundancy**: NRF can assist in load balancing by providing information about the current load and resource availability of different instances of the same network function. It facilitates redundancy and failover mechanisms by helping in the discovery of alternative instances of a network function in case of failures or degraded performance.
4. **Support for Network Slicing**: NRF plays a key role in the context of network slicing, helping in identifying and configuring the appropriate network functions and resources for a specific network slice.
5. **Interworking and Interoperability**: NRF ensures interoperability among different network functions and services by maintaining a centralized repository of their capabilities. It helps in establishing communication between diverse network functions and facilitates the creation of end-to-end network services.
    
The NRF is designed to be highly scalable and resilient, with the ability to handle a large number of sessions simultaneously and to provide redundancy and failover mechanisms. It can be implemented as a standalone function or as a combined function with other network elements.
</div>

### 1.13. Policy Control function (PCF)
![image](https://hackmd.io/_uploads/rJhXEGSFT.png)
<div class="text-justify">

The Policy Control Function (PCF) is a critical component of the 5G core network that provides policy rules for control plane functions, including network slicing, roaming, and mobility management. It enables end-to-end policy management based on network parameters, implements slice-based policies for highly specific applications, supports innovation and enrichment through service exposure, and offers advanced analytics for improved services. The PCF is designed to be highly scalable and resilient, with the ability to handle a large number of sessions simultaneously and to provide redundancy and failover mechanisms. It can be implemented as a standalone function or as a combined function with other network elements. The PCF architecture is built on a multi-layer platform, which enables efficient policy control and management in the 5G Core network. It provides policy rules for application and service data flow detection, gating, Quality of Service (QoS), and flow-based charging to the Session Management Function (SMF). The PCF also accesses subscription information for policy decisions taken by the User Data Repository (UDR) and supports the new 5G QoS policy and charging control functions. The PCF plays a critical role in the evolving 5G ecosystem by providing control over the consumption of network resources, managing subscriber spending, and usage control. It also facilitates the creation of end-to-end network services and supports interworking and interoperability among different network functions and services.
</div>

### 1.14. Application Function (AF)
![image](https://hackmd.io/_uploads/B1Ej8QIYp.png)
<div class="text-justify">
    
The Application Function (AF) is a control plane function within the 5G core network that provides service-related or application-related information to network function service consumers. It plays a key role in traffic management and Quality of Service (QoS) assignments, through interaction with policy elements. The AF exposes the application layer for interaction with 5G network functions and network resources. It resides in the control plane of the 5G Service-Based Architecture (SBA) and establishes QoS for subscribers to a service or application and interacts with policy charging and rules functions. The AF interacts with numerous interfaces, including the Policy Control Function (PCF), Network Exposure Function (NEF), and UE radio Capability Management Function (UCMF). The AF is designed to be highly scalable and resilient, with the ability to handle a large number of sessions simultaneously and to provide redundancy and failover mechanisms. It can be implemented as a standalone function or as a combined function with other network elements. The AF is a crucial component of the 5G core network that enables the provision of innovative services and utilization of network resources by third-party applications.
</div>

### 1.15. Data Network (DN)
![image](https://hackmd.io/_uploads/HJ2TL7LYp.png)
<div class="text-justify">

The term "Data Network (DN)" in the context of the 3GPP 5G Architecture refers to a telecommunications network that enables the exchange of digital information between devices, and it is related to various services and access types. It can be associated with Service Provider services, Internet access, or third-party services. The DN is a critical component of modern communication infrastructure, allowing the exchange of data among different devices, and it can be classified into different types based on the transmission medium, network topology, and communication protocol used. The components of a DN include devices such as computers, routers, switches, hubs, and servers, as well as transmission media such as copper wires, optical fibers, or wireless links. The main function of a DN is to provide a communication infrastructure that allows data to be exchanged with minimal delay and without loss of information, while being highly reliable and resilient to failures. In the 5G context, the DN is also associated with PDU (Protocol Data Unit) sessions, which provide connectivity to specific Data Network Names (DNNs) such as the Internet, IMS, or other dedicated DNNs for industries or factories. The DN is a fundamental element in the 5G architecture, enabling various types of data communication and access to external data networks. It is designed to be highly scalable and resilient, with the ability to handle a large number of sessions simultaneously and to provide redundancy and failover mechanisms. The DN can be implemented as a standalone function or as a combined function with other network elements, and it is a key enabler for the provision of innovative services and the utilization of network resources by third-party applications.
</div>
