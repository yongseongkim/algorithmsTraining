# -*- coding: utf-8 -*-
# https://leetcode.com/problems/trapping-rain-water

import sys

total_case = int(input())
case_index = 0


def trapped_volume(heights):
    lmax = 0
    rmax = 0
    lidx = 0
    ridx = len(heights) - 1
    volume = 0
    while lidx < ridx:
        lmax, rmax = max(heights[lidx], lmax), max(heights[ridx], rmax)
        if lmax < rmax:
            volume += lmax - heights[lidx]
            lidx += 1
        else:
            volume += rmax - heights[ridx]
            ridx -= 1
    return volume

while case_index < total_case:
    # do something
    heights = [int(height) for height in input().split(',')]
    print(trapped_volume(heights))
    case_index += 1
