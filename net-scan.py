import scapy.all as scapy

def scan(ip):
    arp_request = scapy.ARP(pdst=ip)
    #arp_request.show()
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    #broadcast.show()

    # combine arp request and broadcast packet
    arp_request_broadcast = broadcast/arp_request
    #arp_request_broadcast.show()
    answered, unanswered = scapy.srp(arp_request_broadcast, timeout=1)
    print(answered.summary())

print(scan("10.0.2.1/24"))