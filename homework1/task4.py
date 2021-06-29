from typing import List


def check_sum_of_four(a: List[int], b: List[int], c: List[int], d: List[int]) -> int:
    sum_of_zero_tuples = 0
    for i in a:
        for j in b:
            for k in c:
                for l in d:
                    if sum((i, j, k, l)) == 0:
                        sum_of_zero_tuples += 1
    return sum_of_zero_tuples


print(check_sum_of_four([5, 1], [-7, 0], [7, 0], [0, 0]))
