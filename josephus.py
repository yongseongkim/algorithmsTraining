# -*- coding:utf-8 -*-
total_case = input()
case_index = 0

while case_index < total_case:
    NK = [int(i) for i in raw_input().split()]
    N, K = NK[0], NK[1]

    player = [i for i in xrange(2, N + 1)]
    died = 0
    while len(player) != 2:
        died = died + K - 1
        while died >= len(player):
            died = died - len(player)
        player.pop(died)
    for i in player: print i,
    print ''
    case_index = case_index + 1
