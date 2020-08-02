# -*- coding:utf-8 -*-
# https://leetcode.com/problems/longest-palindromic-substring/submissions/
import sys
import collections

total_case = int(input())
case_index = 0

def longest_palindrome_substring(s):
    already_palindrome = collections.defaultdict(bool)
    def is_palindrome(s):
        ls = list(s)
        while len(ls) > 1:
            if ls.pop(0) != ls.pop():
                return False
            if already_palindrome[''.join(ls)]:
                return True
        already_palindrome[s] = True
        return True
    if len(s) < 2 or s == s[::-1]:
        return s

    palindrome = ''
    for length in range(2, len(s) + 1):
        sidx = 0
        while sidx + length <= len(s):
            target = s[sidx:sidx + length]
            if is_palindrome(target) and len(palindrome) < len(target):
                palindrome = target
            sidx += 1
    return palindrome

while case_index < total_case:
    # do something
    s = input()
    print(longest_palindrome_substring(s))
    case_index += 1
