import scapy.all as scapy

def scan(ip):
    scapy.arping(ip)

print(scan("10.0.2.1/24"))