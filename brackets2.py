# -*- coding: utf8 -*-

YES = 'YES'
NO = 'NO'
OPEN_BRACKET = ['(', '[', '{']
CLOSE_BRACKET = [')', ']', '}']


def check_brackets(str):
    stack = []
    for ch in str:
        if ch in OPEN_BRACKET:
            stack.append(ch)
        elif ch in CLOSE_BRACKET:
            if len(stack) == 0:
                return NO
            prev_bracket = stack.pop()
            if prev_bracket == '(':
                if ch != ')':
                    return NO
            elif prev_bracket == '[':
                if ch != ']':
                    return NO
            elif prev_bracket == '{':
                if ch != '}':
                    return NO
    if len(stack) != 0:
        return NO
    return YES

test_case = input()
case = 0
while case < test_case:
    str = raw_input()
    print check_brackets(str)
    case += 1