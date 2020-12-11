# https://leetcode.com/problems/house-robber/
import collections


def house_robber(nums):
    if not nums:
        return 0
    if len(nums) <= 2:
        return max(nums)
    dp = collections.OrderedDict()
    dp[0], dp[1] = nums[0], max(nums[0], nums[1])
    for i in range(2, len(nums)):
        dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])
    return dp.popitem()[1]

print(house_robber([1,2])) # 2
print(house_robber([1,2,3])) # 4
print(house_robber([1,2,3,1])) # 4
print(house_robber([2,7,9,3,1])) # 12

[183,219,57,193,94,233,202,154,65,240,97,234,100,249,186,66,90,238,168,128,177,235,50,81,185,165,217,207,88,80,112,78,135,62,228,247,211]