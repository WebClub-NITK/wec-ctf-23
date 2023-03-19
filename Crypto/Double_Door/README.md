# Double_Doors

Category: Cryptography

Author: Kirubakaran M G

Answer / Flag: `WEC{ORDERFROMCHAOSX}`

## Problem Statement

There are two doors to open to learn the basic concept of cryptography. 
First the EMPEROR's door, then the LORD's. 
Both have the same key just inserted differently.

The following is written on a wall:
`DQN{UAKOXKCSVLONSZG}`

The key can be obtained by solving the riddle:
Turn it on its side and its EVERYTHING. Cut it in half and its NOTHING.



## Hint

The keyword for Lord's cipher must be a word.

## Solution

The hint gives the answer "8". The emperor's door denotes Caesar Cipher and the lord's door denotes Playfair Cipher. The given text is decrypted with Caesar first,  with the shift as 8. Then it is decrypted with Playfair cipher with the keyword as "EIGHT", and the final answer is obtained.

Code:


[DoubleDoors_CODE.txt](./DoubleDoors_CODE.txt)


Links:
Playfair: https://planetcalc.com/7751/
Caesaar: https://www.dcode.fr/caesar-cipher
