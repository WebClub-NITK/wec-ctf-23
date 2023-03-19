# Secrets galore!

Category: Reverse Engineering

Author: Siddharth Bhat

Answer / Flag: `WEC{1M_Ju5t_K1DD1n6_Th3r5_n0_S3cr3t}`

## Problem statement
George Hotz decided to test your "h4x0r sk1lzz" by giving you a challenge. All he wants is a secret from it. Can you give it to him?

### Link to challenge 
The [binary](./chal1.2.o) is in this repo


### Hints
Like most probelms in life, there is a complicated way to do this, and a much much easier way to do this! Put on those thinking caps, because every method is allowed!

## Solution
* On amining the binary in a disassembler of choice, one can observe that there are multiple functions other than the main function
* he functions are copy(), bigbigsecret1(), bigbigsecret2(), bigbigsecret3()
* n observing the behaviour and disassembly, one might notice that bigbigsecret3() is the true function printing something, whereas bigbigsecret1() and bigbigsecret2() don't do much
* On observing further, one can observe that bigbigsecret3() will print out something only if a variable is set to 2!
* bigbigsecret1() and bigbigsecret2() are the functions which increment that particular variable being checked in bigbigsecret3()
* Hence one possible solution is to craft an exploit where the saved return address on the stack is overwritten with a chain of addresses such that both bigbigsecret1() and bigbigsecret2() are called. This will ensure that the variable is incremented to 2 and the check in bigbigsecret3() is passed, printing out the flag!
* The simpler method would be to patch the binary while runtime/before runtime, and set the variable to 2 before the program runs! Then one would have to simply use the address of bigbigsecret3() and call it, and boom, you get the flag!
* The important observation is that the variable being used is a global variable because it is being stored and called from the .data segment of the binary. 
