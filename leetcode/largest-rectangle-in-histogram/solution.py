import unittest
from typing import List

class Solution:
    '''
    Given an array of integers heights representing the histogram's bar 
    height where the width of each bar is 1, return the area of the 
    largest rectangle in the histogram.
    '''
    def largestRectangleAreaTest(self, heights: List[int]) -> int:
        a = 0
        for i in range(len(heights)):
            for j in range(i, len(heights)):
                temp = heights[i: (j+1)]
                min_h = min(temp)
                w = len(temp)
                a = max(a, min_h * w)
                print(temp, a)
            
        return a

    def largestRectangleArea(self, heights: List[int]) -> int:
        a = 0
        min_h = 0
        cur_h = 0
        max_w = 0
        cur_w = 0
        for h in heights:
            if h:
                if min_h == 0:
                    min_h = h
                else:
                    min_h = min(h, min_h)

                if cur_h == 0:
                    cur_h = h
                elif h > cur_h:
                    cur_w = 1
                    cur_h = h
                    

                max_w += 1
                cur_w += 1

                continue
            else:
                min_h = 0
                cur_h = 0
                max_w = 0
                cur_w = 0


class Test(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def test_1(self):
        heights = [2,1,5,6,2,3]
        expect = 10
        actual = self.solution.largestRectangleArea(heights)
        self.assertEqual(expect, actual)

    def test_2(self):
        heights = [2, 4]
        expect = 4
        actual = self.solution.largestRectangleArea(heights)
        self.assertEqual(expect, actual)

    def test_3(self):
        heights = [1 for i in range(100000)]
        expect = 100000
        actual = self.solution.largestRectangleArea(heights)
        self.assertEqual(expect, actual)

if __name__ == '__main__':
    unittest.main()