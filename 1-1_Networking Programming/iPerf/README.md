# Networking Programming - iPerf
- [Networking Programming - iPerf](#networking-programming---iperf)
  - [1. iPerf](#1-iperf)
    - [1.1. What is iPerf?](#11-what-is-iperf)
    - [1.2. Difference Between TCP/IP and UDP/IP](#12-difference-between-tcpip-and-udpip)
    - [1.3. iPerf Network Bandwidth Checking in Windows](#13-iperf-network-bandwidth-checking-in-windows)
    - [1.4. iPerf Network Bandwidth Checking in Linux](#14-iperf-network-bandwidth-checking-in-linux)
    - [1.5. Result iPerf Network Testing](#15-result-iperf-network-testing)
    - [1.6. Example on Using iPerf](#16-example-on-using-iperf)


## 1. iPerf
### 1.1. What is iPerf?

![image](https://hackmd.io/_uploads/Syu0Hajdp.png)

<div class="text-justify">
    
**Iperf** is an open-source command line tool designed to test network throughput between two network hosts. It can generate TCP and UDP traffic between two hosts and measure the maximum data transfer rate. Iperf works in a client-server mode, where the iPerf starts in server mode on the first device and in client mode on the second computer. 
You can use iPerf to quickly measure the maximum network bandwidth (throughput) between a server and a client, and conduct stress testing of the ISP link, router, network gateway (firewall), your Ethernet, or Wi-Fi network performance. 

To install iPerf on Windows, you can download the executable from the official [website](https://iperf.fr/iperf-download.php). Once downloaded, you can run it on two devices, the network throughput between which needs to be tested. 
</div>

Here is an example of how to use iPerf to test network speed on Windows:
```bash
iperf3.exe -s
iperf3.exe -c <server_ip_address>
```

### 1.2. Difference Between TCP/IP and UDP/IP
<div class="text-justify">
    
TCP/IP and UDP/IP are both protocols of the Internet Protocol suite. TCP (Transmission Control Protocol) is a connection-oriented protocol, while UDP (User Datagram Protocol) is a connectionless protocol. 
* TCP is designed to provide reliable delivery services and is used for applications that require error-free data transmission, such as email, file transfer, and web browsing. It establishes a connection between the sender and receiver and ensures that all data is delivered in the correct order. TCP also implements an error control mechanism for reliable data transfer and takes into account the level of congestion in the network.
* UDP is designed for applications that require low-latency and loss-tolerating connections, such as online gaming, video conferencing, and live streaming. It is a lightweight protocol that does not establish a connection before data transfer and does not guarantee delivery of data. UDP is used for simple request-response communication when the size of data is less and hence there is lesser concern about flow and error control. It is also suitable for multicasting as it supports packet switching.
</div>
    
    
### 1.3. iPerf Network Bandwidth Checking in Windows
Here is an example of how to use iPerf to test network performance between two hosts in Windows:

1. Install iPerf on both hosts. You can download iPerf for Windows by following this [link](https://iperf.fr/iperf-download.php). If you want to use iPerf on Linux, there are iPerf versions available for Linux and VMware ESXi.
2. Start the iPerf server on one of the hosts by running the following command in the command prompt: 

    ```bash
    iperf3 -s
    ```

    This command starts the iPerf server in server mode and waits for traffic from the iPerf client.

3. On the other host, start the iPerf client by running the following command in the command prompt:

    ```bash
    iperf3 -c <server_ip_address>
    ```

    Replace `<server_ip_address>` with the IP address of the host running the iPerf server.

4. The iPerf client will then generate TCP or UDP traffic and measure the maximum data transfer rate between the two hosts. The results will be displayed in the command prompt.

    Here is an example of what the output might look like:

    ```bash
    Connecting to host <server_ip_address>, port 5201
    [  4] local 192.168.1.2 port 5001 connected to 192.168.1.1 port 5201
    [ ID] Interval           Transfer     Bitrate
    [  4]   0.00-1.00   sec   112 MBytes   941 Mbits/sec
    [  4]   1.00-2.00   sec   112 MBytes   941 Mbits/sec
    [  4]   2.00-3.00   sec   112 MBytes   941 Mbits/sec
    [  4]   3.00-4.00   sec   112 MBytes   941 Mbits/sec
    [  4]   4.00-5.00   sec   112 MBytes   941 Mbits/sec
    [  4]   5.00-6.00   sec   112 MBytes   941 Mbits/sec
    [  4]   6.00-7.00   sec   112 MBytes   941 Mbits/sec
    [  4]   7.00-8.00   sec   112 MBytes   941 Mbits/sec
    [  4]   8.00-9.00   sec   112 MBytes   941 Mbits/sec
    [  4]   9.00-10.00  sec   112 MBytes   941 Mbits/sec
    [ ID] Interval           Transfer     Bitrate
    [  4]   0.00-10.00  sec  1.10 GBytes   941 Mbits/sec         sender
    [  4]   0.00-10.00  sec  1.10 GBytes   941 Mbits/sec         receiver

    ```

    The `Transfer` column shows the amount of data that was transferred during the test interval, and the `Bitrate` column shows the average data transfer rate during the test interval.

For more detailed instructions and examples, you can refer to this [guide](https://woshub.com/testing-network-bandwidth-using-iperf/).

### 1.4. iPerf Network Bandwidth Checking in Linux
Here is an example of how to use iPerf to test network performance in Linux Ubuntu:

1. Install iPerf on your Ubuntu machine by running the following command in the terminal: 

```bash
sudo apt-get install iperf
```

Output:
```bash
dvnezkl03@ubuntu:~$ sudo apt install iperf
[sudo] password for dvnezkl03: 
Reading package lists... Done
Building dependency tree       
Reading state information... Done
iperf is already the newest version (2.0.13+dfsg1-1build1).
0 upgraded, 0 newly installed, 0 to remove and 0 not upgraded.

```


2. Start the iPerf server by running the following command in the terminal:

```bash
iperf -s
```

3. On another machine, run the following command in the terminal to connect to the iPerf server:

```bash
iperf -c <server_ip_address>
```

Replace `<server_ip_address>` with the IP address of the machine running the iPerf server.

4. To test the network performance, you can use various options with the `iperf` command. For example, to check the network performance in server mode, you can use the `-s` option with the `iperf` command. If you want to check the transfer bandwidth size in KBytes/sec, you can use the `-f` option and specify the unit. Here is an example command:

```bash
iperf -s -f K
```

5. You can also check the network performance in client mode by using the `-c` option with the `iperf` command. Here is an example command:

```bash
iperf -c <server_ip_address>
```

6. You can also test the network performance using UDP instead of TCP. To do this, use the `-u` option with the `iperf` command. Here is an example command:

```bash
iperf -u -c <server_ip_address>
```

7. You can also specify the bandwidth for the test using the `-b` option. Here is an example command:

```bash
iperf -u -c <server_ip_address> -b 10m
```

This command will test the network performance using UDP and set the bandwidth to 10 Mbps.

### 1.5. Result iPerf Network Testing

<div class="text-justify">
The results of an iPerf test can be interpreted in several ways. Here are some of the key metrics to look for:

* Transfer: This column shows how much data was transferred during the specified interval. It is measured in bytes or bits depending on the unit specified.
* Bitrate: This column shows the average bitrate of the transfer during the specified interval. It is measured in bits per second (bps) or megabits per second (Mbps).
* Jitter: This column shows the variation in delay between packets. It is measured in milliseconds (ms).
* Packet Loss: This column shows the percentage of packets that were lost during the transfer.

To get a better understanding of the network performance, it is important to look at these metrics over multiple intervals. This can help identify trends and patterns in the data. For example, if the transfer rate is consistently low over multiple intervals, it may indicate a problem with the network connection. Similarly, if the jitter or packet loss is consistently high, it may indicate a problem with the network quality.

It is also important to consider the type of test being performed. For example, a TCP test will measure the throughput of the network, while a UDP test will measure the packet loss and jitter.
</div>

### 1.6. Example on Using iPerf
In this example, I am going to use iPerf to check the network connection between Server (Windows) and Client (Linux Ubuntu). 
1. Start the server in Windows by running `./iperf.exe -s` as shown below in the Powershell. To use Windows Powershell, you can hold shift, right click inside the folder that has been downloaded from the iperf website for windows. 

    Output:
    ```powershell
    PS C:\Users\Acer\Downloads\iperf-3.1.3-win64\iperf-3.1.3-win64> ./iperf3.exe -s
    -----------------------------------------------------------
    Server listening on 5201
    -----------------------------------------------------------

    ```
    Before starting the server, it is recommended to see your IP configuration details of your network by using `ipconfig`

    Output:
    ```powershell
    PS C:\Users\Acer\Downloads\iperf-3.1.3-win64\iperf-3.1.3-win64> ipconfig

    Windows IP Configuration


    Unknown adapter VPN - VPN Client:

    Media State . . . . . . . . . . . : Media disconnected
    Connection-specific DNS Suffix  . :

    Ethernet adapter Ethernet:

    Media State . . . . . . . . . . . : Media disconnected
    Connection-specific DNS Suffix  . :

    Wireless LAN adapter Local Area Connection* 1:

    Media State . . . . . . . . . . . : Media disconnected
    Connection-specific DNS Suffix  . :

    Wireless LAN adapter Local Area Connection* 2:

    Media State . . . . . . . . . . . : Media disconnected
    Connection-specific DNS Suffix  . :

    Ethernet adapter VMware Network Adapter VMnet1:

    Connection-specific DNS Suffix  . :
    Link-local IPv6 Address . . . . . : fe80::2871:5a8f:443e:687e%21
    IPv4 Address. . . . . . . . . . . : 192.168.65.1
    Subnet Mask . . . . . . . . . . . : 255.255.255.0
    Default Gateway . . . . . . . . . :

    Ethernet adapter VMware Network Adapter VMnet8:

    Connection-specific DNS Suffix  . :
    Link-local IPv6 Address . . . . . : fe80::d86e:7a0d:4d62:f4ae%7
    IPv4 Address. . . . . . . . . . . : 192.168.137.1
    Subnet Mask . . . . . . . . . . . : 255.255.255.0
    Default Gateway . . . . . . . . . :

    Wireless LAN adapter Wi-Fi:

    Connection-specific DNS Suffix  . :
    Link-local IPv6 Address . . . . . : fe80::85ba:6e94:fecf:c9dc%19
    IPv4 Address. . . . . . . . . . . : 192.168.245.21
    Subnet Mask . . . . . . . . . . . : 255.255.255.0
    Default Gateway . . . . . . . . . : 192.168.245.125

    Ethernet adapter Bluetooth Network Connection:

    Media State . . . . . . . . . . . : Media disconnected
    Connection-specific DNS Suffix  . :
    ```

2. After that, I will go to my other device which is on Linux Ubuntu and do the same thing as in the Windows but I am going to make this system as the client.
3. After I install iperf on Linux Ubuntu, I tried to connect the client in Linux to the Server that I just made in Windows Powershell by using the command `iperf3 -c <server ip address>` in this case my server IP address is 192.168.245.21

    Output in Linux Ubuntu:
    ```bash
    dvnezkl03@ubuntu:~$ iperf3 -c 192.168.245.21
    Connecting to host 192.168.245.21, port 5201
    [  5] local 192.168.137.133 port 36968 connected to 192.168.245.21 port 5201
    [ ID] Interval           Transfer     Bitrate         Retr  Cwnd
    [  5]   0.00-1.00   sec  41.4 MBytes   347 Mbits/sec    0   65.6 KBytes       
    [  5]   1.00-2.00   sec  41.5 MBytes   348 Mbits/sec    0   65.6 KBytes       
    [  5]   2.00-3.00   sec  41.9 MBytes   351 Mbits/sec    0   65.6 KBytes       
    [  5]   3.00-4.00   sec  42.3 MBytes   356 Mbits/sec    0   65.6 KBytes       
    [  5]   4.00-5.00   sec  41.8 MBytes   349 Mbits/sec    0   65.6 KBytes       
    [  5]   5.00-6.00   sec  41.7 MBytes   350 Mbits/sec    0   65.6 KBytes       
    [  5]   6.00-7.00   sec  44.2 MBytes   371 Mbits/sec    0   65.6 KBytes       
    [  5]   7.00-8.00   sec  41.8 MBytes   351 Mbits/sec    0   65.6 KBytes       
    [  5]   8.00-9.00   sec  45.8 MBytes   384 Mbits/sec    0   65.6 KBytes       
    [  5]   9.00-10.00  sec  42.0 MBytes   352 Mbits/sec    0   65.6 KBytes       
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bitrate         Retr
    [  5]   0.00-10.00  sec   424 MBytes   356 Mbits/sec    0             sender
    [  5]   0.00-10.00  sec   424 MBytes   356 Mbits/sec                  receiver

    iperf Done.

    ```

    This is the result of the iPerf connection
    4. The same thing happens in the server side when both are connected like this

    Output in Windows Powershell:
    ```powershell
    PS C:\Users\Acer\Downloads\iperf-3.1.3-win64\iperf-3.1.3-win64> ./iperf3.exe -s
    -----------------------------------------------------------
    Server listening on 5201
    -----------------------------------------------------------
    Accepted connection from 192.168.245.21, port 32151
    [  5] local 192.168.245.21 port 5201 connected to 192.168.245.21 port 32152
    [ ID] Interval           Transfer     Bandwidth
    [  5]   0.00-1.00   sec  40.9 MBytes   343 Mbits/sec
    [  5]   1.00-2.00   sec  41.5 MBytes   348 Mbits/sec
    [  5]   2.00-3.00   sec  41.8 MBytes   350 Mbits/sec
    [  5]   3.00-4.00   sec  42.4 MBytes   355 Mbits/sec
    [  5]   4.00-5.00   sec  41.6 MBytes   349 Mbits/sec
    [  5]   5.00-6.00   sec  41.6 MBytes   349 Mbits/sec
    [  5]   6.00-7.00   sec  44.3 MBytes   372 Mbits/sec
    [  5]   7.00-8.00   sec  41.8 MBytes   351 Mbits/sec
    [  5]   8.00-9.00   sec  45.6 MBytes   383 Mbits/sec
    [  5]   9.00-10.00  sec  42.0 MBytes   353 Mbits/sec
    [  5]  10.00-10.01  sec   522 KBytes   353 Mbits/sec
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bandwidth
    [  5]   0.00-10.01  sec  0.00 Bytes  0.00 bits/sec                  sender
    [  5]   0.00-10.01  sec   424 MBytes   355 Mbits/sec                  receiver
    -----------------------------------------------------------
    Server listening on 5201
    -----------------------------------------------------------
    ```

5. That is how to use iPerf in simple examples. We can do more analysis and try more settings that are available in iPerf by using the command `iperf3 --help` to see more options available that can be used in our network testing and analysis