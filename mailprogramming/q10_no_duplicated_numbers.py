# -*- coding: utf-8 -*-
'''

String이 주어지면, 중복된 char가 없는 가장 긴 서브스트링 (substring)의 길이를 찾으시오.

예제)
Input: “aabcbcbc”
Output: 3 // “abc”

Input: “aaaaaaaa”
Output: 1 // “a”

Input: “abbbcedd”
﻿Output: 4 // “bced”

'''


def remove_duplicated(inp):
    max_len_idx = (0, 0)
    idx = (0, 0)
    already = dict()
    for i in range(len(inp)):
        if already.get(inp[i]) is not None:
            already = dict()
            idx = (i, i)
            continue
        idx = (idx[0], i)
        if idx[1] - idx[0] > max_len_idx[1] - max_len_idx[0]:
            max_len_idx = idx
        already[inp[i]] = True
    print(max_len_idx)
    return inp[max_len_idx[0]: max_len_idx[1] + 1]


print(remove_duplicated(input()))
