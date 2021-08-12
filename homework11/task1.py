"""
Vasya implemented nonoptimal Enum classes.
Remove duplications in variables declarations using metaclasses.

from enum import Enum

class ColorsEnum(Enum):
    RED = "RED"
    BLUE = "BLUE"
    ORANGE = "ORANGE"
    BLACK = "BLACK"

class SizesEnum(Enum):
    XL = "XL"
    L = "L"
    M = "M"
    S = "S"
    XS = "XS"

Should become:

class ColorsEnum(metaclass=SimplifiedEnum):
    __keys = ("RED", "BLUE", "ORANGE", "BLACK")

class SizesEnum(metaclass=SimplifiedEnum):
    __keys = ("XL", "L", "M", "S", "XS")

assert ColorsEnum.RED == "RED"
assert SizesEnum.XL == "XL"
"""


class SimplifiedEnum(type):
    def __new__(cls: str, name, bases: tuple, dct: dict) -> super:
        return super().__new__(cls, name, bases, dct)

    def __getattr__(cls, item: str) -> str:
        if item in cls.__dict__[f"_{cls.__name__}__keys"]:
            return item
