import pytest

from homework9.task1 import merge_sorted_files

path_to_file1 = "tests/homework9/file1.txt"
path_to_file2 = "tests/homework9/file2.txt"


def test_from_example():
    assert list(merge_sorted_files([path_to_file1, path_to_file2])) == [
        1,
        2,
        3,
        4,
        5,
        6,
    ]


def test_for_iterator_protocol():
    iterator_1 = merge_sorted_files([path_to_file1, path_to_file2])
    assert "__iter__" in dir(iterator_1)
    assert "__next__" in dir(iterator_1)


def test_next_method():
    iterator_2 = merge_sorted_files([path_to_file1, path_to_file2])
    assert next(iterator_2) == 1
    assert next(iterator_2) == 2
    assert next(iterator_2) == 3
    assert next(iterator_2) == 4
    assert next(iterator_2) == 5
    assert next(iterator_2) == 6
    with pytest.raises(StopIteration):
        assert next(iterator_2)
