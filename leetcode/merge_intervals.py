# https://leetcode.com/problems/merge-intervals/
import collections


def merge_intervals(intervals):
    merged = []
    for interval in sorted(intervals):
        if not merged:
            merged.append(interval)
            continue
        if interval[0] <= merged[-1][1]:
            merged[-1][1] = max(interval[1], merged[-1][1])
        else:
            merged.append(interval)
    return merged

print(merge_intervals([[1,3],[2,6],[8,10],[15,18]])) # [[1,6],[8,10],[15,18]]
print(merge_intervals([[1,4],[4,5]])) # [[1,5]]
print(merge_intervals([[1,4],[0,4]])) # [[0,4]]
print(merge_intervals([[1,4],[2,3]])) # [[1,4]]
