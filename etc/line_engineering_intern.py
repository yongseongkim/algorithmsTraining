# -*- coding:utf-8 -*-
# 2019년 상반기 LINE 인턴 채용 코딩테스트 문제
# https://engineering.linecorp.com/ko/blog/2019-firsthalf-line-internship-recruit-coding-test/

import sys

total_case = int(input())
case_index = 0

def solve(p_cony, p_brown):
    t = 1
    prev_p_brown_list = [p_brown]
    while True:
        if p_cony < 0 or p_cony > 200000:
            return -1
        if p_brown < 0 or p_brown > 200000:
            return -1
        p_cony += t
        moved = []
        for prev_p_brown in prev_p_brown_list:
            if p_cony == prev_p_brown + 1:
                return t
            else:
                moved.append(prev_p_brown + 1)
            if p_cony == prev_p_brown - 1:
                return t
            else:
                moved.append(prev_p_brown - 1)
            if p_cony == prev_p_brown * 2:
                return t
            else:
                moved.append(prev_p_brown * 2)
        prev_p_brown_list = moved
        t += 1

while case_index < total_case:
    # do something
    inputs = [int(x) for x in input().split(' ')]
    print(solve(inputs[0], inputs[1]))
    case_index += 1
