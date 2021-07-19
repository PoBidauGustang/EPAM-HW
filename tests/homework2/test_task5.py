import string

import pytest

from homework2.task5 import custom_range


def test_combinations_start():
    assert custom_range(string.ascii_lowercase, "g") == ["a", "b", "c", "d", "e", "f"]


def test_combinations_end():
    assert custom_range(string.ascii_lowercase, "g", "p") == [
        "g",
        "h",
        "i",
        "j",
        "k",
        "l",
        "m",
        "n",
        "o",
    ]


def test_combinations_step():
    assert custom_range(string.ascii_lowercase, "p", "g", -2) == [
        "p",
        "n",
        "l",
        "j",
        "h",
    ]
