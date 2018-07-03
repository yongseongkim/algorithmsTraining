# -*- coding: utf-8 -*-
'''

주어진 string 에 모든 단어를 거꾸로 하시오.

예제)
Input: “abc 123 apple”
Output: “cba 321 elppa”

'''


def reverse_words(inp):
    result = []
    for word in inp.split(' '):
        result.append(reverse_word(word))
    return ' '.join(result)


def reverse_word(word):
    result = ''
    for i in range(len(word) - 1, -1, -1):
        result += word[i]
    return result


print(reverse_words(input()))
