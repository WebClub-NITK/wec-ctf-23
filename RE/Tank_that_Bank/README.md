# Tank that Bank !

Category : Reverse Engineering

Author   : Siddharth Bhat

Flag : `WEC{13371337}`


## Problem statement  

SUPER-SAFE-AMAZING-BANK distributes a software which provides users with their bank account number when provided with a PIN.
A smart bank customer Praveen realised that the bank distributing such sensitive software could be dangerous and decided to ask a professional to examine the software.

Can _*you*_ guess Praveen's account number and prove that SUPER-SAFE-AMAZING-BANK is infact shipping unsafe software to its customers?

Submit the flag in the format WEC{\<accountnumber\>}



## Link to challenge
[Google drive link to chaleenge - The binary for this challenge is mycrackme32.o](https://drive.google.com/file/d/1EVWQbrtwCwkr53eekgps75ggtga6K47w/view?usp=share_link)

or 

[Binary](./RE2final)


PS - mycrackme32.o is 32 bit, mycrackme.o is 64 bit, any of them can be used for this challenge i think.

## Hint
The bank claims to be extremely secure, and uses a very popular scheme of encryption in their software. Little do they know that the encryption they are using is not at all appropriate for such a scenario!

## Solution
* The binary can be analysed using any disassembler of choice, preferably one with a visual view of the instruction, such as IDA, R2 or Cutter
* The function modular_exponentiation_by_repeated_squaring() should be a very big hint, since this particular operation is performed in the RSA encryption scheme.
* One may also notice that there are a few variables initialised, and some of them are prime numbers, again hinting at the usage of RSA.
* The functions weirdanswer(), flag() and flaganswer() are all meant to be some sort of obfuscation. They all lead into wrong answers, inspite of their sugestive names
* The general input output flow of the program, mainly handled by weirdfunction() also contains many if statements adding another layer of difficulty in reverse engineering the program.
* On noticing that weirdfunction(args)'s if statements are all checking if d != 5011, if one simply inputs 5011 is the PIN, the flag number 13371337 is retrieved!

