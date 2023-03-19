# It's all about the numbers!

Category: Forensics

Author: Pratik Jallan

Flag: `WEC{510}`

## Problem Statement:

On the occasion of Incident NITK, 300 students Each from seniors and juniors came out to establish their supremacy by a game of tug of war. To balance the team, Odd positions were occupied by people with Maximum Strength while the Even positions were occupied by people with Minimum Strength. The fight was so fierce that there was Red blood everywhere. In the end, the seniors team won but the juniors gave them a photo with some hidden key to find as a last resort. Can you help the seniors figure the key out?

The key to the final answer is (0, 2) * (1, 3) * (3, 3) / (4, 3) and flag format is `WEC{numerical_value_obtained}`.

## Relevant files / links:

- ![Picture](./Encoded_Image.png/)
- [Drive Link](https://drive.google.com/file/d/1WHwISb4NY4BJRQz1qIS-zuKYqnD5umew/view?usp=sharing)

## Hints:

1. The image appears to have some puzzle hidden in it, some of the uppercase letters seem to oddly stand out...
2. Shall you succeed in recovering the puzzle, all you need is a little bit of magic to solve it...

## Solution:

Suggested Difficulty: `Medium/Hard`

The problem involves `Image Steganography` and elementary `Magic Square` number theory. Steganography is a method of hiding secret data, by embedding it into some file, in this case, using an image to hide another image. It is one of the methods employed to protect secret or sensitive data from malicious attacks. A magic square is a N x N matrix, where the elements range from 1 to N * N and the sum of all the elements of every row, column and diagnol is equal.

We know that an image is nothing but a matrix of pixel intensities. As this is a coloured image, it is made up of 3 channels `(RGB)` as opposed to a grayscale one. The description gives us the hint of taking a 300 x 300 matrix in the first line. The letters Odd, Even, Maximum, Minimum, Red are all subsequent clues to recover the puzzle hidden in the image. Wherever the pixel values are `odd, take it as 255 (maximum value of a pixel)` and wherever `even, take it as 0 (minimum value of a pixel)`. This gives us a new 300 x 300 matrix which is the magic sqaure in image format.

Then one must solve the magic square manually or by using some online tool. This will give us the following answer:

- ![Magic_Answer](./Images_Used/Magic_Answer.png/)

The final line in the problem description is a set of mathematical operations involving tuples, which is nothing but the `pair of indices` for that particular element. This gives us the answer 510. The encoding python program, solution and original images used for the same have been included.
