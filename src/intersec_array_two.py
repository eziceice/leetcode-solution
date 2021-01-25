import collections
from typing import List


def intersect(nums1: List[int], nums2: List[int]) -> List[int]:
    nums1_dict = collections.Counter(nums1)
    result = []

    for i in nums2:
        if i in nums1_dict.keys():
            if nums1_dict[i] > 0:
                result.append(i)
                nums1_dict[i] = nums1_dict[i] - 1

    return result


print(intersect([4,9,5], [9,4,9,8,4]))