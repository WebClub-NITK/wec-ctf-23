from scapy.all import *

# Define the target IP and port
target_ip = '192.168.122.1'
target_port = 80
sport = 35600

# Set the TCP sequence number to the desired value
seq_num = int.from_bytes(b'\x00\x57\x45\x43', byteorder='big')

# Create an IP packet with the target IP as the destination
ip_packet = IP(dst=target_ip)

# Create a TCP SYN packet with the target port as the destination and set the sequence number
tcp_syn_packet = TCP(sport=sport, dport=target_port, flags='S', seq=seq_num)

# Send the SYN packet and receive a SYN-ACK response
syn_ack_response = sr1(ip_packet/tcp_syn_packet)

# Extract the acknowledgement number from the SYN-ACK response
ack_num = syn_ack_response[TCP].seq + 1

# Create an HTTP GET request for "/"
http_get_request = "GET /flag.html HTTP/1.1\r\nHost: {}\r\n\r\n".format(target_ip)

# Create a TCP PSH-ACK packet with the HTTP GET request as its payload
tcp_get_packet = TCP(sport=sport, dport=target_port, flags='A', seq=tcp_syn_packet.seq + 1, ack=ack_num) / http_get_request

# Send the PSH-ACK packet with the HTTP GET request as its payload
response = sr1(ip_packet/tcp_get_packet)

ack_num = response[TCP].seq +1

tcp_fn_packet = TCP(sport=sport, dport=target_port, flags='R', seq=tcp_get_packet.seq+1)

send(ip_packet/tcp_fn_packet)
# Print the response
response.show()