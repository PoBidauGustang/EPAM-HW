"""
Write a context manager, that suppresses passed exception.
Do it both ways: as a class and as a generator.

>>> with suppressor(IndexError):
...    [][2]

"""

from contextlib import contextmanager


@contextmanager
def suppressor(*exceptions):
    try:
        yield
    except exceptions:
        pass
    finally:
        pass


class Suppressor:
    def __init__(self, *exceptions):
        self._exception = exceptions

    def __enter__(self):
        pass

    def __exit__(self, exc_type, exc_val, exc_tb):
        return issubclass(exc_type, self._exception)
