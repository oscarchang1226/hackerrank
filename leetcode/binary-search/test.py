import unittest
from solution import Solution

class TestBinarySearch(unittest.TestCase):

    def test_search(self):
        sol = Solution()
        self.assertEqual(sol.search([-1,0,3,5,9,12], 9), 4)
        self.assertEqual(sol.search([-1,0,3,5,9,12], 2), -1)


if __name__ == '__main__':
    unittest.main()
