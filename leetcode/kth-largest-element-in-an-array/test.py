import unittest
from solution import Solution

class TestFindKthLargest(unittest.TestCase):

    def test_solution(self):
        sol = Solution()
        self.assertEqual(sol.findKthLargest([3,2,1,5,6,4], 2), 5)
        self.assertEqual(sol.findKthLargest([3,2,3,1,2,4,5,5,6], 4), 4)


if __name__ == '__main__':
    unittest.main()
