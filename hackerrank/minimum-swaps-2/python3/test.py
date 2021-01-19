import unittest
from solution import Solution

class TestMinimumSwaps(unittest.TestCase):

    def test_solution(self):
        sol = Solution()
        self.assertEqual(sol.minimumSwaps([4, 3, 1, 2]), 3)
        self.assertEqual(sol.minimumSwaps([2, 3, 4, 1, 5]), 3)
        self.assertEqual(sol.minimumSwaps([1, 3, 5, 2, 4, 6, 7]), 3)


if __name__ == '__main__':
    unittest.main()
