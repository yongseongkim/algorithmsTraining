# -*- coding: utf-8 -*-
'''

정수 배열(int array)이 주어지면 두번째로 큰 값을 프린트하시오.

예제)
Input: [10, 5, 4, 3, -1]
Output: 5

Input: [3, 3, 3]
Output: Does not exist.

'''


def second_max_value(inp):
    numbers = [int(x) for x in inp.split(',')]
    max = None
    second_max = None
    for n in numbers:
        if max is None:
            max = n
            continue
        if second_max is None:
            if n > max:
                second_max = max
                max = n
            elif max > n:
                second_max = n
            continue
        if n > max:
            second_max = max
            max = n
        elif second_max < n < max:
            second_max = n
    return second_max


second_max = second_max_value(input())
if second_max is None:
    print('Does not exist.')
else:
    print(second_max)
