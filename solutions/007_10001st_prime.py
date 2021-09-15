"""Solution to Project Euler Problem 7."""
import math
from typing import Tuple


def erathostenes_sieve(k: int, up_lim: int) -> Tuple[int, list]:
    """erathostenes_sieve.

    An implementation of the Erathostenes Sieve for
    finding prime numbers.

    Arguments
    ---------
    k : int
        The kth prime to be computed.
    up_lim: int
        The limit of integers to have as search space.

    Returns
    -------
    Tuple[int, list] : The kth prime number if found and the list
        of prime numbers, `-1` and the list of primes otherwise.

    Examples
    --------
    >>> erathostenes_sieve(3, 10,)
    5, [2, 3, 5, 7]
    """
    terms = [[x, True] for x in range(2, up_lim + 1)]
    primes = []
    i = 2
    while i <= math.sqrt(up_lim):
        term = terms[i - 2]
        if term[1] is True:
            j = term[0]
            while j <= up_lim / term[0]:
                terms[(j * term[0]) - 2][1] = False
                j += 1
        i += 1
    for term in terms:
        if term[1] is True:
            primes.append(term[0])
    if k <= len(primes):
        return primes[k - 1], primes
    print(f"Only {len(primes)} primes were found.")
    return -1, primes


if __name__ == "__main__":
    print(erathostenes_sieve(10001, 200000)[0])
