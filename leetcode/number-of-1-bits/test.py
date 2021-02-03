import unittest
from solution import Solution

class TestHammingWeight(unittest.TestCase):

    def test_solution(self):
        sol = Solution()
        self.assertEqual(sol.hammingWeight(11), 3)
        self.assertEqual(sol.hammingWeight(128), 1)
        self.assertEqual(sol.hammingWeight(4294967293), 31)

if __name__ == '__main__':
    unittest.main()
