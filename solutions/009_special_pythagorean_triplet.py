"""Solution to Project Euler Problem 9."""
import math
from typing import Tuple


def get_special_pythagorean_triplet(s: int) -> Tuple[tuple, int]:
    """get_special_pythagorean_triplet.

    Finds a Pythagorean triplet a**2 + b**2 = c**2 such
    a + b + c = s, using the Euclid's formula. In the code there's
    a condition m < math.sqrt(s/2) that is result of reducing the
    equality s = a + b + c = k * (m_squared + n_squared) + k * (2 * m * n) +
    k * (m_squared - n_squared).
    Which leads to:
    s/2 = m ** 2 + m * n (for k = 1)
    If we consider m >> n, then it turns to:
    s/2 = m ** 2
    We can make an assumption for m:
    m = math.sqrt(s / 2)
    And thus, set it as our search space limit.

    Arguments
    ---------
    s : int
        The desired value for `a + b + c = s`.

    Returns
    -------
    Tuple[tuple, int] : A tuple with the triplet and the product of
       `a * b * c` (as desired in the Problem 9) if found. A tuple
        with `(None, None, None), -1` otherwise.

    Examples
    --------
    >>> get_special_pythagorean_triplet(1000)
    ((425, 200, 375), 31875000)
    """
    m = 2
    while m < math.sqrt(s / 2):
        n = 1
        while n < m:
            if math.gcd(m, n) != 1:
                n += 1
                continue
            if (m + n) % 2 == 0:
                n += 1
                continue
            m_squared = m ** 2
            n_squared = n ** 2
            k = 1
            while True:
                a = k * (m_squared + n_squared)
                b = k * (2 * m * n)
                c = k * (m_squared - n_squared)
                if a + b + c == s:
                    return (a, b, c), a * b * c
                if a + b + c > s:
                    break
                k += 1
            n += 1
        m += 1
    return (None, None, None), -1


if __name__ == "__main__":
    print(get_special_pythagorean_triplet(1000))
