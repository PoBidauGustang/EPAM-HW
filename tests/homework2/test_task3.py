from homework2.task3 import combinations


def test_combinations_common():
    assert combinations([1, 2], [3, 4]) == [
        [1, 3],
        [1, 4],
        [2, 3],
        [2, 4],
    ]


def test_combinations_zero():
    assert combinations([]) == []


def test_combinations_cut():
    assert combinations([1], [3], [5]) == [[1, 3, 5]]
