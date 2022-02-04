
from typing import List
import math

class Solution:

    # O(n**2)
    #def maxProduct(self, nums: List[int]) -> int:
        
                
    #    if len(nums) == 1:
    #        return nums[0]
        
    #    result = nums[0]
        
    #    for i in range(len(nums)):
    #        acc = 1
    #        for j in range(i, len(nums)):
    #            acc *= nums[j]
    #            result = max(result, acc)
            


    #    return result

    def maxProduct(self, nums: List[int]) -> int:
        
        if len(nums) == 1:
            return nums[0]

        result = max_now = min_now = nums[0]
        
        for i in range(1, len(nums)):
            curr = nums[i]
            temp_max = max_now * curr
            temp_min = min_now * curr
            max_now = max(curr, temp_max, temp_min)
            min_now = min(curr, temp_max, temp_min)

            result = max(result, max_now)

        return result
