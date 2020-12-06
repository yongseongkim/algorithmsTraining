# https://leetcode.com/problems/product-of-array-except-self/

import sys

total_case = int(input())
case_index = 0


def product_of_array_except_self(nums):
    l2r, r2l = nums[:], nums[:]
    lennums = len(nums)
    for idx in range(lennums):
        if idx > 0:
            l2r[idx] *= l2r[idx - 1]
        ridx = lennums - 1 - idx
        if ridx < lennums - 1:
            r2l[ridx] *= r2l[ridx + 1]
    result = []
    for idx in range(lennums):
        left = 1
        right = 1
        if idx - 1 >= 0:
            left = l2r[idx - 1]
        if idx + 1 <= lennums - 1:
            right = r2l[idx + 1]
        result.append(left * right)
    return result

while case_index < total_case:
    # do something
    nums = [int(x) for x in input().split(',')]
    print(product_of_array_except_self(nums))
    case_index += 1
