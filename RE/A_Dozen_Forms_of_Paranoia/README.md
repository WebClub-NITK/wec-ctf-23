# A Dozen Forms of Paranoia

Category: RE

Author: Kavya Bhat

Answer / Flag: `WEC{n0t_s0_s3cr3t_aft3r_@ll}`

## Problem Statement

Marvin the Android thought it was so smart to use his own form of encoding messages, he forgot to be paranoid. All was well until today, when you decided to take a shot at figuring out one of his messages. Are you going to turn Marvin into a paranoid android again?

## Relevant files / links

<https://drive.google.com/drive/folders/1MBKsbjt4Q_SdWnuinPB5TeyLMfikSBxb?usp=sharing>

## Hint
1. Sometimes, two wrongs make a right.

## Solution

- Open the pcap file in wireshark. On examining some of the TCP packets closely, you'll find that there are some recognizable English words present. 
- Each packet with such data is of the size 91, filter these. (You can use `tcp and frame.len==91` in the display filter.)
- Using the Analyze -> Follow TCP Stream option, you'll be able to get the entire message. There are 2 encoded strings here.
- Analyze the given binary, where a `genkey()` function is present. On examining that, we see that the some characters of the flag are swapped, and then the string is encoded in base 12. 
- The individual encoded strings are invalid in base 12, but the message hints at using both encoded strings. Write a script (or use an online tool :P) to concatenate these strings, and convert the resulting string from base 12 to ASCII. 
- This results in a garbled flag. Now swap the same characters as in the analyzed pseudocode, and yay! You have the required flag :)