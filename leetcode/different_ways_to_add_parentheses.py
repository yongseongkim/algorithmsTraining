# https://leetcode.com/problems/different-ways-to-add-parentheses/


def compute(left, right, operator):
    result = []
    for l in left:
        for r in right:
            if operator == '+':
                result.append(l + r)
            elif operator == '-':
                result.append(l - r)
            elif operator == '*':
                result.append(l * r)
    return result


def different_ways_to_add_parentheses(input):
    if input.isdigit():
        return [int(input)]
    result = []
    for idx in range(len(input)):
        c = input[idx]
        if c in '+-*':
            left, right = input[0:idx], input[idx+1:]
            result.extend(compute(different_ways_to_add_parentheses(left), different_ways_to_add_parentheses(right), c))
    return sorted(result)

print(different_ways_to_add_parentheses("2-1-1")) # [0, 2]
print(different_ways_to_add_parentheses("2*3-4*5")) # [-34, -14, -10, -10, 10]
