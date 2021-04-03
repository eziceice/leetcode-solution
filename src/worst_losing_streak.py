#!/bin/python3


def worst_losing_streak(nums):
    max_price = 0
    max_lost = 0
    for i in nums:
        if i > max_price:
            max_price = i
        elif max_price - i > max_lost:
            max_lost = max_price - i
    return max_lost


print(worst_losing_streak([7, 4, 2, 9]))
