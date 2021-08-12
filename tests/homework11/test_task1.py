import pytest

from homework11.task1 import SimplifiedEnum


class ColorsEnum(metaclass=SimplifiedEnum):
    __keys = ("RED", "BLUE", "ORANGE", "BLACK")


class SizesEnum(metaclass=SimplifiedEnum):
    __keys = ("XL", "L", "M", "S", "XS")


def test_from_example_1():
    assert ColorsEnum.RED == "RED"


def test_from_example_2():
    assert SizesEnum.XL == "XL"


def test_positive():
    assert ColorsEnum.BLACK == "BLACK"


def test_non_existing_key():
    with pytest.raises(KeyError, match="No such key in class`s attribute '__keys'"):
        ColorsEnum.no_such_key
