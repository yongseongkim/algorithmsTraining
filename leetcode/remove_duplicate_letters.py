# https://leetcode.com/problems/remove-duplicate-letters/
import collections


def remove_duplicate_letters(s):
    freqs = collections.Counter(s)
    result = []
    for c in s:
        freqs[c] -= 1
        if c in result:
            continue
        while result and c < result[-1] and freqs[result[-1]] > 0:
            result.pop()
        result.append(c)
    return ''.join(result)

print(remove_duplicate_letters('bcabc')) # abc
print(remove_duplicate_letters('cbacdcbc')) # acdb
print(remove_duplicate_letters('bbcaac')) # bac
print(remove_duplicate_letters('ebcabc')) # eabc
print(remove_duplicate_letters('ebcabce')) # abce
print(remove_duplicate_letters('abacb')) # abc
print(remove_duplicate_letters('bddbccd')) # bcd
