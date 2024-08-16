# Networking Programming - Wireshark and Tshark
- [Networking Programming - Wireshark and Tshark](#networking-programming---wireshark-and-tshark)
  - [1. Wireshark](#1-wireshark)
    - [1.1. What is Wireshark?](#11-what-is-wireshark)
    - [1.2. Wireshark Features](#12-wireshark-features)
    - [1.3. TCP/IP Model Layers and Protocols](#13-tcpip-model-layers-and-protocols)
    - [1.4. Components in Wireshark](#14-components-in-wireshark)
    - [1.5. Wireshark Headers (Customizable)](#15-wireshark-headers-customizable)
    - [1.6. Wireshark Layout](#16-wireshark-layout)
    - [1.7. Running Wireshark](#17-running-wireshark)
  - [2. Tshark](#2-tshark)
    - [2.1. Running Tshark](#21-running-tshark)
  - [3. So Wireshark or Tshark?](#3-so-wireshark-or-tshark)

## 1. Wireshark
### 1.1. What is Wireshark?

![image](https://hackmd.io/_uploads/rkLsqKY_T.png)
<div class="text-justify">
Wireshark is a popular open-source network protocol analyzer that allows you to capture and analyze the data traveling back and forth on a computer network. It is commonly used for troubleshooting network issues, analyzing network traffic, and for educational purposes. Wireshark supports a wide range of protocols and can be used on various operating systems, including Windows, macOS, and Linux.Wireshark displays data from hundreds of different protocols on all major network types. Data packets can be viewed in real-time or analyzed offline. Wireshark supports dozens of capture/trace file formats, including CAP and ERF. Integrated decryption tools display the encrypted packets for several common protocols, including WEP and WPA/WPA2.
    
To use Wireshark, you can download it for free from the Wireshark Foundation website for both macOS and Windows. Once installed, you can capture and view the data traveling on your network by selecting one or more of the available network connections on your current device. The captured data interface contains three main sections: the packet list pane, the packet details pane, and the packet bytes pane. You can also record the capture by selecting File then Save As or choose an Export option.
</div>

### 1.2. Wireshark Features
There are some features that make Wireshark an important framework for network analysis such as:
1. Packet Capture:
Wireshark captures packets as they traverse a network. It can capture live data from a network interface or read saved capture files.
2. Protocol Support:
Wireshark supports a vast array of protocols, including but not limited to Ethernet, IP, TCP, UDP, HTTP, DNS, DHCP, SSL/TLS, and many more. This makes it versatile for analyzing different types of network traffic.
3. User Interface:
Wireshark has a user-friendly graphical interface that allows users to view and analyze captured packets. The interface is divided into three main panes: the packet list pane, packet details pane, and packet bytes pane.
4. Packet Filtering:
Wireshark allows you to apply filters to focus on specific types of packets. Filters can be based on protocols, source/destination addresses, ports, and more. This helps in narrowing down the analysis to the relevant packets.
5. Colorizing and Marking Packets:
Wireshark uses colorization to highlight different types of packets, making it easier to identify patterns or anomalies. Users can also mark packets for reference.
6. Packet Details:
Wireshark provides detailed information about each captured packet. You can drill down into each packet to view its header and payload, helping you understand the structure of the data.
7. Statistics and Conversations:
Wireshark offers various statistical tools to analyze network traffic. You can view overall statistics as well as specific statistics for protocols. Conversations and endpoints can also be analyzed to understand communication patterns.
8. Exporting Data:
Wireshark allows you to export captured data in various formats, including plain text, CSV, XML, and more. This is useful for sharing or further analysis using other tools.
9. Display and Capture Filters:
Display filters are used to filter packets displayed in real-time, while capture filters determine which packets are captured. These filters help in focusing on specific traffic during analysis.
10. VoIP Analysis:
Wireshark includes features for analyzing Voice over IP (VoIP) traffic. It can decode and display SIP, RTP, and other VoIP protocols.
11. Expert Information:
Wireshark provides expert information to highlight potential issues or anomalies in the captured traffic, helping users identify and troubleshoot problems.
12. Scripting and Automation:
Wireshark supports scripting using Lua, allowing users to automate tasks and customize their analysis.
13. Community Support:
Wireshark has an active community, and there are numerous online resources, forums, and documentation available for users seeking assistance or wanting to enhance their skills.

### 1.3. TCP/IP Model Layers and Protocols
<div class="text-justify">
The TCP/IP model is a conceptual model that describes the communication protocols used on the Internet. It consists of four layers: the Application layer, the Transport layer, the Internet layer, and the Link layer 1. Each layer has its own set of protocols that are used to facilitate communication between devices on a network.
    
* **Application layer**: This layer is responsible for providing services to the user. Protocols used in this layer include HTTP, FTP, SMTP, and DNS.
* **Transport layer**: This layer is responsible for providing end-to-end communication between devices. Protocols used in this layer include TCP and UDP.
* **Internet layer**: This layer is responsible for routing packets between devices. Protocols used in this layer include IP, ICMP, and ARP.
* **Data Link layer**: This layer is responsible for transmitting data over a physical medium. Protocols used in this layer include Ethernet, Wi-Fi, and Bluetooth.

In Wireshark, you can capture and analyze network traffic at any of these layers. When you open a packet capture file in Wireshark, you can see the packet details in the packet list pane. The columns in the packet list pane display various information about each packet, such as the packet number, time, source and destination IP addresses, protocol, length, and a summary of the packet contents 2.
</div>
    
### 1.4. Components in Wireshark
There are some components in Network Analysis with Wireshark that we should know like IP Address, MAC Address, and Ports. 
* An **IP address** is a unique identifier assigned to each device on a network. It is used to identify the source and destination of packets. In Wireshark, you can view the IP address of a packet in the Internet Protocol Version 4 or Internet Protocol Version 6 header.
* A **MAC address** is a unique identifier assigned to network devices like computers, switches, and routers. It is used to mark the source and the destination of a packet. In Wireshark, you can find the source MAC address and destination MAC address of a packet in the Ethernet header. You can also use Wireshark to find MAC addresses by capturing packets and observing their details in the detail pane.
* A **port** is a communication endpoint in an operating system that identifies a specific process or a type of network service. Ports are used to differentiate between different types of network traffic. In Wireshark, you can view the port number of a packet in the Transmission Control Protocol or User Datagram Protocol header.

### 1.5. Wireshark Headers (Customizable)
<div class="text-justify">
Tabs or headers in Wireshark can be customize based on our preferences. For example, my preference settings is to add the delta time header to show the time for a process traffic data packet to take and also the TCP Segment Length. There are more features in the header that can be shown depending on our purpose of using Wireshark.
Here is the example of my header preference:
    
![image](https://hackmd.io/_uploads/BycoDH__T.png)
    
Wireshark is a network protocol analyzer that captures and displays network traffic. When you open a packet capture file in Wireshark, you can see the packet details in the packet list pane. The packet list pane contains a list of all the packets in the capture file, and each packet is displayed as a row in the pane. The columns in the packet list pane display various information about each packet. Some of the header columns in Wireshark:

* No.: The packet number in the capture file.
* Time: The time at which the packet was captured.
* Source: The source IP address of the packet.
* Destination: The destination IP address of the packet.
* Protocol: The protocol used by the packet.
* Length: The length of the packet in bytes.
* Info: A summary of the packet contents.

This header columns can be customized and displayed in the packet list pane by right-clicking on any column header and selecting “Column Preferences”. From there, you can add or remove columns, and change the order of the columns. You can also apply filters to the packet list pane to display only packets that match certain criteria.
In Wireshark, you can use coloring rules to highlight packets in the packet list pane based on various criteria. This can help you quickly identify packets of interest and make it easier to analyze network traffic. By default, Wireshark has predefined coloring rules that are enabled. You can enable or disable these rules by selecting Colorize Packet List from the View menu or by clicking on the Colorize Packet List icon in the icon bar. You can also create your own custom coloring rules by selecting Coloring Rules from the View menu and clicking on the + button to add a new rule. The packet list pane displays various columns that provide information about each packet. You can customize the columns displayed in the packet list pane by right-clicking on any column header and selecting Column Preferences. From there, you can add or remove columns, and change the order of the columns. 
The default coloring rules are as follows:
* Black: This color is used for packets that do not match any of the other coloring rules.
* Blue: This color is used for packets that are part of a TCP conversation.
* Green: This color is used for packets that are part of a UDP conversation.
* Red: This color is used for packets that contain errors.
* Orange: This color is used for packets that contain warnings.
* Magenta: This color is used for packets that match a display filter.
* Dark Green: This color is used for packets that match a color filter.
</div>

### 1.6. Wireshark Layout
![image](https://hackmd.io/_uploads/rJ2JOrOuT.png)
In this layout of my Wireshark application in Windows, there are three main features that we can see which are,
1. **Packet List**, this tab displays all the packets in the current capture file. Each line in the packet list corresponds to one packet in the capture file. If you select a line in this pane, more details will be displayed in the Packet Details and Packet Bytes panes. While dissecting a packet, Wireshark will place information from the protocol dissectors into the columns. There are many different columns available. You can choose which columns are displayed in the preferences. See Section 11.5, “Preferences”. The default columns will show: No., Time, Source, Destination, Protocol, Length, and Info. 
2. **Packet Details**, this tab provides a detailed view of the selected packet. It shows the packet in a tree-like structure, with each layer of the protocol stack represented by a node in the tree. You can expand and collapse nodes to view or hide details. The packet details pane also provides a hex dump of the packet data.
3. **Packet Bytes**, this tab shows the data of the current packet (selected in the Packet List pane) in a hexdump style. Each line contains the data offset, sixteen hexadecimal bytes, and sixteen ASCII bytes

### 1.7. Running Wireshark
Wireshark can be run on Windows operating system or in Linux operating system like Ubuntu. You can run Wireshark on Windows 10 operating system by using the Wireshark application that can be downloaded from: 
[Download Wireshark for Windows](https://2.na.dl.wireshark.org/win64/Wireshark-4.2.2-x64.exe)
If you want to run Wireshark on Linux, you can use virtual machine on Windows like VMWare or VirtualBox or you can also use the Linux OS directly.
In this example, I am going to run it on Linux Ubuntu using VMWare.
1. The first thing that we have to do is install the Wireshark using the command 
`sudo apt install wireshark` on the Ubuntu Terminal.
2. After successfully installing it, we can open Wireshark by typing the command `wireshark` in the terminal, and the application will launch. 
3. Then it will open the same Wireshark application as in Windows. We can choose from what network we want to analyze. In this example because I am using an ethernet, I am going to choose ethernet
![image](https://hackmd.io/_uploads/SJgqRNtu6.png)
4. Then we can analyze the network packet for example by capturing the network traffic.
![image](https://hackmd.io/_uploads/H1XgyBF_6.png)
5. In this example, I am trying to capture the packet that have SYN. The preference I made is that every packet that is in TCP and have SYN will be marked light green. This is the example of the packet details and packet bytes of the specific packet data.
![image](https://hackmd.io/_uploads/rk0c1SYOa.png)

## 2. Tshark
![image](https://hackmd.io/_uploads/SygckiYtO6.png)
Tshark is a command-line-based protocol analyzer tool that captures and analyzes network traffic from a live network. It is a part of the Wireshark package and uses the same packet capture library as Wireshark. Tshark is more ideal for scripting and automation. One of the key advantages of Tshark is the ability to filter packets based on different criteria.

To use Tshark, you can open a terminal window and type `tshark` followed by the appropriate command-line options. The syntax of a capture filter is defined by the pcap library; this syntax is different from the display filter syntax described below, and the filtering mechanism is limited in its abilities. Display filters use the same syntax as display and color filters in Wireshark; a display filter is specified with the `-R` option. Display filters can be specified when capturing or when reading from a capture file. 
These are some basic commands of Tshark that can be used to start analyzing network protocols:
```
tshark -i <interface> -c <count>
tshark -i <interface> -w <filename>
tshark -r <filename> -R <filter>
```
    
### 2.1. Running Tshark
I will be trying to run Tshark in the Linux Ubuntu Terminal. Here are the steps:
1. First we must install the Tshark in Ubuntu by executing the command: 
```bash
sudo apt install tshark
```
Output: (I have already installed it)
```bash
dvnezkl03@ubuntu:~$ sudo apt install tshark
Reading package lists... Done
Building dependency tree       
Reading state information... Done
tshark is already the newest version (3.2.3-1).
0 upgraded, 0 newly installed, 0 to remove and 0 not upgraded.

```

2. After that, we can open TShark by typing the command `sudo tshark -D` in the terminal, and tshark can show interface available for capture network.
```bash
dvnezkl03@ubuntu:~$ sudo tshark -D
Running as user "root" and group "root". This could be dangerous.
1. ens33
2. lo (Loopback)
3. any
4. bluetooth-monitor
5. nflog
6. nfqueue
7. bluetooth0
8. ciscodump (Cisco remote capture)
9. dpauxmon (DisplayPort AUX channel monitor capture)
10. randpkt (Random packet generator)
11. sdjournal (systemd Journal Export)
12. sshdump (SSH remote capture)
13. udpdump (UDP Listener remote capture)
```

3. Here I am using Ethernet, that is why I will choose lo (Loopback) which is ethernet interface in the system. We can use the command `sudo tshark -i lo`
![image](https://hackmd.io/_uploads/H1tDwKtup.png)

Other example is I try to run `sudo tshark -i ens33` because my network right now (based on ifconfig which is the NAT network adapter from the virtual machine is ens33).

Output:
```bash
dvnezkl03@ubuntu:~$ sudo tshark -i ens33
Running as user "root" and group "root". This could be dangerous.
Capturing on 'ens33'
    1 0.000000000 35.232.111.17 → 192.168.137.133 HTTP 202 HTTP/1.1 204 No Content 
    2 0.000171671 192.168.137.133 → 35.232.111.17 TCP 54 36518 → 80 [FIN, ACK] Seq=1 Ack=150 Win=64091 Len=0
    3 0.000348030 35.232.111.17 → 192.168.137.133 TCP 60 80 → 36518 [ACK] Seq=150 Ack=2 Win=64239 Len=0
    4 0.002772382 192.168.137.133 → 192.168.137.2 DNS 100 Standard query 0x4bdb A location.services.mozilla.com OPT
    5 0.002972970 192.168.137.133 → 192.168.137.2 DNS 100 Standard query 0x866b AAAA location.services.mozilla.com OPT
    6 0.270472995 192.168.137.2 → 192.168.137.133 DNS 200 Standard query response 0x4bdb A location.services.mozilla.com CNAME locprod2-elb-us-west-2.prod.mozaws.net A 44.238.194.110 A 52.11.7.173 A 54.148.110.228 OPT
    7 0.470274507 192.168.137.1 → 239.255.255.250 SSDP 217 M-SEARCH * HTTP/1.1 
    8 1.280555920 192.168.137.133 → 192.168.137.2 DNS 87 Standard query 0x60eb A daisy.ubuntu.com OPT
    9 1.280690965 192.168.137.133 → 192.168.137.2 DNS 87 Standard query 0x7681 AAAA daisy.ubuntu.com OPT
   10 1.481412691 192.168.137.1 → 239.255.255.250 SSDP 217 M-SEARCH * HTTP/1.1 
   11 2.495951422 192.168.137.1 → 239.255.255.250 SSDP 217 M-SEARCH * HTTP/1.1 
   12 3.511768575 192.168.137.1 → 239.255.255.250 SSDP 217 M-SEARCH * HTTP/1.1 
   13 5.235960191 192.168.137.133 → 192.168.137.2 DNS 109 Standard query 0x17ba AAAA locprod2-elb-us-west-2.prod.mozaws.net OPT
   14 6.392367880 192.168.137.133 → 192.168.137.2 DNS 87 Standard query 0x7681 AAAA daisy.ubuntu.com OPT
   15 6.392419082 192.168.137.133 → 192.168.137.2 DNS 87 Standard query 0x60eb A daisy.ubuntu.com OPT
   16 6.785315653 VMware_c0:00:08 → Broadcast    ARP 60 Who has 192.168.137.2? Tell 192.168.137.1
   17 7.489967393 192.168.137.2 → 192.168.137.133 DNS 200 Standard query response 0x866b AAAA location.services.mozilla.com SOA ns-1260.awsdns-29.org OPT
   18 7.489967572 192.168.137.2 → 192.168.137.133 DNS 119 Standard query response 0x60eb A daisy.ubuntu.com A 162.213.35.24 A 162.213.35.25 OPT
   19 7.489991092 192.168.137.133 → 192.168.137.2 ICMP 228 Destination unreachable (Port unreachable)
   20 7.491997741 192.168.137.2 → 192.168.137.133 DNS 158 Standard query response 0x7681 AAAA daisy.ubuntu.com SOA ns1.canonical.com OPT
   21 7.492221827 192.168.137.2 → 192.168.137.133 DNS 209 Standard query response 0x17ba AAAA locprod2-elb-us-west-2.prod.mozaws.net SOA ns-1260.awsdns-29.org OPT
   22 7.492493063 192.168.137.133 → 54.148.110.228 TCP 74 37352 → 443 [SYN] Seq=0 Win=64240 Len=0 MSS=1460 SACK_PERM=1 TSval=921101696 TSecr=0 WS=128
   23 7.494901636 192.168.137.2 → 192.168.137.133 DNS 158 Standard query response 0x7681 AAAA daisy.ubuntu.com SOA ns1.canonical.com OPT
   24 7.494920159 192.168.137.133 → 192.168.137.2 ICMP 186 Destination unreachable (Port unreachable)
   25 7.517049769 54.148.110.228 → 192.168.137.133 TCP 60 443 → 37352 [SYN, ACK] Seq=0 Ack=1 Win=64240 Len=0 MSS=1460
   26 7.517091315 192.168.137.133 → 54.148.110.228 TCP 54 37352 → 443 [ACK] Seq=1 Ack=1 Win=64240 Len=0
   27 7.517512085 192.168.137.133 → 54.148.110.228 TLSv1.2 571 Client Hello
   28 7.517708823 54.148.110.228 → 192.168.137.133 TCP 60 443 → 37352 [ACK] Seq=1 Ack=518 Win=64240 Len=0
   29 7.519058811 192.168.137.2 → 192.168.137.133 DNS 119 Standard query response 0x60eb A daisy.ubuntu.com A 162.213.35.24 A 162.213.35.25 OPT
   30 7.519077279 192.168.137.133 → 192.168.137.2 ICMP 147 Destination unreachable (Port unreachable)
   31 7.988205911 54.148.110.228 → 192.168.137.133 TLSv1.2 2654 Server Hello
   32 7.988220769 192.168.137.133 → 54.148.110.228 TCP 54 37352 → 443 [ACK] Seq=518 Ack=2601 Win=62780 Len=0
   33 7.988837133 54.148.110.228 → 192.168.137.133 TLSv1.2 895 Certificate, Server Key Exchange, Server Hello Done
   34 7.988845810 192.168.137.133 → 54.148.110.228 TCP 54 37352 → 443 [ACK] Seq=518 Ack=3442 Win=62780 Len=0
   35 7.990209299 192.168.137.133 → 54.148.110.228 TLSv1.2 129 Client Key Exchange
   36 7.990329695 192.168.137.133 → 54.148.110.228 TLSv1.2 60 Change Cipher Spec
   37 7.990455720 54.148.110.228 → 192.168.137.133 TCP 60 443 → 37352 [ACK] Seq=3442 Ack=593 Win=64240 Len=0
   38 7.990455771 54.148.110.228 → 192.168.137.133 TCP 60 443 → 37352 [ACK] Seq=3442 Ack=599 Win=64240 Len=0
   39 7.990566225 192.168.137.133 → 54.148.110.228 TLSv1.2 99 Encrypted Handshake Message
   40 7.990729972 54.148.110.228 → 192.168.137.133 TCP 60 443 → 37352 [ACK] Seq=3442 Ack=644 Win=64240 Len=0
   41 8.178811657 VMware_c0:00:08 → Broadcast    ARP 60 Who has 192.168.137.2? Tell 192.168.137.1
   42 8.673973462 54.148.110.228 → 192.168.137.133 TLSv1.2 105 Change Cipher Spec, Encrypted Handshake Message
   43 8.674296354 192.168.137.133 → 54.148.110.228 TLSv1.2 270 Application Data
   44 8.674511718 54.148.110.228 → 192.168.137.133 TCP 60 443 → 37352 [ACK] Seq=3493 Ack=860 Win=64240 Len=0
   45 8.674518659 192.168.137.133 → 54.148.110.228 TLSv1.2 85 Application Data
   46 8.674808527 54.148.110.228 → 192.168.137.133 TCP 60 443 → 37352 [ACK] Seq=3493 Ack=891 Win=64240 Len=0
   47 8.789646162 VMware_c0:00:08 → Broadcast    ARP 60 Who has 192.168.137.2? Tell 192.168.137.1
   48 9.209039166 54.148.110.228 → 192.168.137.133 TLSv1.2 634 Application Data
   49 9.320614487 54.148.110.228 → 192.168.137.133 TCP 634 [TCP Retransmission] 443 → 37352 [PSH, ACK] Seq=3493 Ack=891 Win=64240 Len=580
   50 9.320631024 192.168.137.133 → 54.148.110.228 TCP 54 37352 → 443 [ACK] Seq=891 Ack=4073 Win=62780 Len=0
   51 9.794328686 VMware_c0:00:08 → Broadcast    ARP 60 Who has 192.168.137.2? Tell 192.168.137.1
   52 10.359635424 192.168.137.1 → 255.255.255.255 UDP 79 59710 → 27127 Len=37
   53 15.714492476 VMware_c0:00:08 → Broadcast    ARP 60 Who has 192.168.137.2? Tell 192.168.137.1
   54 16.295510689 VMware_c0:00:08 → Broadcast    ARP 60 Who has 192.168.137.2? Tell 192.168.137.1
   55 17.294233319 VMware_c0:00:08 → Broadcast    ARP 60 Who has 192.168.137.2? Tell 192.168.137.1
   56 18.730549096 VMware_c0:00:08 → Broadcast    ARP 60 Who has 192.168.137.2? Tell 192.168.137.1
   57 19.294076536 VMware_c0:00:08 → Broadcast    ARP 60 Who has 192.168.137.2? Tell 192.168.137.1
   58 20.295724665 VMware_c0:00:08 → Broadcast    ARP 60 Who has 192.168.137.2? Tell 192.168.137.1
   59 24.747949417 VMware_c0:00:08 → Broadcast    ARP 60 Who has 192.168.137.2? Tell 192.168.137.1
   60 25.296425850 VMware_c0:00:08 → Broadcast    ARP 60 Who has 192.168.137.2? Tell 192.168.137.1
   61 26.285071209 VMware_c0:00:08 → Broadcast    ARP 60 Who has 192.168.137.2? Tell 192.168.137.1
   62 27.759103848 VMware_c0:00:08 → Broadcast    ARP 60 Who has 192.168.137.2? Tell 192.168.137.1
   63 28.293645087 VMware_c0:00:08 → Broadcast    ARP 60 Who has 192.168.137.2? Tell 192.168.137.1
   64 29.295102755 VMware_c0:00:08 → Broadcast    ARP 60 Who has 192.168.137.2? Tell 192.168.137.1
^C64 packets captured

```

The tshark terminal command outputs a detailed log of network activities similar to Wireshark but in a terminal mode. The main components of the output include:
    1. **Time Information:** Each line starts with a timestamp indicating when the corresponding network activity occurred.
    2. **Source and Destination:** Identifies the source and destination IP addresses or MAC addresses involved in the communication.
    3. **Protocol Information:** Specifies the protocol used in each packet (e.g., TCP, ARP, DNS).
    4. **Packet Details:** Displays specific information about each packet, such as flags, sequence and acknowledgment numbers, window size, and timestamp values for TCP packets.
    5. **Raw Packet Bytes:** Provides the raw hexadecimal representation of the packet’s bytes for in-depth analysis.
    6. **Network Activities:** Includes various network activities such as TCP connections, ARP requests and replies, and DNS queries and responses.
    7. **Interface Specification:** The output specifies the interface (e.g., "wlx7c3d090080c3") from which the capture is performed.
    
4. To explore options in tshark, use the command `tshark --help`, which displays all available options and their functions. Some popular options include:

    - **-c (count):** Specifies the number of packets to capture or display. For example, `tshark -c 10` captures or displays the first 10 packets.
    - **-D:** Lists the available interfaces for capturing traffic. For instance, `tshark -D` provides a list of available network interfaces.
    - **-V:** Enables verbose output, providing more detailed information about each packet. Use `tshark -V` to display packet details with additional verbose information.
    - **-i (interface):** Specifies the network interface for packet capture. For instance, `tshark -i ens33` captures packets on the "ens33" interface.
    - **-r (file):** Reads packets from a specified file instead of capturing live traffic. For example, `tshark -r capturefile.pcap` analyzes packets from the file "capturefile.pcap."
    - **-w (file):** Writes captured packets to a specified file. Use `tshark -w outputfile.pcap` to save captured packets to the file "outputfile.pcap."
    - **-f (capture filter):** Applies a display filter during packet capture. For instance, `tshark -f "tcp port 80"` captures only packets with TCP traffic on port 80.

5. In some other approach, users can effectively combine options to tailor their packet capture and analysis based on specific needs. For example, in the given command `sudo tshark -i lo -c 1 -V`, multiple options work together synergistically. The -i option designates the network interface (here, "lo") for packet capture, the -c option restricts the capture to a specific number of packets (in this instance, just 1 packet), and the -V option activates verbose output, offering detailed information about the captured packet. Through the integration of these options, the user effectively captures a single packet on the specified interface while obtaining comprehensive verbose details for in-depth analysis.
![image](https://hackmd.io/_uploads/B1OVtttO6.png)
![image](https://hackmd.io/_uploads/BJOvYYF_T.png)
![image](https://hackmd.io/_uploads/H1uqFttO6.png)

Here I also try `sudo tshark -i ens33 -c 1 -V`

Output:
```bash
dvnezkl03@ubuntu:~$ sudo tshark -i ens33 -c 1 -V
Running as user "root" and group "root". This could be dangerous.
Capturing on 'ens33'
Frame 1: 92 bytes on wire (736 bits), 92 bytes captured (736 bits) on interface ens33, id 0
    Interface id: 0 (ens33)
        Interface name: ens33
    Encapsulation type: Ethernet (1)
    Arrival Time: Jan 23, 2024 17:55:02.341026471 PST
    [Time shift for this packet: 0.000000000 seconds]
    Epoch Time: 1706061302.341026471 seconds
    [Time delta from previous captured frame: 0.000000000 seconds]
    [Time delta from previous displayed frame: 0.000000000 seconds]
    [Time since reference or first frame: 0.000000000 seconds]
    Frame Number: 1
    Frame Length: 92 bytes (736 bits)
    Capture Length: 92 bytes (736 bits)
    [Frame is marked: False]
    [Frame is ignored: False]
    [Protocols in frame: eth:ethertype:ip:udp:nbns]
Ethernet II, Src: VMware_c0:00:08 (00:50:56:c0:00:08), Dst: Broadcast (ff:ff:ff:ff:ff:ff)
    Destination: Broadcast (ff:ff:ff:ff:ff:ff)
        Address: Broadcast (ff:ff:ff:ff:ff:ff)
        .... ..1. .... .... .... .... = LG bit: Locally administered address (this is NOT the factory default)
        .... ...1 .... .... .... .... = IG bit: Group address (multicast/broadcast)
    Source: VMware_c0:00:08 (00:50:56:c0:00:08)
        Address: VMware_c0:00:08 (00:50:56:c0:00:08)
        .... ..0. .... .... .... .... = LG bit: Globally unique address (factory default)
        .... ...0 .... .... .... .... = IG bit: Individual address (unicast)
    Type: IPv4 (0x0800)
Internet Protocol Version 4, Src: 192.168.137.1, Dst: 192.168.137.255
    0100 .... = Version: 4
    .... 0101 = Header Length: 20 bytes (5)
    Differentiated Services Field: 0x00 (DSCP: CS0, ECN: Not-ECT)
        0000 00.. = Differentiated Services Codepoint: Default (0)
        .... ..00 = Explicit Congestion Notification: Not ECN-Capable Transport (0)
    Total Length: 78
    Identification: 0x203c (8252)
    Flags: 0x0000
        0... .... .... .... = Reserved bit: Not set
        .0.. .... .... .... = Don't fragment: Not set
        ..0. .... .... .... = More fragments: Not set
    Fragment offset: 0
    Time to live: 64
    Protocol: UDP (17)
    Header checksum: 0xc611 [validation disabled]
    [Header checksum status: Unverified]
    Source: 192.168.137.1
    Destination: 192.168.137.255
User Datagram Protocol, Src Port: 137, Dst Port: 137
    Source Port: 137
    Destination Port: 137
    Length: 58
    Checksum: 0xf07a [unverified]
    [Checksum Status: Unverified]
    [Stream index: 0]
    [Timestamps]
        [Time since first frame: 0.000000000 seconds]
        [Time since previous frame: 0.000000000 seconds]
NetBIOS Name Service
    Transaction ID: 0xf91e
    Flags: 0x0110, Opcode: Name query, Recursion desired, Broadcast
        0... .... .... .... = Response: Message is a query
        .000 0... .... .... = Opcode: Name query (0)
        .... ..0. .... .... = Truncated: Message is not truncated
        .... ...1 .... .... = Recursion desired: Do query recursively
        .... .... ...1 .... = Broadcast: Broadcast packet
    Questions: 1
    Answer RRs: 0
    Authority RRs: 0
    Additional RRs: 0
    Queries
        WORKGROUP<1b>: type NB, class IN
            Name: WORKGROUP<1b> (Domain Master Browser)
            Type: NB (32)
            Class: IN (1)

1 packet captured
```

## 3. So Wireshark or Tshark?
<div class="text-justify">
In conclusion, both Wireshark and Tshark offer distinct advantages and drawbacks, catering to different preferences and use cases. Wireshark, with its graphical user interface (GUI), is renowned for its user-friendly nature. The richness of its feature set, including robust filtering options, color-coded packet inspection, and extensive protocol dissection capabilities, makes it a comprehensive tool for network packet analysis. The interactive packet inspection facilitated by Wireshark enables users to delve into specific packets in real-time, fostering a thorough understanding of network traffic. However, Wireshark comes with its own set of cons. Its graphical interface can be resource-intensive, demanding substantial memory and processing power. Additionally, the learning curve may be steep, especially for beginners unfamiliar with the tool's extensive functionalities. The limited command-line capabilities of Wireshark also restrict its scripting and automation potential. On the other hand, Tshark, being command-line-based, offers efficiency for scripting, automation, and remote captures, making it a lightweight alternative to Wireshark. Its resource-friendly nature and scripting capabilities contribute to its appeal, particularly for users prioritizing command-line efficiency. Nonetheless, Tshark is not without its drawbacks. Its command-line interface may pose a challenge for beginners, requiring a learning curve for effective utilization. Moreover, Tshark lacks the interactive and visually appealing features of Wireshark, making it less suitable for users who prefer a GUI for in-depth analysis.

Ultimately, the choice between Wireshark and Tshark hinges on individual preferences, specific use cases, and the level of expertise in network packet analysis. Wireshark stands out for its interactive, visually-driven analysis, while Tshark excels in command-line efficiency and automation. Users may find value in adopting both tools, leveraging each based on their distinct requirements and workflow preferences.
</div>
