# Espionage Escapade

Category: Reverse Engineering

Author: Aditya Harish

Answer / Flag: `WEC{gR3p__c4N_h3Lp}`

## Problem Statement

You discover this binary executable while spying on enemy governments. The way the government hides their data is rather weak, however it can be painstaking. 

## Relevant files / links

https://drive.google.com/file/d/1Wf_HQx9Y-GL1ERl_h7yptZ_H6gvWqrFK/view?usp=sharing




## Solution

On using the strings command, we can observe a large string with a lot of gibberish. We know the flag is of the format `WEC{flag}`.On running the command `strings topsecretinfo | grep -o "WEC{.*"` we can search through all strings that start with the pattern `WEC{`, and then the flag is obtained.
