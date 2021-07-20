from typing import Generator

from homework4.task5 import fizzbuzz


def test_fizzbuzz_positive():
    assert list(fizzbuzz(18)) == [
        "1",
        "2",
        "fizz",
        "4",
        "buzz",
        "fizz",
        "7",
        "8",
        "fizz",
        "buzz",
        "11",
        "fizz",
        "13",
        "14",
        "fizzbuzz",
        "16",
        "17",
        "fizz",
    ]


def test_fizzbuzz_is_generator():
    """checking that output is a generator"""
    assert isinstance(fizzbuzz("anything"), Generator)
