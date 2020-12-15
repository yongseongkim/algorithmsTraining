# https://leetcode.com/problems/letter-combinations-of-a-phone-number/


def letter_combinations_of_phone_number(digits):
    phone = {
        '2': ['a', 'b', 'c'],
        '3': ['d', 'e', 'f'],
        '4': ['g', 'h', 'i'],
        '5': ['j', 'k', 'l'],
        '6': ['m', 'n', 'o'],
        '7': ['p', 'q', 'r', 's'],
        '8': ['t', 'u', 'v'],
        '9': ['w', 'x', 'y', 'z'],
        '0': ['+']
    }

    def comb(digits, s):
        if not digits:
            if not s:
                return []
            return [s]
        chars = phone[digits[0]]
        result = []
        for char in chars:
            result.extend(comb(digits[1:], s + char))
        return result
    return comb(digits, "")

print(letter_combinations_of_phone_number('23')) # ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]
print(letter_combinations_of_phone_number('')) # []
print(letter_combinations_of_phone_number('2')) # ["a", "b", "c"]
