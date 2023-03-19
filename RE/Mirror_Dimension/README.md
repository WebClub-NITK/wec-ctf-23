# **MIRROR DIMENSION**

Category: RE

Author: Aditya Harish

Answer / Flag: `WEC{buff3r_0v3rfl0ws}`

## Problem Statement

While exploring the mirror dimension in the USA, you come across a plaque that reads `17f9c875d33b0fb8cb40fdf6712f3746e2ec325ef1e55c413a9fa5a61b5cb7b5`. In order to make sense of it, you are given an executable that will lead you to your answer. You also know that the encryption algorithm is vulnerable to a padding oracle attack.

## Relevant files / links

https://drive.google.com/file/d/1tLvHrAflLpe8Pzs5xG1d2jS-U68a52kf/view?usp=sharing

## Hint

In order to narrow down the mode of encryption, think of the phrase "too bad I hid a boot". 

## Solution

The flag is encrypted using AES CBC. As AES is symmetric, only one key is required. On analyzing the binary, there are two functions of interest. One of them called `getonecomponent()` and `getanothercomponent()`. These functions print the key and initialization vector when called. There's no direct call to these functions but `gets()` is used in the executable, so the return address of the functions can be corrupted with a buffer overflow attack. 
The key is `youhavesuccessfullyfoundthekey!!` and the initialization vector is `1238190421ABCDEF`.  
