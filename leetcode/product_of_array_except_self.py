# -*- coding: utf-8 -*-
# https://leetcode.com/problems/product-of-array-except-self/

import sys

total_case = int(input())
case_index = 0

def product_of_array_except_self(nums):
    l2r, r2l = [nums[0]], [nums[-1]]
    for idx in range(len(nums)):
        num = nums[idx]
        l2r.append(l# -*- coding: utf-8 -*-
# https://leetcode.com/problems/valid-palindrome/

import sys

total_case = int(input())
case_index = 0

def is_valid_palindrome(s):
    filtered = []
    for c in s:
        if c.isalnum():
            filtered.append(c.lower())
    while len(filtered) > 1:
        if filtered.pop(0) != filtered.pop():
            return False
    return True


while case_index < total_case:
    # do something
    target = input()
    print(is_valid_palindrome(target))
    case_index += 1
2r[-1] * num[idx])
        r2l.insert(0, r2l[0] * nums[idx])   
    result = []
    for idx in range(len(nums)):
        if idx == 0:
            result.append(r2l[1])
        elif idx == len(nums) - 1:
            result.append(l2r[-2])
        else:
            result.append(l2r[idx - 1] * r2l[idx + 1])
    return result


while case_index < total_case:
    # do something
    nums = [int(x) for x in input().split(',')]
    print(product_of_array_except_self(nums))
    case_index += 1
