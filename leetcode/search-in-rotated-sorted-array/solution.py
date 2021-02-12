from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        pivot = None
        result = -1
        lo = None
        hi = None
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                if target <= nums[i]:   
                pivot = i + 1
                break
        return pivot
