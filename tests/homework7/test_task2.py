from homework7.task2 import backspace_compare


def test_example_1():
    a = "ab#c"
    b = "ad#c"
    assert backspace_compare(a, b)


def test_example_2():
    a = "a##c"
    b = "#a#c"
    assert backspace_compare(a, b)


def test_example_3():
    a = "a#c"
    b = "b"
    assert not backspace_compare(a, b)


def test_empty_strings():
    a = ""
    b = ""
    assert backspace_compare(a, b)
