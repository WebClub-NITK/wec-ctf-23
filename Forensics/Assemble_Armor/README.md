# **Assemble Armor**

Category: Forensics

Author: Chinmaya Sharma

Answer / Flag: `WEC{1m_5uch_4_h4ck3r}`

## Problem Statement

Iron Man is locked in a cave. He has "experimented" with creating a suit of armor that can fly. He is finally finished with the suit, but does not want his captors to find it, so he disassembles it and hides the parts in different parts of the cave. Find out where the parts of the suit are hidden, and put them together to escape the cave.

## Relevant files / links

- [https://drive.google.com/file/d/1wQyDndxsosjHjvKao6haVML98M58G8ru/view?usp=sharing](https://drive.google.com/file/d/1TxDoysSpncuXorf5Sm2YPROyyM6vBmL3/view?usp=share_link)

## Hint

All the parts weigh the same.

## Solution

- Open the pcap file in wireshark
- Filter for experimental ethernet type
- Packets of size 160 are repeating
- Use scapy or other tools to filter out packets not of type 0x88b5 or size 160, and join together the payloads
- Payload is in bytes, save it to an image format, and open the image, flag is in the image
