"""Solution to Project Euler Problem 6."""


def find_diff(n) -> int:
    """find_diff.

    Find the sum square difference. The algorithm
    performs the equation result of reducing the main
    formula. That instead calculating the squares
    we only calculate some products.

    Arguments
    ---------
    n : int
        The number of terms to differentiate (greater than
        zero).

    Returns
    -------
    int : The square difference.
    """
    if n <= 0:
        print("Not supported.")
        return -1
    terms = list(range(1, n + 1))
    result = 0
    for x in terms:
        for y in terms:
            result += x * y if x != y else 0
    return result


if __name__ == "__main__":
    print(find_diff(100))
