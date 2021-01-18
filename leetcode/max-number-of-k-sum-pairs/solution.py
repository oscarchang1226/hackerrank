from typing import List
import math

class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        count = 0
        freq = {}
        for i in nums:
            if i in freq:
                freq[i] += 1
            else:
                freq[i] = 1
        for j in freq:
            if (k / 2.0 == j):
                count += math.floor(freq[j] / 2.0)
            elif (k - j) in freq and freq[k - j] > 0:
                count += min(freq[j], freq[k - j])
                freq[k - j] = 0
        return count
            
