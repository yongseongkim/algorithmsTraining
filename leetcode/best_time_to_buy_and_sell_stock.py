# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

import sys

total_case = int(input())
case_index = 0


def best_time_to_buy_and_sell_stock(prices):
    if len(prices) < 2:
        return 0
    result = 0
    mn_price = prices[0]
    for idx in range(1, len(prices)):
        price = prices[idx]
        mn_price = min(price, mn_price)
        result = max(result, price - mn_price)
    return result


while case_index < total_case:
    # do something
    prices = [int(x) for x in input().split(',')]1
    print(best_time_to_buy_and_sell_stock(prices))
    case_index += 1
