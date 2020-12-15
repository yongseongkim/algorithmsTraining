# https://leetcode.com/problems/course-schedule
import collections


def course_schedule(num_courses, preqs):
    if not preqs:
        return True
    graph = collections.defaultdict(list)
    for x, y in preqs:
        graph[x].append(y)
    
    visited = set()
    def dfs(v):
        if v in visited:
            return False
        visited.add(v)
        for w in graph[v]:
            if not dfs(w):
                return False
        visited.remove(v)
        return True
    for v in list(graph):
        if not dfs(v):
            return False
    return True

print(course_schedule(2, [[1,0]])) # true
print(course_schedule(2, [[1,0],[0,1]])) # false
print(course_schedule(3, [[0,1],[0,2],[1,2]])) # true
print(course_schedule(4, [[2,0],[1,0],[3,1],[3,2],[1,3]])) # false
