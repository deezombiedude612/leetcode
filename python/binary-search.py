from typing import *


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def bin_s(nums, target, offset=0):
            if len(nums) < 1:
                return -1

            mid = len(nums) // 2
            if nums[mid] < target:
                return bin_s(nums[mid+1:], target, offset+mid+1)
            if nums[mid] > target:
                return bin_s(nums[:mid], target, offset)
            return offset + mid

        return bin_s(nums, target)


for nums, target in (
    ([-1, 0, 3, 5, 9, 12], 9),
    ([-1, 0, 3, 5, 9, 12], 2),
):
    print(Solution().search(nums, target))
