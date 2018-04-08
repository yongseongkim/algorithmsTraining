# -*- coding: utf-8 -*-
'''

주어진 string 에 모든 단어를 거꾸로 하시오.

예제)
Input: “abc 123 apple”
Output: “cba 321 elppa”

'''


def reverse_words(inp):
    result = ''
    for i in range(len(inp) - 1, -1, -1):
        result += inp[i]
    return result


print(reverse_words(input()))
