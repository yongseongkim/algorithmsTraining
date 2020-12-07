# -*- coding:utf-8 -*-
# https://leetcode.com/problems/top-k-frequent-elements/
import collections
import heapq


def top_k_frequent(nums, k):
    freqs = collections.Counter(nums)
    hfreq = []
    for f in freqs:
        heapq.heappush(hfreq, (-freqs[f], f))
    result = []
    for _ in range(k):
        result.append(heapq.heappop(hfreq)[1])
    return result

print(top_k_frequent([1, 1, 1, 2, 2, 3], 2))
print(top_k_frequent([1], 1))
