# https://algospot.com/judge/problem/read/JOSEPHUS

total_case = int(input())
case_index = 0

while case_index < total_case:
    NK = [int(i) for i in input().split()]
    N, K = NK[0], NK[1]

    player = [i for i in range(2, N + 1)]
    died = 0
    while len(player) != 2:
        died = died + K - 1
        while died >= len(player):
            died = died - len(player)
        player.pop(died)
    for i in player: print(i, end=' ')
    case_index = case_index + 1
