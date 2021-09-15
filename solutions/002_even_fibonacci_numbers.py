"""Solution to Project Euler #2 Problem."""
from typing import Generator


def fibonacci() -> Generator[int, None, None]:
    """fibonacci.

    Iterative Fibonacci implemetation with Python generators.

    Yields
    ------
    Generator[int, None, None] : The ith term of the Fibonacci Series.

    Examples
    --------
    >>> gen = fibonacci()
    >>> next(gen)
    0
    >>> next(gen)
    1
    """
    a = 0
    b = 1
    yield 0
    while True:
        c = a + b
        a = b
        b = c
        yield c


def even_fibonacci_sum(boundary: int) -> int:
    """even_fibonacci_sum.

    Finds the sum of the even Fibonacci's Serie terms.

    Arguments
    ---------
    boundary : int
        The limit of Fibonacci terms.

    Returns
    -------
    int : The sum of the even Fibonacci terms.

    Examples
    --------
    >>> even_fibonacci_sum(int(4e6),)
    4613732
    """
    even_sum = 0
    gen = fibonacci()
    n = 0
    while n < boundary:
        n = next(gen)
        if n % 2 == 0:
            even_sum += n
    return even_sum


if __name__ == "__main__":
    print(even_fibonacci_sum(int(4e6)))
