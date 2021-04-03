from typing import List


def two_sum(nums: List[int], target: int) -> List[int]:
    # result = {}
    # for i in range(len(nums)):
    #     if nums[i] not in result.keys():
    #         result[target - nums[i]] = i
    #     else:
    #         return [result[nums[i]], i]
    item_dict = {}
    for i in range(len(nums)):
        item_dict[nums[i]] = i

    for i in range(len(nums)):
        expect = target - nums[i]
        if expect in item_dict.keys() and item_dict[expect] != i:
            return [item_dict[expect], i]

print(two_sum([2, 7, 11 ,15], 9))