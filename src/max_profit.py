import sys
from typing import List


def max_profit_multiple_trade(prices: List[int]) -> int:
    profit = 0
    for i in range(len(prices)):
        if (i + 1 < len(prices)) and (prices[i + 1] - prices[i] > 0):
            profit = profit + prices[i + 1] - prices[i]
    print(profit)


def max_profit_single_day_trade(prices: List[int]) -> int:
    # m_profit = 0
    # for i in range(len(prices)):
    #     for j in range(i, len(prices)):
    #         if prices[j] - prices[i] > 0:
    #             profit = prices[j] - prices[i]
    #             if profit > m_profit:
    #                 m_profit = profit
    # return m_profit
    min_price = sys.maxsize
    max_profit = 0
    for i in prices:
        if i < min_price:
            min_price = i
        elif i - min_price > max_profit:
            max_profit = i - min_price
    return max_profit
