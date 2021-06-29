from typing import Tuple


def find_maximum_and_minimum(file_name: str) -> Tuple[int, int]:
    values = []
    with open(file_name) as fi:
        for line in fi:
            values.append(int(line))
    return (min(values), max(values))
