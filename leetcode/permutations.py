# https://leetcode.com/problems/permutations/


def permutations(nums):
    result = []
    def rpermutations(nums, sets):
        if len(nums) == 1:
            result.append(sets + [nums[0]])
            return
        for i, v in enumerate(nums):
            cnums = nums[:]
            cnums.remove(v)
            rpermutations(cnums, sets + [v])
    rpermutations(nums, [])
    return result


print(permutations([1, 2, 3])) # [[1,2,3], [1,3,2], [2,1,3], [2,3,1], [3,1,2], [3,2,1]]
print(permutations([0, 1])) # [[0,1], [1,0]]
print(permutations([1])) # [[1]]
