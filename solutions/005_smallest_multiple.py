"""Solution to Project Euler Problem 5."""

import math

"""
Let n be an integer | n >= 1
n is divisible by 1.
If n is divisible by 20, it is divisible by 10, 5, 4, 2, 1
-------------------- 18, ------------------ 9, 3, 6, 2, 1
-------------------- 16, ------------------ 8, 4, 2, 1
-------------------- 15, ------------------ 5, 3, 1
-------------------- 14, ------------------ 7, 2, 1
-------------------- 12, ------------------ 6 ,2, 1
19, 17, 13, 11 are primes

We only need to calculate the LCM for 20,19,18,17,16,15,14,13,12,11
"""

divisors = [i for i in range(11,21)]

def gcd(a: int, b: int) -> int:
    r = []
    r.append(a)
    r.append(b)
    i = 1
    while r[i] != 0:
        r.append(r[i - 1] % r[i])
        i += 1
    return r[i - 1]

def lcm(a: int ,b: int) -> int:
    return a // gcd(a, b) * b

def smallest_multiple():
    res = 1
    for d in divisors:
        res = lcm(res, d)
    return res

if __name__ == "__main__":
    print(smallest_multiple())
