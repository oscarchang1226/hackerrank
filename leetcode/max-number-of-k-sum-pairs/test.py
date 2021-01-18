import unittest
from solution import Solution

class TestMaxOperations(unittest.TestCase):

    def test_solution(self):
        sol = Solution()
        self.assertEqual(sol.maxOperations([1, 2, 3, 4], 5), 2)
        self.assertEqual(sol.maxOperations([3, 1, 3, 4, 3], 6), 1)


if __name__ == '__main__':
    unittest.main()
