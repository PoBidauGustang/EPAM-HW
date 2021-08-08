from homework9.task2 import Suppressor, suppressor


def test_example_from_task_with_class():
    with Suppressor(IndexError):
        [][2]


def test_example_from_task_with_foo():
    with suppressor(IndexError):
        [][2]


def test_with_NameError_with_class():
    with Suppressor(NameError):
        andrew


def test_with_NameError_with_foo():
    with suppressor(NameError):
        andrew


def test_with_ZeroDivisionError_with_class():
    with Suppressor(ZeroDivisionError):
        0 / 0


def test_with_ZeroDivisionError_with_foo():
    with suppressor(ZeroDivisionError):
        0 / 0
