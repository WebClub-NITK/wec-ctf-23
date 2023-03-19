# ****Restaurant RE-cipies****

Category: Reverse Engineering

Author: Siddharth Bhat

Answer / Flag: `WEC{qazwsxedcrfvtgbyhnujmikolp}`


## Problem statement  

A new fancy restaurant is allowing you to order food via their cutting edge food ordering program.

They also have a secret limited edition item on the menu, which can also be ordered through the software. Unfortunately, the restaurant has not disclosed the name of the item, and it is up to you to try to guess the name and order this specialty item!

Can _*you*_ guess what the name of this strange item is?


## Link to the challenge
The [binary](./RE3Chalfinal) is included in this branch.
The link to the binary - [here](https://drive.google.com/file/d/1ib6Rnj86qA99BnvEXbN2FDPVYHW4wkYb/view?usp=share_link)


## Hints

* The chefs of this restaurant have made the name of the food item very un pronounceable, this is part of their plans
* There is no limit for you to place orders using this software to feel free to bombard the chefs with orders! By the way, the name of the food item does not contain any capial letters, special characters or numbers! ( This should help narrow down the search for the correct string)


## Solution

* The binary can be analysed using any disassembler of choice, preferably one with a visual view of the instruction, such as IDA, R2 or Cutter
* There are no other _important_ function other than main, and inside main one can observe that some sort of summation is being done with the ASCII values of the string.
* The loop adds the ASCII value of the characters in the string to a variable, and subtracts the ASCII value of the character is the position of the charcter of the string is a multiple of 5.
* One can write a simple program to brute-force try different types of strings but that would simply be complicated and time consuming
* Instead if we observe properly, the final sum is being compared to 1493 after the loop, hence one can write a program to check all strings which upon calculation give the number 1493.
* The correct string is qazwsxedcrfvtgbyhnujmikolp and the flag will be WEC{qazwsxedcrfvtgbyhnujmikolp}
