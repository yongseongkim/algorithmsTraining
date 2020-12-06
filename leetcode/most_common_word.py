# https://leetcode.com/problems/most-common-word/

import sys
import re
import collections

total_case = int(input())
case_index = 0


def most_common_word(paragraph, banned):
    frequency = collections.defaultdict(int)
    words = [word for word in re.sub(r'[^\w]', ' ', paragraph).lower().split() if word not in banned]
    for word in words:
        frequency[word] += 1
    word = max(frequency, key=frequency.get), frequency
    return word, frequency[word]


while case_index < total_case:
    # do something
    paragraph = input('paragraph = ')
    banned = input('banned = ').split(',')
    result = most_common_word(paragraph, banned)
    print(result)
    case_index += 1
