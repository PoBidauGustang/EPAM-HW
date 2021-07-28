from homework5.task2 import custom_sum


def test_original_name():
    assert custom_sum.__name__ == "custom_sum"


def test_original_doc():
    assert custom_sum.__doc__ == "This function can sum any objects which have __add__"


def test_original_func(capsys):
    print(custom_sum.__original_func)
    captured = capsys.readouterr()
    assert "<function custom_sum at " in captured.out


def test_sum_func_without_print():
    without_print = custom_sum.__original_func
    assert without_print(1, 2, 3, 4) == 10
