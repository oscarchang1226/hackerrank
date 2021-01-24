from typing import List

class Solution:
    def mostCompetitive(self, nums: List[int], k: int) -> List[int]:
        stack = [nums[0]]
        availableToRemove = len(nums) - k 
        for i in range(1, len(nums)):
            while stack and stack[-1] > nums[i] and availableToRemove > 0:
                stack.pop()
                availableToRemove -= 1
            stack.append(nums[i])
        return stack[:k]
