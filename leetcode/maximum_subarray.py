# https://leetcode.com/problems/maximum-subarray/

def maximum_subarray(nums):
    sums = [nums[0]]
    for i, v in enumerate(nums):
        if i == 0: continue
        sums.append(nums[i] if sums[i - 1] <= 0 else nums[i] + sums[i - 1])
    return max(sums)

print(maximum_subarray([-2,1,-3,4,-1,2,1,-5,4])) # 6
print(maximum_subarray([0])) # 0
print(maximum_subarray([1])) # 1
print(maximum_subarray([-1])) # -1
