# **Welcome to Hell**

Category: Crypto

Author: Adarsh Kishore

Answer / Flag: `WEC{S0me_pohl1g-Hell@sH12t-th13}`

## Problem Statement

Feistel has lately been studying some advanced Elliptic Curve Cryptography. He came across the elliptic curve

$$
y^2 = x^3 + 2x +3 \, \text{mod} \, 106859
$$

which has an *order* of 53608 from the generator $(3, 6)$. Futher, he further knows that the result point obtained from the generator is $(81310, 85453)$.

Apart from this, he has a strange looking text `1+jn39uL7ZylzIrUzMicmEhlbGxAc0gxMnQtdGgxM30=\n` along with a text saying `XOR your rounds!` which apparently encodes the method to solve this entire problem.

Help him decode the instructions.

## Hint

1. Interesting challenge name, don't you think?
2. Interesting user name, don't you think?
3. It says XOR your rounds. Perhaps round function is a XOR?

## Solution

### Problem Setup

This problem is a combination of **Elliptic Curve Diffie-Hellman** and **Feistel Cipher**.

Let the elliptic curve be

$$
E: y^2 = x^3 + 2x + 3 \, \text{mod} \, 106859
$$

the generator $G = (3, 6)$ and the final point $R = (81310, 85435)$. It is given that $O(G) = 53608$.

First, we need to find the number $x$ with the property that

$$
R = xG
$$

with multiplication having the usual notion in elliptic curve cryptography. This is the discrete logarithm problem, and is infeasible to brute force.

If the order of the curve has many small prime factors, then it is feasible to break the discrete logarithm problem by the **Pohlig-Hellman** algorithm. A quick computation (using SageMath or any online math factor calculator) shows that

$$
53608 = 2^3 \cdot 6701
$$

which are small enough to apply the Pohlig-Hellman algorithm.

---

### Pohlig-Hellman Algorithm

The Pohlig-Hellman algorithm basically states that if

$$
m = O(G) = \prod_{i=1}^n p_i^{k_i}
$$

and

$$
Q=xP
$$

then for each $i$ in $\{ 1,2,\ldots n \}$, let

$$
x = x_i \, \text{mod} \, p_i^{k_i} \\
x_i = \left( \sum_{r = 0}^{k_i - 1} a_r p_i^r \right)\, \text{mod} \, p_i
$$

and

$$
\frac{ma_0}{p_i}P = \left(\frac{m}{p_i} Q \right) \, \text{mod} \, p_i
$$

and

$$
\frac{ma_r}{p_i} P = \left( \frac{m}{p_i^{r+1}} Q - m \sum_{p=0}^{r-1} \frac{a_p}{p_i^{r-p}} P\right) \, \text{mod} \, p_i, \quad r > 0
$$

Each of these steps are small enough that they can be brute-forced, finally we get

$$
x = x_1 \, \text{mod} \, p_1^{k_1}\\
x = x_2 \, \text{mod} \, p_2^{k_2}\\
x = x_3 \, \text{mod} \, p_3^{k_3}\\
\dots\\
x = x_n \, \text{mod} \, p_n^{k_n}\\
$$

By applying **Chinese Remainder Theorem** on this, we can find $x$, such that

$$
Q = xP
$$

---
From this procedure, we can find $x$ such that $R = xG$.

Since $m = 2^3 \cdot 6701$, $p_1 = 2$, $k_1 = 3$, $p_2 = 6701$, $k_2 = 1$.

Let

$$
x_1 = a_0 + a_1 (2) + a_2 (2)^2 \\
x_2 = b_0
$$

Therefore

$$
(2^2 \cdot 6701) a_0 G = (2^2 \cdot 6701) R \, \text{mod} \, 2 \\
$$

from which we can calculate $a_0$.
Similarly,

$$
(2^2 \cdot 6701) a_1 G = \left((2 \cdot 6701) R - (2 \cdot 6701) a_0 P \right) \, \text{mod} \, 2
$$

$$
(2 \cdot 6701) a_2 G = \left(6701 R - (2^3 \cdot 6701) \left( \frac{a_0}{2^3} P + \frac{a_1}{2^2} P \right) \right) \, \text{mod} \, 2
$$

For the next factor,

$$
2^3 b_0 G = 2^3 R \, \text{mod} \, 6701
$$

Finally, we get

$$
x = x_1 \, \mod \, 2^3 \\
x = x_2 \, \mod \, 6701
$$

using the Chinese Remainder Theorem, we get

$$
x = 23752 \, \text{mod} \, 2^3 \cdot 6701
$$

---

### Feistel cipher

The given text `1+jn39uL7ZylzIrUzMicmEhlbGxAc0gxMnQtdGgxM30=\n` is in `base64`. On converting it to byte format we get `\xd7\xe8\xe7\xdf\xdb\x8b\xed\x9c\xa5\xcc\x8a\xd4\xcc\xc8\x9c\x98Hell@sH12t-th13}`. The last 16 bits of the total 32 bits are clearly part of the flag. This suggests that a Feistel cipher has been used.

The Fiestel cipher uses one round in which it uses $x$ as the round key. The round function is just a term by term XORing of the bits. So if the given input is $L1+R1$,
output is

$$
L2 = L1 \oplus f(R1, x)\\
R2 = R1
$$

The nice thing about Feistel cipher is that it is its own inverse. If we apply it one more time on the given text with the obtained value of $x$, we get the flag. A full soultion is outlined in [ECDH.py](ECDH.py) which uses the [elliptic_curve.py](elliptic_curve.py) file for ECC operations.
