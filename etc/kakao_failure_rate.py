# 2019년 카카오 신입 공채 1차 코딩테스트
# https://tech.kakao.com/2018/09/21/kakao-blind-recruitment-for2019-round-1/#2-실패율

import sys

total_case = int(input())
case_index = 0


def failure_rate(N, stages):
    result = []
    users = {}
    for n in range(1, N + 1):
        users[n] = 0
    for stage in stages:
        users[stage] += 1
    keys = sorted(users.keys())
    for stage_level in range(1, N + 1):
        nclear = users[stage_level]
        total = sum(users[key] for key in keys[stage_level - 1:])
        result.append((float(nclear/total), stage_level))
    return [x[1] for x in sorted(result, key=lambda x: (-x[0], x[1]))]

while case_index < total_case:
    # do something
    N = int(input())
    stages = [int(x) for x in input().split(',')]
    print(failure_rate(N, stages))
    case_index += 1
