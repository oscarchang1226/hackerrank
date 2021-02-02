from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nums.sort()
        i = None
        while len(nums) > 0:
            j = nums.pop()
            print(i, j)
            if i is None:
                i = j
            elif i == j:
                i = None
            else:
                break
        return i        
