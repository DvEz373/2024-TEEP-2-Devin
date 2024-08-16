# Networking Programming - Ping
- [Networking Programming - Ping](#networking-programming---ping)
  - [1. Ping](#1-ping)
    - [1.1. What is Ping?](#11-what-is-ping)
    - [1.2. ICMP](#12-icmp)
    - [1.3. Difference Between Ping and Traceroute](#13-difference-between-ping-and-traceroute)
    - [1.4. Ping Command in Windows](#14-ping-command-in-windows)
    - [1.5. Ping Command in Linux](#15-ping-command-in-linux)
    - [1.6. Result Ping Network Testing](#16-result-ping-network-testing)
    - [1.7. Example in Using Ping Command](#17-example-in-using-ping-command)

## 1. Ping
### 1.1. What is Ping?
![image](https://hackmd.io/_uploads/Sy2qfsju6.png)

<div class="text-justify">
    
**Ping** is a network diagnostic tool used to test the connectivity between two nodes or devices. It is based on the **ICMP** protocol and is available for virtually all operating systems that have networking capability. When you ping a destination node, an ICMP echo request packet is sent to that node. If a connection is available, the destination node responds with an echo reply. The **ping command** measures the time it takes for the packet to travel from your device to the target device and back. This round-trip time (**RTT**) provides valuable information about the speed and responsiveness of your network connection. A low ping time is critical in situations where the timely delivery of data is more important than the quantity and quality of the desired information. 
</div>

### 1.2. ICMP
<div class="text-justify">
    
**ICMP** stands for **Internet Control Message Protocol**. It is a network layer protocol used by network devices to diagnose network communication issues. ICMP is mainly used to determine whether or not data is reaching its intended destination in a timely manner. When two devices connect over the Internet, the ICMP generates errors to share with the sending device in the event that any of the data did not get to its intended destination. For example, if a packet of data is too large for a router, the router will drop the packet and send an ICMP message back to the original source for the data. 

ICMP is also used to perform network diagnostics. The commonly used terminal utilities **traceroute** and **ping** both operate using ICMP. The traceroute utility is used to display the routing path between two Internet devices. The routing path is the actual physical path of connected routers that a request must pass through before it reaches its destination. The journey between one router and another is known as a ‘hop,’ and a traceroute also reports the time required for each hop along the way. This can be useful for determining sources of network delay. The ping utility is a simplified version of traceroute. A ping will test the speed of the connection between two devices and report exactly how long it takes a packet of data to reach its destination and come back to the sender’s device. Although ping does not provide data about routing or hops, it is still a very useful metric for gauging the latency between two devices.

### 1.3. Difference Between Ping and Traceroute
**Ping** and **Traceroute** are both network diagnostic tools used to test the connectivity between two nodes or devices. However, they differ in their use cases and the information they provide.
* **Ping** is used to test network connectivity and name resolution. It sends a packet to the specified address and waits for a response. If the other device responds, the ping is successful, and the round-trip time (RTT) is measured. The RTT provides valuable information about the speed and responsiveness of your network connection. A low ping time is critical in situations where the timely delivery of data is more important than the quantity and quality of the desired information. For example, if you are streaming a game on YouTube, you'll want the latency to be as low as possible so that viewers can watch in real-time.
* **Traceroute** is used to display the routing path between two Internet devices. The routing path is the actual physical path of connected routers that a request must pass through before it reaches its destination. The journey between one router and another is known as a ‘hop,’ and a traceroute also reports the time required for each hop along the way. This can be useful for determining sources of network delay. Traceroute works by sending packets of data with a low survival time (Time to Live – TTL) which specifies how many steps (hops) the packet can survive before it is returned. When a packet can’t reach the final destination and expires at an intermediate step, that node returns the packet and identifies itself. So, by increasing the TTL gradually, Traceroute is able to identify the intermediate hosts. If any of the hops come back with “Request timed out”, it denotes network congestion and a reason for slow-loading Web pages and dropped connections.
</div>

### 1.4. Ping Command in Windows
<div class="text-justify">
To use the ping command in Windows, follow these steps:

1. Open the **Command Prompt** by typing `cmd` in the search bar and selecting the app.
2. Type `ping` followed by the IP address or domain name of the device you want to ping.
3. Press the **Enter** key to execute the command.

Here's an example of how to use the ping command to test the connectivity to the Google DNS server:

```
C:\Users\username>ping 8.8.8.8
```

This will send a series of ICMP echo requests to the specified IP address and display the results. You can use the `-t` option to ping the target indefinitely until you stop it by pressing `Ctrl+C`. The `-a` option can be used to resolve the hostname of an IP address target. The `-n count` option sets the number of ICMP echo requests to send, from 1 to 4294967295. The `-l size` option sets the size of the ICMP echo request packet, from 32 to 65500 bytes. The `-f` option sets the Don't Fragment flag in the packet. The `-i TTL` option sets the Time To Live (TTL) value of the packet. The `-v TOS` option sets the Type Of Service (TOS) value of the packet. The `-r count` option sets the number of hops to search for the target. The `-s count` option sets the timestamp for each echo request.

### 1.5. Ping Command in Linux
To use the ping command in Linux, follow these steps:

1. Open the **Terminal** application.
2. Type `ping` followed by the IP address or domain name of the device you want to ping.
3. Press the **Enter** key to execute the command.

Here's an example of how to use the ping command to test the connectivity to the Google DNS server:

```
$ ping 8.8.8.8
```

This will send a series of ICMP echo requests to the specified IP address and display the results. You can use the `-c` option to ping the target for a specific number of times. The `-i` option sets the interval between two consecutive packets. The `-s` option sets the size of the ICMP echo request packet ⁶. The `-t` option sets the Time To Live (TTL) value of the packet. The `-v` option sets the verbosity level of the output. The `-w` option sets the timeout value in seconds.

### 1.6. Result Ping Network Testing
When you run a **ping** command, you will see a series of lines in the output. The following example shows the results of running the command `ping www.example.com` on Windows Command Prompt:

```
Pinging www.example.com [93.184.216.34] with 32 bytes of data:
Reply from 93.184.216.34: bytes=32 time=2ms TTL=56
Reply from 93.184.216.34: bytes=32 time=2ms TTL=56
Reply from 93.184.216.34: bytes=32 time=2ms TTL=56
Reply from 93.184.216.34: bytes=32 time=2ms TTL=56

Ping statistics for 93.184.216.34:
    Packets: Sent = 4, Received = 4, Lost = 0 (0% loss),
Approximate round trip times in milli-seconds:
    Minimum = 2ms, Maximum = 2ms, Average = 2ms
```

Here's how to interpret the results:
- **Destination IP Address or Hostname**: The first line typically shows the IP address or hostname of the target device. In this example, it is `www.example.com`.
- **Packet Size**: At the end of the first line, you can read the size of each ICMP (Internet Control Message Protocol) packet sent. In this case, the packet size is 32 bytes.
- **Ping Responses**: The following lines represent the responses received from the target device. Each line shows the number of bytes in the response, the time it took for the response to be received, and the TTL (Time-to-Live) value of the packet. The TTL value indicates the number of routers the packet has passed through before reaching the destination. A low TTL value may indicate network congestion or other issues.
- **Ping Statistics**: The last section of the output provides statistics about the ping test. It shows the number of packets sent, received, and lost, as well as the minimum, maximum, and average round-trip times in milliseconds.

By analyzing the **ping results**, you can gather insights into potential network problems. Consistently high response times or packet loss may indicate network congestion, device connectivity issues, or even problems with the target server.
    
</div>

### 1.7. Example in Using Ping Command
In this example I am going to use `ping` command to check connection to the target device. In this case it will be,
https://dvnezkl03.github.io/portfolioresume-website/
This can be used both in Windows and Linux.
1. To check ping in Windows, we will be using the command 

    ```powershell
    ping -n 7 dvnezkl03.github.io
    ```

    Output:
    ```powershell
    C:\Users\Acer>ping -n 7 dvnezkl03.github.io

    Pinging dvnezkl03.github.io [185.199.108.153] with 32 bytes of data:
    Reply from 185.199.108.153: bytes=32 time=51ms TTL=53
    Reply from 185.199.108.153: bytes=32 time=59ms TTL=53
    Reply from 185.199.108.153: bytes=32 time=112ms TTL=53
    Reply from 185.199.108.153: bytes=32 time=63ms TTL=53
    Reply from 185.199.108.153: bytes=32 time=72ms TTL=53
    Reply from 185.199.108.153: bytes=32 time=67ms TTL=53
    Reply from 185.199.108.153: bytes=32 time=59ms TTL=53

    Ping statistics for 185.199.108.153:
        Packets: Sent = 7, Received = 7, Lost = 0 (0% loss),
    Approximate round trip times in milli-seconds:
        Minimum = 51ms, Maximum = 112ms, Average = 69ms
    ```

2. This can also be done in Linux Ubuntu with some different syntax based on the operating system. The command:
    ```powershell
    ping -c 9 dvnezkl03.github.io
    ```

    Output:
    ```bash
    dvnezkl03@ubuntu:~$ ping -c 9 dvnezkl03.github.io
    PING dvnezkl03.github.io (185.199.108.153) 56(84) bytes of data.
    64 bytes from cdn-185-199-108-153.github.com (185.199.108.153): icmp_seq=1 ttl=128 time=68.4 ms
    64 bytes from cdn-185-199-108-153.github.com (185.199.108.153): icmp_seq=2 ttl=128 time=72.8 ms
    64 bytes from cdn-185-199-108-153.github.com (185.199.108.153): icmp_seq=3 ttl=128 time=69.0 ms
    64 bytes from cdn-185-199-108-153.github.com (185.199.108.153): icmp_seq=4 ttl=128 time=64.0 ms
    64 bytes from cdn-185-199-108-153.github.com (185.199.108.153): icmp_seq=5 ttl=128 time=136 ms
    64 bytes from cdn-185-199-108-153.github.com (185.199.108.153): icmp_seq=6 ttl=128 time=64.0 ms
    64 bytes from cdn-185-199-108-153.github.com (185.199.108.153): icmp_seq=7 ttl=128 time=64.3 ms
    64 bytes from cdn-185-199-108-153.github.com (185.199.108.153): icmp_seq=8 ttl=128 time=111 ms
    64 bytes from cdn-185-199-108-153.github.com (185.199.108.153): icmp_seq=9 ttl=128 time=117 ms

    --- dvnezkl03.github.io ping statistics ---
    9 packets transmitted, 9 received, 0% packet loss, time 8570ms
    rtt min/avg/max/mdev = 63.958/85.279/136.489/26.591 ms
    ```
3. The number of ping that we can specify in the command can be arbitrary based on our needs.
4. The next thing that we can do is we can specify some specific options based on our purpose of network analysis. The parameters or options added after the ping command are known as the ping switches or modifiers. Typically, the command `ping ?` allows us to get details for all the ping options they can use on any operating system. Outlined below are some of the popular switches in Linux by using the `ping --help` command:
```bash
dvnezkl03@ubuntu:~$ ping --help
ping: invalid option -- '-'

Usage
  ping [options] <destination>

Options:
  <destination>      dns name or ip address
  -a                 use audible ping
  -A                 use adaptive ping
  -B                 sticky source address
  -c <count>         stop after <count> replies
  -D                 print timestamps
  -d                 use SO_DEBUG socket option
  -f                 flood ping
  -h                 print help and exit
  -I <interface>     either interface name or address
  -i <interval>      seconds between sending each packet
  -L                 suppress loopback of multicast packets
  -l <preload>       send <preload> number of packages while waiting replies
  -m <mark>          tag the packets going out
  -M <pmtud opt>     define mtu discovery, can be one of <do|dont|want>
  -n                 no dns name resolution
  -O                 report outstanding replies
  -p <pattern>       contents of padding byte
  -q                 quiet output
  -Q <tclass>        use quality of service <tclass> bits
  -s <size>          use <size> as number of data bytes to be sent
  -S <size>          use <size> as SO_SNDBUF socket option value
  -t <ttl>           define time to live
  -U                 print user-to-user latency
  -v                 verbose output
  -V                 print version and exit
  -w <deadline>      reply wait <deadline> in seconds
  -W <timeout>       time to wait for response

IPv4 options:
  -4                 use IPv4
  -b                 allow pinging broadcast
  -R                 record route
  -T <timestamp>     define timestamp, can be one of <tsonly|tsandaddr|tsprespec>

IPv6 options:
  -6                 use IPv6
  -F <flowlabel>     define flow label, default is random
  -N <nodeinfo opt>  use icmp6 node info query, try <help> as argument

For more details see ping(8).
```

This can also be done in Windows to see several options available:
```bash
C:\Users\Acer>ping --help
Bad option --help.

Usage: ping [-t] [-a] [-n count] [-l size] [-f] [-i TTL] [-v TOS]
            [-r count] [-s count] [[-j host-list] | [-k host-list]]
            [-w timeout] [-R] [-S srcaddr] [-c compartment] [-p]
            [-4] [-6] target_name

Options:
    -t             Ping the specified host until stopped.
                   To see statistics and continue - type Control-Break;
                   To stop - type Control-C.
    -a             Resolve addresses to hostnames.
    -n count       Number of echo requests to send.
    -l size        Send buffer size.
    -f             Set Don't Fragment flag in packet (IPv4-only).
    -i TTL         Time To Live.
    -v TOS         Type Of Service (IPv4-only. This setting has been deprecated
                   and has no effect on the type of service field in the IP
                   Header).
    -r count       Record route for count hops (IPv4-only).
    -s count       Timestamp for count hops (IPv4-only).
    -j host-list   Loose source route along host-list (IPv4-only).
    -k host-list   Strict source route along host-list (IPv4-only).
    -w timeout     Timeout in milliseconds to wait for each reply.
    -R             Use routing header to test reverse route also (IPv6-only).
                   Per RFC 5095 the use of this routing header has been
                   deprecated. Some systems may drop echo requests if
                   this header is used.
    -S srcaddr     Source address to use.
    -c compartment Routing compartment identifier.
    -p             Ping a Hyper-V Network Virtualization provider address.
    -4             Force using IPv4.
    -6             Force using IPv6.
```
