# https://leetcode.com/problems/network-delay-time/
import collections
import heapq


def network_delay_time(times, N, K):
    graph = collections.defaultdict(list)
    for u, v, w in times:
        graph[u].append((v, w))

    Q = [(0, K)]
    taken_times = collections.defaultdict(int)
    while Q:
        time, node = heapq.heappop(Q)
        if node not in taken_times:
            taken_times[node] = time
            for adjacent, weight in graph[node]:
                heapq.heappush(Q, (time + weight, adjacent))
    # find not visited node after traverse.
    if len(taken_times) == N:
        return max(taken_times.values())
    return -1

print(network_delay_time([[2,1,1],[2,3,1],[3,4,1]], 4, 2)) # 2
