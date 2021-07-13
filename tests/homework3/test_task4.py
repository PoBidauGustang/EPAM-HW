import pytest

from homework3.task4 import is_armstrong


def test_positive_1():
    assert is_armstrong(9)


def test_positive_2():
    assert is_armstrong(153)


def test_negative_1():
    assert not is_armstrong(19)


def test_negative_2():
    assert not is_armstrong(400)


def test_zero():
    assert is_armstrong(0)


def test_negative_number():
    assert not is_armstrong(-44)
