import pytest

from homework1.task5 import find_maximal_subarray_sum


def test_max_subarray_sum_case_positive():
    assert find_maximal_subarray_sum([1, 3, -1, -3, 5, 3, 6, 7], 3) == 16


def test_sum_of_four_case_one_item():
    assert find_maximal_subarray_sum([6], 1) == 6


def test_sum_of_four_case_0():
    assert find_maximal_subarray_sum([0], 1) == 0


def test_sum_of_four_case_big_sub_array():
    assert find_maximal_subarray_sum([3, 22, 2, -17, 5], 111) == 15
