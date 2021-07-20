from typing import Generator


def fizzbuzz(n: int) -> Generator:
    for i in range(1, n + 1):
        yield [f"{i}", "fizz", "buzz", "fizzbuzz"][(i % 3 == 0) + 2 * (i % 5 == 0)]
