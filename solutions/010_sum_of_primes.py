"""Solution to Project Euler Problem 10."""
import math
from typing import List


def erathostenes_sieve(n: int) -> List[int]:
    """erathostenes_sieve.

    Get the prime numbers below `n` using the Erathostenes Sieve algorithm.

    Parameters
    ----------
    n : int
        The limit for the Erathostenes Sieve.

    Returns
    -------
    List[int] : The list of primes below n.

    Examples
    --------
    >>> erathostenes_sieve(10)
    [2, 3, 5, 7]
    """
    sieve = [[x, True] for x in range(2, n + 1)]
    i = 2
    while i <= math.sqrt(n):
        if sieve[i - 2][1] is True:
            j = i
            while j <= n / i:
                sieve[(i * j) - 2][1] = False
                j += 1
        i += 1
    primes = []
    for term in sieve:
        if term[1] is True:
            primes.append(term[0])
    return primes


if __name__ == "__main__":
    print(sum(erathostenes_sieve(2000000)))
