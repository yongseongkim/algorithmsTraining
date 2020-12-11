# https://leetcode.com/problems/longest-palindromic-substring/submissions/
import sys
import collections

total_case = int(input())
case_index = 0


def longest_palindrome_substring(s):
    def is_palindrome(substr):
        return substr == substr[::-1]
    if not s:
        return ''
    for window in range(len(s), 0, -1):
        for i in range(0, len(s) - window + 1):
            substr = s[i:i+window]
            if is_palindrome(substr):
                return substr
    return s[0]

while case_index < total_case:
    # do something
    s = input()
    print(longest_palindrome_substring(s))
    case_index += 1
