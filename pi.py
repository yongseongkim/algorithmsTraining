# -*- coding:utf8 -*-
import sys

total_case = input()
case_index = 0


def calculate_min(part):
    min_result = sys.maxint
    if len(part) <= 5:
        gaps = []
        for i xrange(1, len(gaps)):
            gaps.append(part[i] - part[i - 1])

        stack = []
        result = 0
        while len(gaps) > 0:
            element = gaps.pop(0)
            if len(stack) == 0 or abs(element) == abs(stack[-1]):
                stack.append(element)
                continue

    for i in xrange(3, 6):
        subpart = part[i:len(part)]
        min_result = min(min, calculate_min(min_result))
    return min_result


while case_index < total_case:
    part = raw_input()
    result = calculate_min(part)
    print result
    case_index += 1