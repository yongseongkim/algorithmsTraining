# -*- coding:utf-8 -*-
total_case = input()
case_index = 0

strs = [input() for idx in range(int(total_case))]
fst = strs[0]
for i in range(0, len(fst)):
    same = False
    for j in range(1, len(strs)):
        same = fst[i] == strs[j][i]
        if not same:
            break
    if same:
        print(fst[i], end="")
    else:
        print("?", end="")
