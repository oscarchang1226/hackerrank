import unittest
from solution import Solution

class TestMaxArea(unittest.TestCase):

    def testSolution(self):
        sol = Solution()
        self.assertEqual(sol.maxArea([1,8, 6, 2, 5, 4, 8, 3, 7]), 49)
        self.assertEqual(sol.maxArea([1, 1]), 1)
        self.assertEqual(sol.maxArea([4, 3, 2, 1, 4]), 16)
        self.assertEqual(sol.maxArea([1, 2, 1]), 2)

if __name__ == '__main__':
    unittest.main()
