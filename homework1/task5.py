from typing import List


def find_maximal_subarray_sum(nums: List[int], k: int) -> int:
    if k > len(nums):
        k = len(nums)
    max_sub_sum = 0
    for i in range(len(nums)):
        sub_sum = max_iteration_sum = 0
        for j in nums[i : i + k]:
            sub_sum += j
            if sub_sum > max_iteration_sum:
                max_iteration_sum = sub_sum
            print(f"{sub_sum=}")
            print(f"{max_iteration_sum=}")
        if max_iteration_sum > max_sub_sum:
            max_sub_sum = max_iteration_sum
        print(f"!!!{max_sub_sum=}")
    return max_sub_sum
