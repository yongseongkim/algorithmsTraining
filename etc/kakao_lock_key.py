# 2019년 카카오 신입 공채 1차 코딩테스트
# https://tech.kakao.com/2019/10/02/kakao-blind-recruitment-2020-round1/
# Just search all cases.

import sys
import copy

total_case = int(input())
case_index = 0

def rotate90(key):
    return list(zip(*key[::-1]))


def match(lock, key):
    N = len(lock)
    M = len(key)
    extlock = [[0] * (N + 2 * M) for i in range((N + 2 * M))]
    for i in range(M, N + M, 1):
        for j in range(M, N + M, 1):
            extlock[i][j] = lock[i - N][j - N]
    for i in range(N + M + 1):
        for j in range(N + M + 1):
            is_matched = submatch(extlock, key, i, j, N, M)
            if is_matched:
                return True
    return False

            
def submatch(extlock, key, i, j, N, M):
    matched = copy.deepcopy(extlock)
    for k in range(M):
        for l in range(M):
            if matched[i + k][j + l] == 1 and key[k][l] == 1:
                return False
            matched[i + k][j + l] = key[k][l]
    for i in range(N):
        for j in range(N):
            if matched[M + i][M + j] == 0:
                return False
    return True


def solve(lock, key):
    result = match(lock, key)
    if result:
        return True
    rotated90 = rotate90(key)
    result = match(lock, rotated90)
    if result:
        return True
    rotated180 = rotate90(rotated90)
    result = match(lock, rotated180)
    if result:
        return True
    rotated270 = rotate90(rotated180)
    match(lock, rotated270)
    if result:
        return True
    return False

while case_index < total_case:
    # do something
    print('lock')
    lock = []
    lock.append([int(x) for x in input().split(',')])
    for i in range(len(lock[0]) - 1):
        lock.append([int(x) for x in input().split(',')])
    print('key')
    key = []
    key.append([int(x) for x in input().split(',')])
    for i in range(len(key[0]) - 1):
        key.append([int(x) for x in input().split(',')])
    print(solve(lock, key))
    case_index += 1
