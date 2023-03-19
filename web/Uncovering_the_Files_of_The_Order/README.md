# **Uncovering the Files of The Order**

Category: Web (File Structure)

Author: Shubham Rasal

Flag: `WEC{h1dden_1n_pl41n_s1ght}`

## Problem Statement

The Order, a secretive organization, has been leaking their files to the public. We need to find out what they are hiding.

You might be familiar with the order from their hideous website.

## Relevant files / links

Actual challenge link : https://shubham-rasal.github.io/web-ctf/

## Hint

Do you know what a an inspector does ?

## Solution

This challenge can be solved by using the inspect element feature of the browser. 
There you will be able to find the css file that is being loaded from the secret folder hinting you that there might be other files there.

You can then use this logic to find the next file called secret.html and then later on hidden.html using the same logic.

Finally you will reach the topsecret.html page which has the actual flag.