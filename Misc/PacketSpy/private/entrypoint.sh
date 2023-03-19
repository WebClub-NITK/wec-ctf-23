#!/bin/sh
set -e
# Who are we? W: 0x53 E: 0x45 C: 0x43
iptables -A INPUT -p tcp --tcp-flags SYN SYN --match u32 ! --u32 "24&0xFFFFFFFF=0x00574543" -j DROP
/docker-entrypoint.sh "$@"
