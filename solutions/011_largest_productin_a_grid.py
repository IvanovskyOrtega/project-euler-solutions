"""Solution to Project Euler Problem 11."""
from typing import List


def find_greatest_product_in_rows(grid: List[List[int]], n: int) -> int:
    """find_greatest_product_in_rows.

    Find the greatest product of `n` consecutive numbers in the rows of a given
    grid.

    Arguments
    ----------
    grid : List[List[int]]
        The grid of numbers.
    n : int
        The amount of consecutive numbers to find its product.

    Returns
    -------
    int : The maximum product for the grid rows.

    Examples
    --------
    >>> find_greatest_product_in_rows([[1,2], [2,3]],2,)
    6
    """
    grid_size = len(grid)
    if n > grid_size:
        return -1
    max_prod = 0
    i = 0
    while i < grid_size:
        j = n - 1
        numbers = grid[i][0:n]
        while True:
            current_prod = 1
            for num in numbers:
                if num == 0:
                    current_prod = 0
                    break
                current_prod *= num
            max_prod = max(max_prod, current_prod)
            j += 1
            if j >= grid_size:
                break
            numbers.pop(0)
            numbers.append(grid[i][j])
        i += 1
    return max_prod


def find_greatest_product_in_cols(grid: List[List[int]], n: int) -> int:
    """find_greatest_product_in_cols.

    Find the greatest product of `n` consecutive numbers in the columns of a
    given grid.

    Arguments
    ----------
    grid : List[List[int]]
        The grid of numbers.
    n : int
        The amount of consecutive numbers to find its product.

    Returns
    -------
    int : The maximum product for the grid rows.

    Examples
    --------
    >>> find_greatest_product_in_rows([[1,2], [2,3]],2,)
    6
    """
    grid_size = len(grid)

    if n > grid_size:
        return -1

    max_prod = 0
    j = 0
    while j < grid_size:
        numbers = [grid[x][j] for x in range(0, n)]
        i = n - 1
        while True:
            currrent_prod = 1
            for num in numbers:
                if num == 0:
                    currrent_prod = 0
                    break
                currrent_prod *= num
            max_prod = max(max_prod, currrent_prod)
            i += 1
            if i >= grid_size:
                break
            numbers.pop(0)
            numbers.append(grid[i][j])
        j += 1
    return max_prod


def find_greatest_product_in_diags_l2r(grid: List[List[int]], n: int) -> int:
    """find_greatest_product_in_diags_12r.

    Find the greatest product of `n` consecutive numbers in the diagonals from
    left to right of a given grid.

    Arguments
    ----------
    grid : List[List[int]]
        The grid of numbers.
    n : int
        The amount of consecutive numbers to find its product.

    Returns
    -------
    int : The maximum product for the grid rows.

    Examples
    --------
    >>> find_greatest_product_in_rows([[1,2,3], [2,3,4]],2,)
    8
    """
    max_prod = 0
    i = 0
    grid_size = len(grid)
    j = grid_size - 1
    while i < grid_size:
        while j >= 0:
            numbers = []
            k = 0
            while ((j + k) < grid_size) and ((i + k) < grid_size):
                numbers.append(grid[i + k][j + k])
                k += 1
                if k < n:
                    continue
                current_prod = 1
                for num in numbers:
                    if num == 0:
                        current_prod = 0
                        break
                    current_prod *= num
                max_prod = max(max_prod, current_prod)
                numbers.pop(0)
            if k < n:
                j -= 1
                continue
            if j == 0:
                break
            j -= 1
        i += 1
    return max_prod


def find_greatest_product_in_diags_r2l(grid: List[List[int]], n: int) -> int:
    """find_greatest_product_in_diags_r2l.

    Find the greatest product of `n` consecutive numbers in the diagonals from
    right to left of a given grid.

    Arguments
    ----------
    grid : List[List[int]]
        The grid of numbers.
    n : int
        The amount of consecutive numbers to find its product.

    Returns
    -------
    int : The maximum product for the grid rows.

    Examples
    --------
    >>> find_greatest_product_in_rows([[1,2,3], [2,3,4]],2,)
    8
    """
    max_prod = 0
    grid_size = len(grid)
    i = grid_size - 1
    j = grid_size - 1
    while i >= 0:
        while j >= 0:
            numbers = []
            k = 0
            while ((j + k) < grid_size) and ((i - k) > 0):
                numbers.append(grid[i - k][j + k])
                k += 1
                if k < n:
                    continue
                current_prod = 1
                for num in numbers:
                    if num == 0:
                        current_prod = 0
                        break
                    current_prod *= num
                max_prod = max(max_prod, current_prod)
                numbers.pop(0)
            if k < n:
                j -= 1
                continue
            if j == 0:
                break
            j -= 1
        i -= 1
    return max_prod


def read_grid() -> List[List[int]]:
    """read_grid.

    Loads the grid of numbers from a static file.

    Returns
    -------
    List[List[int]] : The grid of numbers.

    Examples
    --------
    >>> read_grid()
    [[1, 2, 3, 4, 5],[6, 7, 8, 9, 10]]
    """
    filepath = "./files/grid.txt"
    with open(filepath, "r", encoding="utf8") as f:
        grid = f.readlines()
        grid_len = len(grid)
        for i in range(grid_len):
            grid[i] = grid[i].replace("\n", "").split(" ")
            for j in range(grid_len):
                grid[i][j] = int(grid[i][j])
        return grid


if __name__ == "__main__":
    sample_grid = read_grid()
    print(find_greatest_product_in_rows(sample_grid, 4))
    print(find_greatest_product_in_cols(sample_grid, 4))
    print(find_greatest_product_in_diags_l2r(sample_grid, 4))
    print(find_greatest_product_in_diags_r2l(sample_grid, 4))
