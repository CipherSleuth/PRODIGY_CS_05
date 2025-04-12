from scapy.all import sniff, IP, TCP, UDP, Raw
from datetime import datetime

def packet_callback(packet):
    print("\n--- Packet Captured ---")
    
    # Timestamp
    print("Time:", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    
    # Source and Destination IP
    if IP in packet:
        print("Source IP:", packet[IP].src)
        print("Destination IP:", packet[IP].dst)
        print("Protocol:", packet[IP].proto)
    
    # Protocol details
    if TCP in packet:
        print("Protocol: TCP")
        print("Source Port:", packet[TCP].sport)
        print("Destination Port:", packet[TCP].dport)
    elif UDP in packet:
        print("Protocol: UDP")
        print("Source Port:", packet[UDP].sport)
        print("Destination Port:", packet[UDP].dport)
    
    # Payload (limited to 100 characters)
    if Raw in packet:
        payload = packet[Raw].load
        print("Payload:", payload[:100])  # Show first 100 bytes for safety

# Sniff packets (use iface='your_interface_name' if needed)
print("Starting packet sniffer... Press Ctrl+C to stop.\n")
sniff(prn=packet_callback, count=0, store=0)
