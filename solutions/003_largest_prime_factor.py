"""Solution to Project Euler #3 Problem."""
from typing import Generator
import random


def primality_test(n: int, k: int) -> bool:
    if n == 2 or n == 3:
        return True
    if n % 2 == 0:
        return False
    s, d = 0, n - 1
    while d & 1 == 0:
        s, d = s + 1, d >> 1
    pp = True
    for _ in range(k):
        a = random.randint(2, n - 2)
        x =  pow(a, d, n)
        if x == 1 or x == (n - 1):
            continue
        for _ in range(1,s):
            x = pow(x, 2, n)
            if x == (n - 1):
                break
            elif x == 1:
                pp = False
        if not pp:
            return False
    return True


def prime_generator() -> Generator[int, None, None]:
    i = 2
    while True:
        if primality_test(i, 4):
            yield i
        i += 1

def largest_prime_factor(n: int) -> int:
    gp = prime_generator()
    max_prime = 0
    p = next(gp)
    while n > 1:
        if n % p != 0:
            p = next(gp)
        else:
            n, max_prime = n // p, p
    return max_prime

if __name__ == "__main__":
    print(largest_prime_factor(600851475143))
