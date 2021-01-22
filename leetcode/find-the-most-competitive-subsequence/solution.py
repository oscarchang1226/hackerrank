from typing import List

class Solution:
    def mostCompetitive(self, nums: List[int], k: int) -> List[int]:
        stack = [nums[1]]
        for i in range(1, len(nums)):
            if (k - len(stack) == i + 1):
                stack.append(nums[i])
            else:
                while len(stack) > 0 and stack[-1] > nums[i]:
                    stack.pop()
                stack.append(nums[i])
        return stack
