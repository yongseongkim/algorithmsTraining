# -*- coding:utf-8 -*-
# https://leetcode.com/problems/daily-temperatures/
import collections


def daily_temperatures(nums):
    result = [0 for _ in range(len(nums))]
    stacks = []
    for i in range(len(nums)):
        while stacks and nums[stacks[-1]] < nums[i]:
            latest_idx = stacks.pop()
            result[latest_idx] = i - latest_idx
        stacks.append(i)
    return result

print(daily_temperatures([73, 74, 75, 71, 69, 72, 76, 73]))
