# **Uncovering the Secrets of The Order's Secret**

Category: Miscellanous (Blockchain)

Author: Shubham Rasal

Flag: `WEC{53811586f68bad2a1a1d7196d46}`

## Problem Statement

The Order, a secretive organization, has created a blockchain-based smart contract that stores a highly classified message known as the "Flag." Your task is to extract this message by exploiting the contract's vulnerabilities.

The contract contains several functions that perform different operations. However, due to the Order's obsession with secrecy, they have overlooked some programming errors that can be exploited. Remember you will have to give something to get something.

Your objective is to identify these vulnerabilities and find a way to retrieve the Flag.

## Relevant files / links

Actual challenge link : https://shubham-rasal.github.io/ctf/

## Hint

Do you know what a fallback function is?

## Solution

This challenge can be solved by sending a transaction to the contract with a value of non-zero ether. This will trigger the fallback function.

The getFlag() function can be only called by the owner of the contract. So, we need to make the contract owner as the sender of the transaction. This can be done by sending a transaction to the contract with a value of non-zero ether. This will trigger the fallback function.

The fallback function will make the caller the owner of the contract. Now, we can call the getFlag() function to get the flag.
