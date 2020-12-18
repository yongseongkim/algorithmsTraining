# https://leetcode.com/problems/cheapest-flights-within-k-stops/
import collections
import heapq


def cheapest_flights_within_k_stops(n, flights, src, dst, K):
    graph = collections.defaultdict(list)
    for u, v, w in flights:
        graph[u].append((v, w))

    Q = [(0, src, 0)]
    while Q:
        price, node, k = heapq.heappop(Q)
        if node == dst:
            return price
        if k <= K:
            for v, w in graph[node]:
                heapq.heappush(Q, (price + w, v, k + 1))
    return -1

print(cheapest_flights_within_k_stops(3, [[0,1,100],[1,2,100],[0,2,500]], 0, 2, 1)) 
# The cheapest price from city 0 to city 2 with at most 1 stop costs 200, as marked red in the picture.
print(cheapest_flights_within_k_stops(3, [[0,1,100],[1,2,100],[0,2,500]], 0, 2, 0))
# The cheapest price from city 0 to city 2 with at most 0 stop costs 500, as marked blue in the picture.
print(cheapest_flights_within_k_stops(3, [[0,1,1], [0,2,5], [1,2,1], [2,3,1]], 0, 3, 1)) # 6
