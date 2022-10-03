import scapy.all as scapy

def scan(ip):
    arp_request = scapy.ARP(pdst=ip)
    arp_request.show()
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    broadcast.show()

    # combine arp request and broadcast packet
    arp_request_broadcast = broadcast/arp_request
    arp_request_broadcast.show()

print(scan("10.0.2.1/24"))