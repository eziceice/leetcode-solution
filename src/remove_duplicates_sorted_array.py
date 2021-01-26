from typing import List


def remove_duplicates(nums: List[int]) -> int:
    for i in range(len(nums) - 1, 0, -1):
        if nums[i] == nums[i - 1]:
            nums.pop(i)
    return len(nums)


remove_duplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4])
