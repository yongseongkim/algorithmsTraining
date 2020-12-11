# https://leetcode.com/problems/number-of-islands/
import collections


def number_of_islands(grid):
    pass

grid = [
    ["1","1","1","1","0"],
    ["1","1","0","1","0"],
    ["1","1","0","0","0"],
    ["0","0","0","0","0"]
]
print(number_of_islands(grid)) # 1
grid = [
    ["1","1","0","0","0"],
    ["1","1","0","0","0"],
    ["0","0","1","0","0"],
    ["0","0","0","1","1"]
]
print(number_of_islands(grid)) # 3
