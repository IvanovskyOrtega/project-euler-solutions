"""Solution to Project Euler problem 8."""


def get_product(digits: list) -> int:
    """get_product.

    Find the product of the digits in a given string of digits.

    Parameters
    ----------
    digits : list
        A list of characters.

    Returns
    -------
    int : The product of the digits.

    Examples
    --------
    >>> get_product(["1", "2", "3"])
    6
    """
    product = 1
    for digit in digits:
        if digit == "0":
            return 0
        product *= int(digit)
    return product


def find_largest_product_in_a_series(s: str, n: int) -> int:
    """find_largest_product_in_a_series.

    Find the largest product of n-digits number in a string
    of m digits (m > n).

    Parameters
    ----------
    s : str
        The string of digits.
    n : int
        The amount of digits for the product.

    Returns
    -------
    int : The maximum product of n-digits.

    Examples
    --------
    >>> find_largest_product_in_a_series("123456", 3)
    120
    """
    i = 0
    j = i + n
    digits = list(s[i:j])
    max_product = 0
    while (i <= len(s) - n) and (j < len(s)):
        product = get_product(digits)
        max_product = max(product, max_product)
        digits.pop(0)
        digits.append(s[j])
        i += 1
        j += 1
    return max_product


if __name__ == "__main__":
    FILEPATH = "./files/1000-digit-number.txt"
    with open(FILEPATH, "r", encoding="utf-8") as f:
        content = f.readlines()
    STRING = "".join([x.replace("\n", "") for x in content])
    print(find_largest_product_in_a_series(STRING, 13))
