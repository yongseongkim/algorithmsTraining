# -*- coding: utf-8 -*-
'''

간격(interval)로 이루어진 배열이 주어지면, 겹치는 간격 원소들을 합친 새로운 배열을 만드시오. 간격은 시작과 끝으로 이루어져 있으며 시작은 끝보다 작거나 같습니다.

예제)
Input: {{2,4}, {1,5}, {7,9}}
Output: {{1,5}, {7,9}}

Input: {{3,6}, {1,3}, {2,4}}
Output: {{1,6}}


'''


def find_cross_interval(intervals):
    sorted_intervals = sorted(intervals, key=lambda interval: interval[0])
    result = [sorted_intervals[0]]
    for interval in intervals:
        if result[-1][1] < interval[0]:
            result.append(interval)
        else:
            result[-1][1] = max(result[-1][1], interval[1])
    return result


filtinp = input().replace(' ', '').replace('{', '').replace('}', '').split(',')
print(find_cross_interval([[filtinp[i], filtinp[i + 1]] for i in range(0, len(filtinp), 2)]))
