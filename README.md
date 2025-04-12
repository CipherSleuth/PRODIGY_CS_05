# Packet Sniffer Tool (Python)

A simple and effective network packet sniffer built using Python and Scapy. This tool captures and analyzes live network traffic, displaying important information such as:

- Source & Destination IP addresses
- Protocols (TCP/UDP)
- Port Numbers
- Payload (limited to 100 characters)

> **Note:** This tool is strictly for **educational and ethical** purposes only.

---

## Features

- Real-time packet capture
- Protocol and port identification
- Lightweight and console-based
- Timestamped logs for each packet
- Easy to understand for beginners in cybersecurity

---

## Installation

### Requirements

- Python 3.x
- Scapy library

### Install Scapy

```bash
pip install scapy


---

Usage

python packet_sniffer.py

You can optionally specify a network interface:

sniff(prn=packet_callback, iface="eth0", count=0, store=0)


---

Sample Output

--- Packet Captured ---
Time: 2025-04-12 14:23:15
Source IP: 192.168.1.100
Destination IP: 142.250.180.206
Protocol: TCP
Source Port: 52344
Destination Port: 443
Payload: b'GET / HTTP/1.1\r\nHost: www.google.com\r\nUser-Agent:...'


---

Ethical Use

This packet sniffer is created only for learning purposes. Never use this tool on networks you do not own or have explicit permission to analyze. Unauthorized monitoring is illegal and unethical.


---

To Do / Enhancements

Save captured packets to .pcap file

Add GUI version

Add filters (port, IP, protocol)

Export to CSV or JSON



---

License

This project is licensed under the MIT License – see LICENSE file for details.


---

Author

Tejas Sardar
Passionate about cybersecurity, ethical hacking, and network analysis.

---

## **4. LICENSE** (MIT)

```plaintext
MIT License

Copyright (c) 2025 Tejas Sardar

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights  
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell      
copies of the Software, and to permit persons to whom the Software is          
furnished to do so, subject to the following conditions:                        

The above copyright notice and this permission notice shall be included in     
all copies or substantial portions of the Software.                            

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR     
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,       
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE    
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER         
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,  
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN      
THE SOFTWARE.
