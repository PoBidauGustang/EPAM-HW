from homework11.task2 import Order


def morning_discount(order):
    ...


def elder_discount(order):
    ...


def test_from_example1():
    order_1 = Order(100, morning_discount)
    assert order_1.final_price() == 75


def test_from_example2():
    order_2 = Order(100, elder_discount)
    assert order_2.final_price() == 10
