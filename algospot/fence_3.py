# -*- coding: utf8 -*-
# https://algospot.com/judge/problem/read/FENCE

total_case = int(input())
case_index = 0


def get_max_area(fences):
	max_area = 0
	for i in range(len(fences) - 1):
		width = 1
		for j in range(i + 1, len(fences)):
			if fences[i] > fences[j]:
				width = j - i
				break
			elif j == len(fences) - 1:
				width = j - i + 1
		max_area = max([max_area, width * fences[i]])
	return max_area


while case_index < total_case:
	number_of_fences = input()
	fences = [int(x) for x in input().split(' ')]
	result = get_max_area(fences)
	print(result)
	case_index += 1
