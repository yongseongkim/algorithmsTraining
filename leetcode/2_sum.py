# -*- coding:utf-8 -*-
# https://leetcode.com/problems/two-sum/
import sys
import collections

total_case = int(input())
case_index = 0


def two_sum(nums, target):
    for i in range(len(nums)-1):
        num = nums[i]
        if target - num in nums[i + 1:]:
            return [i, nums[i + 1:].index(target - num) + i + 1]
    return None

while case_index < total_case:
    # do something
    s = input()
    print(longest_palindrome_substring(s))
    case_index += 1
