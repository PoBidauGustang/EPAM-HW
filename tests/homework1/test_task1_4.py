from homework1.task4 import check_sum_of_four


def test_sum_of_four_case_16():
    assert check_sum_of_four([0, 0], [0, 0], [0, 0], [0, 0]) == 16


def test_sum_of_four_case_8():
    assert check_sum_of_four([0, 0], [0, 0], [7, 0], [0, 0]) == 8


def test_sum_of_four_case_4():
    assert check_sum_of_four([0, 5], [-7, 0], [7, 0], [0, 0]) == 4


def test_sum_of_four_case_0():
    assert check_sum_of_four([1, 5], [-7, 0], [7, 0], [0, 0]) == 0
