from typing import List


def find_maximal_subarray_sum(nums: List[int], k: int) -> int:
    if k > len(nums):
        k = len(nums)
    max_sub_sum = 0
    for i in range(len(nums) - (k - 1)):
        sub_sum = 0
        for index in range(i, i + k):
            sub_sum += nums[index]
        if sub_sum > max_sub_sum:
            max_sub_sum = sub_sum
    return max_sub_sum


print(find_maximal_subarray_sum([3, 22, 2, -17, 5], 3))
