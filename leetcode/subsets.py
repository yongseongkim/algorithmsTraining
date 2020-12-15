# https://leetcode.com/problems/subsets/
import collections


def subsets(nums):
    def rsubsets(nums, sets):
        if len(nums) == 0:
            return [sets]
        result = []
        result.extend(rsubsets(nums[1:], sets + [nums[0]]))
        result.extend(rsubsets(nums[1:], sets))
        return result
    return sorted(rsubsets(nums, []))

print(subsets([1, 2, 3])) # [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
print(subsets([0])) # [[],[0]]
