# -*- coding:utf-8 -*-
istr = input().split(' ')
tnum, tsum = int(istr[0]), int(istr[1])
iset = [int(x) for x in input().split(' ')]
total_case = 0
def sub_sum(list, sum_list):
    global total_case
    if len(list) == 0:
        if len(sum_list) > 0 and tsum == sum(sum_list):
            total_case += 1
        return
    sub_sum(list[1:], sum_list)
    sub_sum(list[1:], sum_list + [list[0]])

sub_sum(iset, [])
print(total_case)