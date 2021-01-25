from typing import List


def contains_duplicate(nums: List[int]) -> bool:
    # return len(nums) == len(set(nums))
    items = {}
    for num in nums:
        if num in items.keys():
            return True
        else:
            items[num] = 1
    return False
