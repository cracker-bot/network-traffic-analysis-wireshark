from scapy.all import sniff

def packet_callback(packet):
    print(packet.summary())

# Capture 10 packets
sniff(count=10, prn=packet_callback)