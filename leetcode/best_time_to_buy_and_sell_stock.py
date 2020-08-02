# -*- coding: utf-8 -*-
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
