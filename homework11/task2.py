"""
You are given the following code:

class Order:
    morning_discount = 0.25

    def __init__(self, price):
        self.price = price

    def final_price(self):
        return self.price - self.price * self.morning_discount

Make it possible to use different discount programs.
Hint: use strategy behavioural OOP pattern.
https://refactoring.guru/design-patterns/strategy

Example of the result call:

def morning_discount(order):
    ...

def elder_discount(order):
    ...

order_1 = Order(100, morning_discount)
assert order_1.final_price() == 75

order_2 = Order(100, elder_discount)
assert order_2.final_price() == 10
"""
from abc import ABC, abstractmethod
from typing import Callable


def to_camel_case(snake_str: str) -> str:
    items = snake_str.split("_")
    return "".join(x.title() for x in items)


class Order:
    def __init__(self, price: int, variable_discount: Callable) -> None:
        discount_class_name = to_camel_case(variable_discount.__name__)
        staregy = globals()[discount_class_name]

        self.price = price
        self.discount = staregy.get_discount(self)

    def final_price(self) -> int:
        return self.price - self.price * self.discount


class Discount(ABC):
    @abstractmethod
    def get_discount(self) -> None:
        pass


class MorningDiscount(Discount):
    def get_discount(self) -> float:
        return 0.25


class ElderDiscount(Discount):
    def get_discount(self) -> float:
        return 0.9
