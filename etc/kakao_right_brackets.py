# 2020년 카카오 신입 블라인드 채용 1차 코딩 테스트
# https://tech.kakao.com/2019/10/02/kakao-blind-recruitment-2020-round1/

import sys
import collections

total_case = int(input())
case_index = 0


def is_balanced(s):
    num_open = 0
    num_close = 0
    for c in s:
        if c == '(':
            num_open += 1
        elif c == ')':
            num_close += 1
    return num_open == num_close


def is_right(s):
    stack = []
    for i in range(len(s)):
        if s[i] == '(':
            stack.append('(')
        elif s[i] == ')':
            if len(stack) > 0:
                stack.pop()
    return len(stack) == 0


def balanced(s):
    for i in range(1, len(s) + 1, 1):
        if is_balanced(s[:i]):
            return s[:i], s[i:]
    return [], s


def solve(s):
    # 1. 입력이 빈 문자열인 경우, 빈 문자열을 반환합니다.
    if not s:
        return s
    # 2. 문자열 w를 두 "균형잡힌 괄호 문자열" u, v로 분리합니다. 단, u는 "균형잡힌 괄호 문자열"로 더 이상 분리할 수 없어야 하며, v는 빈 문자열이 될 수 있습니다.
    tu, v = '', s
    while len(v) > 0:
        u, v = balanced(s)
        if is_right(u):
            # 3. 문자열 u가 "올바른 괄호 문자열" 이라면 문자열 v에 대해 1단계부터 다시 수행합니다.   
            # 3-1. 수행한 결과 문자열을 u에 이어 붙인 후 반환합니다.
            tu += u
        else:
            # 4. 문자열 u가 "올바른 괄호 문자열"이 아니라면 아래 과정을 수행합니다.
            # 4-1. 빈 문자열에 첫 번째 문자로 '('를 붙입니다.
            # 4-2. 문자열 v에 대해 1단계부터 재귀적으로 수행한 결과 문자열을 이어 붙입니다.
            # 4-3. ')'를 다시 붙입니다.
            # 4-4. u의 첫 번째와 마지막 문자를 제거하고, 나머지 문자열의 괄호 방향을 뒤집어서 뒤에 붙입니다.
            # 4-5. 생성된 문자열을 반환합니다.
            '(' + v + ')'
    return s
                
while case_index < total_case:
    # do something
    print(solve(input()))
    case_index += 1
