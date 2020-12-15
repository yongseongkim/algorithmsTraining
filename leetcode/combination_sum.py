# https://leetcode.com/problems/combination-sum


def combination_sum(nums, target):
    result = []
    def csum(nums, target, path):
        if target < 0:
            return
        if target == 0:
            result.append(path)
            return
        for i in range(len(nums)):
            csum(nums[i:], target - nums[i], path + [nums[i]])
    csum(nums, target, [])
    return result

print(combination_sum([2, 3, 6, 7], 7)) # [[7], [2,2,3]]
print(combination_sum([2, 3, 5], 8)) # [[2,2,2,2],[2,3,3],[3,5]]
print(combination_sum([1], 1)) # [[1]]
print(combination_sum([1], 2)) # [[1,1]]
