# https://leetcode.com/problems/minimum-height-trees/
import collections


def minimum_height_trees(n, edges):
    if n <= 1:
        return [0]
    graph = collections.defaultdict(list)
    for f, t in edges:
        graph[f].append(t)
        graph[t].append(f)
    prev = graph

    while n > 2:
        leaves = [v for v in list(graph) if len(graph[v]) == 1]
        for leaf in leaves:
            neighbor = graph[leaf].pop()
            graph[neighbor].remove(leaf)
            del graph[leaf]
        n -= len(leaves)
    return [v for v in list(graph)]

print(minimum_height_trees(4, [[1,0],[1,2],[1,3]])) # [1]
print(minimum_height_trees(6, [[3,0],[3,1],[3,2],[3,4],[5,4]])) # [3,4]
print(minimum_height_trees(1, [])) # [0]
print(minimum_height_trees(2, [[0,1]])) # [0,1]
