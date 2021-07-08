from typing import List, Tuple


def major_and_minor_elem(inp: List) -> Tuple[int, int]:
    minor = inp[0]
    major = None
    min_count = len(inp) // 2
    for item in set(inp):
        count_items = inp.count(item)
        if count_items > len(inp) // 2:
            major = item
        if count_items <= min_count:
            minor, min_count = item, count_items
    return (major, minor)
