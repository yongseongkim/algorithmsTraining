# https://leetcode.com/problems/longest-repeating-character-replacement/
import collections


def longest_repeating_character_replacement(s, k):
    left = right = 0
    counter = collections.Counter()
    for right in range(1, len(s) + 1):
        counter[s[right - 1]] += 1
        num_most_common_char = counter.most_common(1)[0][1]
        if right - left - num_most_common_char > k:
            counter[s[left]] -= 1
            left += 1
    return right - left

print(longest_repeating_character_replacement("ABAB", 2)) # 4
print(longest_repeating_character_replacement("AABABBA", 1)) # 4
