import scapy.all as scapy
import argparse

# input the ip target range for scan
def get_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("-t", "--target", dest="target", help="Target IP / IP Range")
    options = parser.parse_args()
    return options

def scan(ip):
    arp_request = scapy.ARP(pdst=ip)
    #arp_request.show()
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    #broadcast.show()

    # combine arp request and broadcast packet
    arp_request_broadcast = broadcast/arp_request
    #arp_request_broadcast.show()
    answered_list = scapy.srp(arp_request_broadcast, timeout=1)[0]
    
    # create a dictionary of ips and macs from list
    clients_list = []
    for element in answered_list:
        clients_dict = {"ip": element[1].psrc, "mac": element[1].hwsrc}
        clients_list.append(clients_dict)
        
    return clients_list

def print_results(results_list):
    print("---------------------------------------------------")
    print("IP\t\t|\tMAC Address\n---------------------------------------------------")
    for client in results_list:
        print(f'{client["ip"]}\t|\t{client["mac"]}')


options = get_arguments()
scan_result = scan(options.target)
print_results(scan_result)