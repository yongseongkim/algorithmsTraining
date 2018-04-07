# -*- coding: utf-8 -*-
'''

정수 n이 주어지면, n개의 여는 괄호 "("와 n개의 닫는 괄호 ")"로 만들 수 있는 괄호 조합을 모두 구하시오. (시간 복잡도 제한 없습니다).

예제)
Input: 1
Output: ["()"]
Input: 2
Output: ["(())", "()()"]
Input: 3
Output: ["((()))", "(()())", "()(())", "(())()", "()()()"]

'''

dp = {}


def bracket_cases(n):
    global dp
    if n < 1:
        return ''
    if n == 1:
        dp[n] = set(['()'])
    else:
        if dp.get(n) is None:
            bracket_cases(n - 1)
            cases = set()
            subcases = dp.get(n - 1)
            for subcase in subcases:
                cases.add('({})'.format(subcase))
                cases.add('{}()'.format(subcase))
                cases.add('(){}'.format(subcase))
            dp[n] = cases
    return dp.get(n)


print(bracket_cases(int(input())))
