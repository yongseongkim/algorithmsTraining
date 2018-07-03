# -*- coding: utf-8 -*-
'''

정수 배열(int array)이 주어지면 0이 아닌 정수 순서를 유지하며 모든 0을 배열 오른쪽 끝으로 옮기시오. 단, 시간복잡도는 O(n), 공간복잡도는 O(1)여야 합니다.

예제)
Input: [0, 5, 0, 3, -1]
Output: [5, 3, -1, 0, 0]

Input: [3, 0, 3]
﻿Output: [3, 3, 0]


'''


def move_zero(inp):
    numbers = [int(x) for x in inp.split(',')]
    first_zero_idx = -1
    # 첫 번째 0인 index를 이용해서 값만 바꿔준다.
    for i in range(len(numbers)):
        if first_zero_idx == -1:
            # 첫 번째 0인 index가 없으면 그냥 이동
            if numbers[i] == 0:
                first_zero_idx = i
            continue
        if numbers[i] != 0:
            numbers[first_zero_idx] = numbers[i]
            numbers[i] = 0
            if i - first_zero_idx == 1:
                first_zero_idx = i
            else:
                first_zero_idx = first_zero_idx + 1
    return numbers


print(move_zero(input()))
