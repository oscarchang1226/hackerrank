import unittest
from solution import Solution

class TestSingleNumber(unittest.TestCase):

    def test_solution(self):
        sol = Solution()
        self.assertEqual(sol.singleNumber([2,2,1]), 1)
        self.assertEqual(sol.singleNumber([4,1,2,1,2]), 4)
        self.assertEqual(sol.singleNumber([1]),1)

if __name__ == '__main__':
    unittest.main()
