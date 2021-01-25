from typing import List


def missing_number(nums: List[int]) -> int:
    all_items = set()
    for i in range(len(nums) + 1):
        all_items.add(i)
    return list(all_items.difference(set(nums)))[0]
