# -*- coding: utf-8 -*-
'''

정수(int)가 주어지면, 팰린드롬(palindrome)인지 알아내시오.
팰린드롬이란, 앞에서부터 읽으나 뒤에서부터 읽으나 같은 단어를 말합니다.
단, 정수를 문자열로 바꾸면 안됩니다

예제)

Input: 12345
Output: False

Input: -101
Output: False

Input: 11111
Output: True

Input: 12421
﻿Output: True

'''


def is_palindrome(inp):
    if inp < 0:
        return False
    digits = []
    value = inp
    while value != 0:
        digits.append(value % 10)
        value = int(value / 10)
    for i in range(int(len(digits) / 2)):
        if digits[i] != digits[len(digits) - i - 1]:
            return False
    return True


print(is_palindrome(int(input())))
