# https://leetcode.com/problems/group-anagrams/

import sys
import collections

total_case = int(input())
case_index = 0


def group_anagrams(words):
    group = collections.defaultdict(list)
    for word in words:
        # sorted(ate), sorted(tea), sorted(eat) -> aet
        sorted_word = ''.join(sorted(word))
        group[sorted_word].append(word)
    return group.values()

while case_index < total_case:
    # do something
    words = input().split(',')
    print(group_anagrams(words))
    case_index += 1
