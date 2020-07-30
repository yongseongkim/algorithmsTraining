# -*- coding: utf8 -*-
# https://algospot.com/judge/problem/read/FENCE

total_case = int(input())
case_index = 0

# 무식하게 세기

def get_min_height(list):
	min_height = 10001
	for element in list:
		if min_height > element:
			min_height = element
	return min_height


def get_max_area(fences):
	max = 0
	for x1 in range(len(fences)):
		for x2 in range(x1, len(fences)):
			width = x2 - x1 + 1
			min_height = get_min_height(fences[x1:x2+1])
			area = width * min_height
			if area > max:
				max = area
	return max


while case_index < total_case:
	number_of_fences = int(input())
	fences = [int(x) for x in input().split(' ')]
	result = get_max_area(fences)
	print(result)
	case_index += 1
