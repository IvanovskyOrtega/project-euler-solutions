"""Solution to Project Euler Problem 12."""
from math import sqrt
from typing import List


def prime_decomposition(n: int) -> int:
    """prime_decomposition.

    Calculates the primes decomposition powers and sums them to get the number
    of divisors that `n` has. The sum of the powers minus for each prime plus
    the num of prime factors will be the amount of divisors.

    Arguments
    ----------
    n : int
        The number to find its amount of divisors.

    Returns
    -------
    int : The number of divisor that `n` has.

    Examples
    --------
    >>> prime_decomposition([2,3],3,)
    2
    """
    prime_factors = set()
    powers = 1
    aux = n
    for prime in primes:
        current_pow = 1
        residual = aux % prime
        if residual == 0:
            prime_factors.add(prime)
        while residual == 0:
            aux = aux // prime
            residual = aux % prime
            current_pow += 1
        powers *= current_pow
        if aux == 1:
            break
    return powers


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
    i = 2
    sieve = [[x, True] for x in range(2, n + 1)]
    while i <= sqrt(n):
        j = i
        if sieve[i][1] is False:
            i += 1
            continue
        while j <= n // i:
            sieve[(i * j) - 2][1] = False
            j += 1
        i += 1
    primes_below_n = [term[0] for term in sieve if term[1] is True]
    return primes_below_n


primes = erathostenes_sieve(100000)


def get_triangular_num_with_over_n_divisors(divisors: int) -> int:
    """get_triangular_num_with_over_n_divisors.

    Gets the triangular number with more or equal than `n` divisors.

    Arguments
    ----------
    divisors : int
        The number of divisors that the triangular number must have.

    Returns
    -------
    int : The triangular number with more or equal than `n` divisors.

    Examples
    --------
    >>> get_triangular_num_with_over_n_divisors(500,)
    76576500
    """
    triang_num = 3
    i = 3
    while True:
        res = prime_decomposition(triang_num)
        if res >= divisors:
            return triang_num
        triang_num += i
        i += 1


if __name__ == "__main__":
    print(get_triangular_num_with_over_n_divisors(500))
