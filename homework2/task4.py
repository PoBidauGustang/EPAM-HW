"""

Write a function that accepts another function as an argument. Then it
should return such a function, so the every call to initial one
should be cached.


def func(a, b):
    return (a ** b) ** 2


cache_func = cache(func)

some = 100, 200

val_1 = cache_func(*some)
val_2 = cache_func(*some)

assert val_1 is val_2

"""
from pickle import dumps
from typing import Callable


def cache(func: Callable) -> Callable:
    def wrapper(*args):
        dumped_arg = dumps(args)
        if dumped_arg in cache:
            return cache[dumped_arg]
        result = cache[dumped_arg] = func(*args)
        return result

    cache = {}
    return wrapper
