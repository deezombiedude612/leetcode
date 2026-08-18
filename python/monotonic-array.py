from typing import *


class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        # if all same element, return True (can be either monotonic increasing or monotonic decreasing)
        if len(set(nums)) == 1:
            return True

        is_asc, is_desc = False, False
        i = 0

        # find out if trend is ascending or descending
        while not is_asc and not is_desc and i < len(nums)-1:
            diff = nums[i+1] - nums[i]
            if diff > 0:
                is_asc = True
            elif diff < 0:
                is_desc = True
            i += 1

        # if any deviation from earlier trend in later elements, return False
        for i in range(i, len(nums)-1):
            if is_asc:
                diff = nums[i+1] - nums[i]
                if diff < 0:
                    return False
            elif is_desc:
                diff = nums[i+1] - nums[i]
                if diff > 0:
                    return False

        return True


for L in (
    [1, 2, 2, 3],
    [6, 5, 4, 4],
    [1, 3, 2],

    [2, 2, 2, 1, 4, 5],
):
    print(Solution().isMonotonic(L))
