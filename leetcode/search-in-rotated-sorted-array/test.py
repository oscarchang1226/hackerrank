import unittest
from solution import Solution

class TestSearch(unittest.TestCase):

    def test_solution(self):
        sol = Solution()
        self.assertEqual(sol.search([4,5,6,7,0,1,2], 0), 4)
        self.assertEqual(sol.search([4,5,6,7,0,1,2], 3), -1)
        self.assertEqual(sol.search([1], 0), -1)

if __name__ == '__main__':
    unittest.main()
