# **The Rhythm of the Packets**

Category: Misc

Author: [Advaith](https://github.com/advaithcurpod)

Answer / Flag: `WEC{t1m3stamp1sTH3KE3}`

## Problem Statement

We have intercepted some suspicious network packets from an enemy agent. We suspect that they contain a secret message. Can you find the flag?

## Relevant files / links

[timings.pcap](https://drive.google.com/file/d/1xu6fGbNUMYRtzKw1EbcaDdbUavC1YWrn/view?usp=share_link)

## Solution

1. Download and open the pcap file in wireshark
2. Observe that all packets have an empty payload except for the last 2 packet
3. The payload is the hint as to how to solve this question.
4. On careful observation, you will see that the delay between each consecutive packet is either 0.1 seconds or 0.2 seconds, and the hints indicate that 0.1 seconds is a 0 bit and 0.2 seconds is a 1 bit.
5. Convert the delay between each packet to binary and the binary string into bytes to get a base64 string.
6. Decode the base64 string to get the flag.

[Python code for the solution](./sol.py)
