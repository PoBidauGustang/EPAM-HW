from pickle import dumps
from typing import Callable


def cache(times: int) -> Callable:

    initial_times = times

    def num_try(func):
        def wrapper(*args):
            dumped_arg = dumps(args)
            nonlocal times
            if dumped_arg in memory and times:
                times -= 1
                return memory[dumped_arg]
            result = memory[dumped_arg] = func(*args)
            times = initial_times
            return result

        memory = {}
        return wrapper

    return num_try
