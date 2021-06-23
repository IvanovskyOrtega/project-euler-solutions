"""Solution to Project Euler #1 Problem."""

def multiples_sum(numbers: list, boundary: int) -> int:
    multiples_sum = 0
    seen = set()
    for num in numbers:
        i = 1
        multiple = num
        while multiple < 1000:
            if multiple not in seen:
                multiples_sum += multiple
                seen.add(multiple)
            i = i + 1
            multiple = num * i
        print(seen)
    return multiples_sum

if __name__ == "__main__":
    print(multiples_sum([3,5], 1000))
