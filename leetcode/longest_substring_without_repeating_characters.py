# https://leetcode.com/problems/longest-substring-without-repeating-characters/

import sys

total_case = int(input())
case_index = 0


def longest_substring_without_repeating_characters(s):
    used = {}
    mxlen = start = 0
    for idx, char in enumerate(s):
        if char in used and start <= used[char]:
            start = used[char] + 1
        else:
            mxlen = max(mxlen, idx - start + 1)
        used[char] = idx
    return mxlen

while case_index < total_case:
    # do something
    print(longest_substring_without_repeating_characters(input()))
    case_index += 1
