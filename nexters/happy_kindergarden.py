# -*- coding:utf-8 -*-

nk = input().split(' ')
k = int(nk[1])
students = [int(x) for x in input().split(' ')]
max_diffs = []
sum = 0 

for i in range(1, len(students)):
    diff = students[i] - students[i - 1]
    max_diffs.append(diff)
    if len(max_diffs) == k:
        max_diffs.sort()
        if diff > max_diffs[0]:
            sum += max_diffs[0]
            del max_diffs[0]
            max_diffs.append(diff)
        else:
            sum += diff
print(sum)