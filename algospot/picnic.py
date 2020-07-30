# -*- coding:utf-8 -*-
# https://algospot.com/judge/problem/read/PICNIC

import sys

case = 0
totalCase = int(input())


def count_pairs(students, is_friend):
    #   students not exist
    if len(students) == 0:
        return 0
    #   students only two, friend
    if len(students) == 2 and is_friend[students[0]][students[1]]:
        return 1
    #   students only two, not friend
    if len(students) == 2 and not(is_friend[students[0]][students[1]]):
        return 0

    #   counting
    result = 0
    for i in range(1, len(students)):
        if is_friend[students[0]][students[i]]:
            __students = [students[j] for j in range(len(students)) if j is not 0 and j is not i]
            result += count_pairs(__students, is_friend)
    return result


while totalCase != case:
    input = sys.stdin.readline().strip().split()
    student_num, friend_case = int(input[0]), int(input[1])

    #   initialize is_friend, students_num x students_num matrix
    is_friend = [[False for j in range(student_num)] for i in range(student_num)]

    #   setup is_friend matrix
    input = sys.stdin.readline().strip().split()
    for j in range(0, len(input), 2):
        is_friend[int(input[j])][int(input[j + 1])] = True
        is_friend[int(input[j + 1])][int(input[j])] = True

    #   search for case from data
    print(count_pairs(range(student_num), is_friend))

    case += 1