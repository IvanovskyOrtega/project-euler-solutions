"""Solution to Project Euler Problem 13."""


def get_first_n_digits_of_sum(n: int) -> str:
    """get_first_n_digits_of_sum.

    Get the first `n` digits of a large integers sum given in the problem.

    I think this was easy in Python. :C
    My C language solution may be load the numbers as arrays, sum ith digits of
    each array with the carry (first carry will be 0, further iterations will
    be calculated by getting the integer division of the ith sum with 10) and
    append the residuals into a new array which will hold the result digits.

    Arguments
    ----------
    n : int
        The first `n` digits we want from the sum.

    Returns
    -------
    str : The `n` digits.

    Examples
    --------
    >>> get_first_n_digits_of_sum(10)
    5537376230
    """
    with open(
        "./files/100-50-digit-numbers.txt", "r", encoding="utf8"
    ) as input_file:
        nums = [int(num) for num in input_file.readlines()]
    res = sum(nums)
    return str(res)[:n]


if __name__ == "__main__":
    print(get_first_n_digits_of_sum(10))
