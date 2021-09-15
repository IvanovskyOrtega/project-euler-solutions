"""Solution to Project Euler Problem 5.

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


divisors = list(range(11, 21))


def gcd(a: int, b: int) -> int:
    """gcd.

    Euclid's algorithm to calculate the GCD.

    Arguments
    ----------
    a : int
        The first number.
    b : int
        The second number.

    Returns
    -------
    int : The GCD for a and b.

    Examples
    --------
    >>> gcd(3, 1,)
    1
    """
    remainders = []
    remainders.append(a)
    remainders.append(b)
    i = 1
    while remainders[i] != 0:
        remainders.append(remainders[i - 1] % remainders[i])
        i += 1
    return remainders[i - 1]


def lcm(a: int, b: int) -> int:
    """lcm.

    Get the LCM for the given numbers.

    Arguments
    ----------
    a : int
        The first number.
    b : int
        The second number.

    Returns
    -------
    int : The LCM for a and b.

    Examples
    --------
    >>> lcm(3,1,)
    3
    """
    return a // gcd(a, b) * b


def smallest_multiple() -> int:
    """smallest_multiple.

    Get the smallest positive number that is evenly divisible by al the numbers
    from 1-20.

    Returns
    -------
    int : The LCM for the divisors list.

    Examples
    --------
    >>> smallest_multiple()
    232792560
    """
    res = 1
    for d in divisors:
        res = lcm(res, d)
    return res


if __name__ == "__main__":
    print(smallest_multiple())
