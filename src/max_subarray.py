from typing import List


def max_sub_array(nums: List[int]) -> int:
    # t_max = nums[0]
    # for i in range(len(nums)):
    #     pre_total = nums[i]
    #     cur_max = nums[i]
    #     if i + 1 < len(nums):
    #         for j in range(i + 1, len(nums)):
    #             pre_total = pre_total + nums[j]
    #             if pre_total > cur_max:
    #                 cur_max = pre_total
    #     if cur_max > t_max:
    #         t_max = cur_max
    # return t_max
    c_total = nums[0]
    t_max = c_total
    for i in range(1, len(nums)):
        if nums[i] > c_total + nums[i]:
            c_total = nums[i]
        else:
            c_total = c_total + nums[i]
        if c_total > t_max:
            t_max = c_total
    return t_max


print(max_sub_array([-2,1,-3,4,-1,2,1,-5,4]))