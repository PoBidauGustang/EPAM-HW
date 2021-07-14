import pytest

from homework2.task2 import major_and_minor_elem


def test_major_and_minor_elem_one():
    assert major_and_minor_elem([0]) == (0, 0)


def test_major_and_minor_elem_same():
    assert major_and_minor_elem([3, 3, 3]) == (3, 3)


def test_major_and_minor_elem_common():
    assert major_and_minor_elem([2, 2, 1, 1, 1, 2, 2]) == (2, 1)


def test_major_and_minor_elem_negative():
    assert major_and_minor_elem([-1, 3, 3, -1, -1]) == (-1, 3)
