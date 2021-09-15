"""Solution to Project Euler #3 Problem."""
from typing import Generator
import random


def primality_test(n: int, k: int) -> bool:
    """primality_test.

    Miller-Rabin + Fermat's primality test.

    Arguments
    ---------
    n : int
        The number to test if it's possible prime.
    k : int
        The number of rounds to apply the test.

    Returns
    -------
    bool : `True` if it's probably prime, `False` otherwise.

    Examples
    --------
    >>> primality_test(n,k,)
    #sampleResult
    """
    if n in (2, 3):
        return True
    if n % 2 == 0:
        return False
    s, d = 0, n - 1
    while d & 1 == 0:
        s, d = s + 1, d >> 1
    pp = True
    for _ in range(k):
        a = random.randint(2, n - 2)
        x = pow(a, d, n)
        if x in (1, n - 1):
            continue
        for _ in range(1, s):
            x = pow(x, 2, n)
            if x == (n - 1):
                break
            if x == 1:
                pp = False
        if not pp:
            return False
    return True


def prime_generator() -> Generator[int, None, None]:
    """prime_generator.

    Generates possible prime numbers using the Miller-Rabin + Fermat's
    primality tests.

    Yields
    ------
    Generator[int, None, None] : A probably prime number.

    Examples
    --------
    >>> gen = prime_generator()
    >>> next(gen)
    2
    >>> next(gen)
    3
    """
    i = 2
    while True:
        if primality_test(i, 4):
            yield i
        i += 1


def largest_prime_factor(n: int) -> int:
    """largest_prime_factor.

    Calculates the largest prime factor of a given number.

    Arguments
    ---------
    n : int
        The number to get its largest prime factor.

    Returns
    -------
    int : The largest prime factor for the given number.

    Examples
    --------
    >>> largest_prime_factor(600851475143,)
    6857
    """
    gen = prime_generator()
    max_prime = 0
    p = next(gen)
    while n > 1:
        if n % p != 0:
            p = next(gen)
        else:
            n, max_prime = n // p, p
    return max_prime


if __name__ == "__main__":
    print(largest_prime_factor(600851475143))
