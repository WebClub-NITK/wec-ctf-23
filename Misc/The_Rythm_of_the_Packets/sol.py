from scapy.all import *

import base64
# read the stego.pcap file
packets = rdpcap("timings.pcap")

# create a list to store the bits
bits = []

# loop through the packets
prev_time = packets[0].time
for pkt in packets[1:]:
    # time delta from previous captured packet
    delta = pkt.time - prev_time

    # round of delta to 1 decimal 
    delta = float(round(delta, 1))
    if(delta == 0.1):
        bits.append("0")
    elif(delta == 0.2):
        bits.append("1")

    prev_time = pkt.time

# convert the bits to a string
message = "".join(bits)

# convert the binary string to bytes
message = int(message, 2).to_bytes((len(message) + 7) // 8, "big").decode()

#decode message using base64
message = base64.b64decode(message).decode('ascii')

print(message)