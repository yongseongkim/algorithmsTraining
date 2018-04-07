# -*- coding: utf-8 -*-
'''

정수 배열과 타겟 숫자가 주어지면, 합이 타겟값이 되는 두 원소의 인덱스를 찾으시오.
단, 시간복잡도 O(n) 여야 합니다.

예제)
Input: [2, 5, 6, 1, 10], 타겟 8
Output: [0, 2] // 배열[0] + 배열[2] = 8

'''


def find_index(inp, target):
    dp = dict()
    for i in range(len(inp)):
        # dictionary에 (target - i 번째 값)을 key로 i를 value로 저장한다.
        # 매번 i 번째 값을 dictionary에 있는지 확인하면서 있으면 해당 value(index)와 현재 i를 리턴한다.
        v = inp[i]
        if v >= target:
            continue
        if dp.get(v) is not None:
            return [dp.get(v), i]
        print(target - v, i)
        dp[target - v] = i
    return []


input_arr = [int(x) for x in input().split()]
print(find_index(input_arr[0:len(input_arr) - 1], input_arr[len(input_arr) - 1]))
