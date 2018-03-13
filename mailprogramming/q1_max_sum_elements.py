# -*- coding: utf-8 -*-
'''

정수 배열(int array)가 주어지면 가장 큰 이어지는 원소들의 합을 구하시오. 단, 시간복잡도는 O(n).

예제}
Input: -1 3 -1 5
Output: 7 // 3 + (-1) + 5

Input: -5 -3, -1
Output: -1 // -1

Input: 2 4 -2 -3 8
Output: 9 // 2 + 4 + (-2) + (-3) + 8

'''


def max_sum_connected_array(inp):
    max_sum = inp[0]
    sum = inp[0]
    for i in range(1, len(inp)):
        e = inp[i]
        if sum >= 0:
            sum += e
        else:
            sum = e
        if max_sum < sum:
            max_sum = sum
    return max_sum


input_arr = [int(x) for x in input().split()]
print(max_sum_connected_array(input_arr))
