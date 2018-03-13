# -*- coding: utf-8 -*-
'''

피보나치 배열은 0과 1로 시작하며, 다음 피보나치 수는 바로 앞의 두 피보나치 수의 합이 된다. 정수 N이 주어지면, N보다 작은 모든 짝수 피보나치 수의 합을 구하여라.

예제)
Input: 12
Output: 10 // 0, 1, 2, 3, 5, 8 중 짝수인 2 + 8 = 10.

'''


def even_fibonacci_sum(n):
    fib = [0, 1]
    even_fib_sum = 0
    i = 0
    next_e = fib[i] + fib[i + 1]
    while next_e < n:
        fib.append(next_e)
        if next_e % 2 == 0:
            even_fib_sum += next_e
        i += 1
        next_e = fib[i] + fib[i + 1]
    return even_fib_sum


print(even_fibonacci_sum(int(input())))
