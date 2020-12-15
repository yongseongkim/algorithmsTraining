# https://leetcode.com/problems/kth-largest-element-in-an-array/
import heapq


def kth_largest_element_in_array(nums, k):
    heap = []
    for num in nums:
        heapq.heappush(heap, -num)
    result = None
    for _ in range(k):
        result = heapq.heappop(heap)
    return -result

print(kth_largest_element_in_array([3,2,1,5,6,4], 2)) # 5
print(kth_largest_element_in_array([3,2,3,1,2,4,5,5,6], 4)) # 4
