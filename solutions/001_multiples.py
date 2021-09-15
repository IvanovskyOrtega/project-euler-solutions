"""Solution to Project Euler #1 Problem."""


def multiples_sum(numbers: list, boundary: int) -> int:
    """multiples_sum.

    Find the sum of the multiples below `boundary` of the given `numbers` list.

    Arguments
    ---------
    numbers : list
        The list of numbers to sum their multiples.
    boundary : int
        The boundary of natural numbers.

    Returns
    -------
    int : The sum of the multiples.

    Examples
    --------
    >>> multiples_sum([3, 5], 1000,)
    233168
    """
    res = 0
    seen = set()
    for num in numbers:
        i = 1
        multiple = num
        while multiple < boundary:
            if multiple not in seen:
                res += multiple
                seen.add(multiple)
            i = i + 1
            multiple = num * i
    return res


if __name__ == "__main__":
    print(multiples_sum([3, 5], 1000))
