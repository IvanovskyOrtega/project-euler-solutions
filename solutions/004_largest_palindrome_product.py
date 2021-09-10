"""Solution to Project Euler Problem 4."""

def is_palindrome(n: int) -> bool:
    """is_palindrome.

    This function determines if a given integer number is a
    palindrome or not.

    Parameters
    ----------
    n : int
        The number to check if is palindrome.

    Returns
    -------
    bool : `True` if is palindrome, `False` otherwise.
    """
    n_str = str(n)
    l = len(n_str)
    i = 0
    while i < l // 2:
        if n_str[i] != n_str[l - i - 1]:
            return False
        i += 1
    return True

def largest_palindrome_product(n_digits: int) -> int:
    """largest_palindrome_product.

    This function returns the largest palindrome product
    of two n-digit numbers.

    Parameters
    ----------
    The number of digits for the numbers.

    Returns
    -------
    int : The largest palindrome
    """
    res = 0
    lower_bound = 10 ** (n_digits - 1)
    upper_bound = 10 ** n_digits
    j = lower_bound
    it = 1
    for i in range(lower_bound, upper_bound):
        while j < upper_bound:
            n = i * j
            if is_palindrome(n):
                res = n if n > res else res
            j += 1
        j = lower_bound + it # Avoid to re-compute previous cases
        it += 1
    return res

if __name__ == "__main__":
    print(largest_palindrome_product(3))
