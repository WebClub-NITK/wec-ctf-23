# PacketSpy

Category: MISC/Networking

Author: Amogh Umesh

Answer / Flag: `WEC{7cp_h4nd5h4k35_4r3_fun}`

## Problem Statement

You are a secret agent trying to gain access to a highly secure facility where the Web Enthusiasts' club is headquartered. In order to infiltrate their network, you must crack a TCP challenge. To practice your espionage skills, we've provided you with a docker image that mimics the server image, but without the flag. Can you use your cunning and expertise to crack the WEC code and gain access to the network? Good luck, agent.

## Relevant files / links

`docker run --cap-add NET_ADMIN -d -p 80:80 am0gh/network_magic`

Dockerfile: `https://drive.google.com/file/d/1LWs9cJ-mz0xwdZa7fKQJpxw2ZQdHENrA/view?usp=sharing`

## Solution

Explore the docker container and you can find out that server blocks all tcp packets if they dont start with sequence number `0x00574543`. So we need to send a packet with sequence number `0x00574543` make 3 way TCP handshake and make GET request for [flag.html](./private/flag.html). Solution given [here](./private/sol.py).
