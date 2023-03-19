# The Concrete Jungle

Category: Forensics

Author: Pratham Kiran K

Answer / Flag: `WEC{F0und_mE}`

## Problem Statement

Thomas just reached New York city hoping to enjoy his vacations, just to have his wallet stolen on the first day. The robbers left a clue for him which may lead him to the wallets. Help Thomas solve the clues so that he can buy himself lunch.  

## Relevant files / links

* https://drive.google.com/file/d/1dfMysE--oqgesudUZ65IdnFQVQ35pJWW/view?usp=sharing
* https://drive.google.com/file/d/19YihC43QVjWBADvMSKwbHrGLPouW3H_t/view?usp=sharing

## Hint

A good structure is always built on top of a good base.

## Solution

* Two image files `base` and `structure` have been provided.
* `base` has the list of encodings and the data source.
* Structure is a .png maze
* To get the flag, overlap the two images and reduce the saturation of `structure.png` to 0% (Or whatever helps you see the images clearly).
* There is only one entry point for the maze - author. The end goal is the flag.
* Solve the maze and find a path from the author to the flag. 
* On solving the maze we get the know that the flag is encoded as
  * Flag ->base64 -> base62 -> base58 -> base45 -> author
* Hence, to get the flag, follow the same steps, but in reverse order. That is, is this very specific order:
  * Author -> base45 -> base58 -> base62 -> base64 -> Flag
* Plugging in the author name (present in the metadata of `base.png`), we get the flag
  * Here, author is  `:A8ZTA479O8DNB76ECAB87.CZJE.*8W+A++8XYA2N8KS92DBUEECNA82`
  * Using this text, we get the flag as `WEC{F0und_mE}`
  
