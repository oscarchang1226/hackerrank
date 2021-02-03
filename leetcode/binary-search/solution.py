from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lo = 0
        hi = len(nums) - 1
        result = -1
        while hi >= lo:
            i = lo + (hi - lo) // 2
            if nums[i] == target:
                result = i
                break
            elif nums[i] > target:
                hi = i - 1
            else:
                lo = i + 1
        return result
