# -*- coding: utf8 -*-
# https://algospot.com/judge/problem/read/FESTIVAL
# xrange, range랑 시간 차이 많이 난다.
# float 연산이 비효율적이니 나눈 값을 비교하지 말고 값은 비교하고 average를 구한다.
# 1~3까지 더한 값은 3까지 더한 값의 0까지 더한값을 빼면 된다. (for 문 줄이기)

test_case = int(input())
case = 0
while case < test_case:
    max_days, teams = [int(x) for x in input().split()]
    cost = [int(x) for x in input().split()]
    cost.insert(0, 0)
    for x in range(max_days + 1):
        if x != 0:
            cost[x] += cost[x-1]

    min_avr = float(cost[max_days]) / max_days
    # days는 예약할 날 수를 뜻한다. 최소 days는 team 수다.
    for days in range(teams, max_days + 1):
        min_sum = cost[max_days]
        for idx in range(days, max_days + 1):
            if min_sum > cost[idx] - cost[idx - days]:
                min_sum = cost[idx] - cost[idx - days]
        if min_avr > (float(min_sum) / days):
            min_avr = float(min_sum) / days
    print("%.11f" % min_avr)
    case += 1