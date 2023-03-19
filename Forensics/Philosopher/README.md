# Philosopher

Category: Forensics

Author: Pratham Kiran K

Answer / Flag: `WEC{True_Philosopher}`

## Problem Statement

While relaxing in a park, you notice an old man sitting next to you, enjoying his day. You ask him, "What is the secret to your happiness?". He gives
you a disk which has only one file in it. he says that if you really want to understand it, you should go back in reverse and think about the information he has given you.  
Before leaving he says the following words:  
Every  Fruit   Live  
Third  Love    Pain  
Letter   Stress  Life  

## Relevant files / links

https://drive.google.com/file/d/1S79n-k68EjFGUhAomlvPxGAmd-DYoaNB/view?usp=sharing

## Hint

The last set of words he spoke are not random, just need to see it in a different perspective.

## Solution

* The file is a QR Code image, when scanned gives a string of binaries
* Coverting the binary text to string text, we get
  * **}d`rxIe\6hN4p@Aou1sojoG9l:ciwhhU:PX2_cHe`_u7urkBTa]{^OCzYEnMW8G**
* We have to go backwards to understand it, hence we reverse the string we get.
* The last set of sentences when read from the first word downwards, we get Every Third Letter, so we every third letter from the string, to get the flag, which is **WEC{True_Philosopher}**
  
