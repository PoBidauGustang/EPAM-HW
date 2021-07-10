import pytest

from homework2.task4 import cache


def test_cache_positive():
    def func(a, b):
        return (a ** b) ** 2

    some = 100, 200

    cache_func = cache(func)

    val_1 = cache_func(*some)
    val_2 = cache_func(*some)

    assert val_1 is val_2


def test_cache_negative():
    def func(a, b):
        return (a ** b) ** 2

    some = 100, 200

    val_1 = func(*some)
    val_2 = func(*some)

    assert val_1 is not val_2


def test_cache_continious():
    def func(a, b):
        return (a ** b) ** 2

    some_1 = 1, 2
    some_2 = 2, 3
    val_1 = func(*some_1)
    val_2 = func(*some_2)
    val_3 = func(*some_1)
    val_4 = func(*some_2)

    assert val_1 is val_3
    assert val_2 is val_4
    assert val_1 is not val_2
