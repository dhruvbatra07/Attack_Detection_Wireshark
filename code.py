import pyshark
 
def detect_syn_flood(packet):
   try:
       if 'TCP' in packet and packet.tcp.flags_syn == '1' and packet.tcp.flags_ack == '0':
           print(f"[!] SYN Flood detected: {packet}")
           return True
   except AttributeError:
       pass
   return False
 
def detect_port_scan(packet):
   try:
       if 'TCP' in packet and packet.tcp.flags_syn == '1' and packet.tcp.flags_ack == '1':
           print(f"[!] Port Scan detected: {packet}")
           return True
   except AttributeError:
       pass
   return False
 
def detect_arp_spoof(packet):
   try:
       if 'ARP' in packet and packet.arp.opcode == '2':
           print(f"[!] ARP Spoofing detected: {packet}")
           return True
   except AttributeError:
       pass
   return False
 
def analyze_packet(packet):
   if detect_syn_flood(packet):
       # Additional handling for SYN Flood
       pass
   elif detect_port_scan(packet):
       # Additional handling for Port Scan
       pass
   elif detect_arp_spoof(packet):
       # Additional handling for ARP Spoofing
       pass
 
def analyze_pcap(file_path):
   capture = pyshark.FileCapture(file_path)
   for packet in capture:
       analyze_packet(packet)
 
if __name__ == "__main__":
   pcap_file = "new.pcapng"  # Replace with the correct path
   analyze_pcap(pcap_file)