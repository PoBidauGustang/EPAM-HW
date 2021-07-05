from itertools import product
from typing import List


def check_sum_of_four(a: List[int], b: List[int], c: List[int], d: List[int]) -> int:
    sum_of_zero_tuples = 0
    tuples = list(product(a, b, c, d))
    for i in tuples:
        if sum(i) == 0:
            sum_of_zero_tuples += 1
    return sum_of_zero_tuples
