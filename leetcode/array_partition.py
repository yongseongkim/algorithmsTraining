# https://leetcode.com/problems/array-partition-i/
import collections


def array_partition(nums):
    # [::2] 짝수 index 만
    return sum(sorted(nums)[::2])

print(array_partition([1, 4, 3, 2]))
print(array_partition([6, 2, 6, 5, 1, 2]))
