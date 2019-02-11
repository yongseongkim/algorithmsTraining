# -*- coding:utf-8 -*-

# 7 명을 선택하기 보다는 2명을 제외하는 방식
def find_7dwarfs(dwarfs):
    dwarfs = _find_7dwarfs(dwarfs, [])
    if dwarfs is None:
        return
    for dwarf in dwarfs:
        print(dwarf)

def _find_7dwarfs(dwarfs, sum_dwarfs):
    if len(sum_dwarfs) == 7 and sum(sum_dwarfs) == 100:
        return sum_dwarfs
    if len(dwarfs) == 0 or sum(sum_dwarfs) > 100:
        return None
    result = _find_7dwarfs(dwarfs[1:], sum_dwarfs)
    if result is None:
        result = _find_7dwarfs(dwarfs[1:], sum_dwarfs + [dwarfs[0]])
    return result

dwarfs = sorted([int(input()) for i in range(9)])
find_7dwarfs(dwarfs)
