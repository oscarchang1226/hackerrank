import unittest
from typing import List

class Solution:
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        m = {}
        res = 0
        for a in A:
            for b in B:
                m[a + b] = m.get(a + b, 0) + 1

        for c in C:
            for d in D:
                res += m.get(-(c + d), 0)

        return res

    def kSumCount(self, lists: List[List[int]]) -> int:
        m = {}

        # This method populates the first half of lists into m
        def addToHash(lists, idx, sum):
            if idx == len(lists) // 2:
                m[sum] = m.get(sum, 0) + 1
            else:
                for a in lists[idx]:
                    addToHash(lists, idx + 1, sum + a)

        def countComplements(lists, idx, complement):
            # reach the end of the lists
            if idx == len(lists):
                return m.get(complement, 0)
            else:
                cnt = 0
                for b in lists[idx]:
                    cnt += countComplements(lists, idx + 1, complement - b)
                return cnt
        
        addToHash(lists, 0, 0)
        return countComplements(lists, len(lists) // 2, 0)
        

class Test(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_1(self):
        
        nums1 = [1, 2]        
        nums2 = [-2, -1]        
        nums3 = [-1, 2]        
        nums4 = [0, 2]
        expect = 2
        # actual = self.solution.fourSumCount(nums1, nums2, nums3, nums4)
        # self.assertEqual(expect, actual)
        actual = self.solution.kSumCount([nums1, nums2, nums3, nums4])
        self.assertEqual(expect, actual)

    def test_2(self):
        
        nums1 = [0 for i in range(200)]        
        nums2 = [0 for i in range(200)]        
        nums3 = [0 for i in range(200)]        
        nums4 = [0 for i in range(200)]
        expect = 200 * 200 * 200 * 200
        # actual = self.solution.fourSumCount(nums1, nums2, nums3, nums4)
        # self.assertEqual(expect, actual)
        actual = self.solution.kSumCount([nums1, nums2, nums3, nums4])
        self.assertEqual(expect, actual)

if __name__ == '__main__':
    unittest.main()