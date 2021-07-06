from typing import Sequence


def check_fibonacci(data: Sequence[int]) -> bool:
    length = len(data)
    if length == 0 or data[0] != 0:
        return False
    if length >= 2 and data[1] != 1:
        return False
    if length > 2:
        for i in range(2, length):
            if data[i] != data[i - 2] + data[i - 1]:
                return False
    return True
