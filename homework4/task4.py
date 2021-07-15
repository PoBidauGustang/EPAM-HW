from typing import List


def fizzbuzz(n: int) -> List[str]:
    """
    >>> fizzbuzz(0)
    []
    >>> fizzbuzz(3)
    ['1', '2', 'fizz']
    >>> fizzbuzz(5)
    ['1', '2', 'fizz', '4', 'buzz']
    >>> fizzbuzz(10)
    ['1', '2', 'fizz', '4', 'buzz', 'fizz', '7', '8', 'fizz', 'buzz']
    """
    fizzbuzz_numbers = []
    counter = 1
    while len(fizzbuzz_numbers) != n:
        if counter % 15 == 0:
            fizzbuzz_numbers.append("fizzbuzz")
        if counter % 3 == 0:
            fizzbuzz_numbers.append("fizz")
        elif counter % 5 == 0:
            fizzbuzz_numbers.append("buzz")
        else:
            fizzbuzz_numbers.append(f"{counter}")
        counter += 1
    return fizzbuzz_numbers
