"""Solution to Project Euler #2 Problem."""

def fibonacci() -> int:
    a = 0
    b = 1
    yield 0
    while True:
        c = a + b
        a = b
        b = c
        yield c

def even_fibonacci_sum(boundary: int) -> int:
    even_sum = 0
    gen = fibonacci()
    n = 0
    while n < boundary:
        n = next(gen)
        if n % 2 == 0:
            even_sum += n
    return even_sum

if __name__ == "__main__":
    print(even_fibonacci_sum(4e6))
