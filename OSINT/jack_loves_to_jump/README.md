# **Jack loves to jump**

Category: OSINT

Author: Madhav Kumar

Answer / Flag: `WEC{j@ck_fe3ls_l0v3ly}`

## Problem Statement

Jack also famously known as his alias jumpingjack129 is a super smart dude who loves to build extremly complicated and immersive projects and show it off to the world. 

## Solution

- Given the username type alias, you should search for it using sherlock. Also, the information about projects should direct to github.
- In the github profile, you can see two repos, go to "Hello-world" repo and go through the commit of branch b2.
- You will find a hint in the commit message -> "It seems you seek something but can't find it. Perhaps you should try finding it on my social media."
- Go to the profile of github and you will find a twitter link.
- Go to twitter profile, in the bio, it's written "Why don't we all go back in time and find the answers" which hints to use wayback machine.
- In wayback machine, you will find a tweet which contains an image and a drive link to the image with a hint that there might be something hidden in the image.
- Download it and use the steganography tool which is forked in the github account to find the flag image.