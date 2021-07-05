import pytest

from homework1.task3 import find_maximum_and_minimum


def test_max_and_min_case_positive():
    """Testing that function finds min and max values correctly"""
    assert find_maximum_and_minimum("tests/tekst.txt") == (-5, 345)
