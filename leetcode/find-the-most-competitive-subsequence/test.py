import unittest
from solution import Solution

class TestMostCompetitive(unittest.TestCase):

    def test_solution(self):
        sol = Solution();
        self.assertEqual(sol.mostCompetitive([3, 5, 2, 6], 2), [2, 6])
        self.assertEqual(sol.mostCompetitive([2, 4, 3, 3, 5, 4, 9, 6], 4), [2, 3, 3, 4])
        self.assertEqual(sol.mostCompetitive([3, 5, 2, 6], 4), [3, 5, 2, 6])
        self.assertEqual(sol.mostCompetitive([3, 5, 2, 6], 3), [3, 2, 6])
        
        nums = [0 for i in range(10**5)]
        k = 50000
        self.assertEqual(sol.mostCompetitive(nums, k), nums[:k])
        nums = [10**9 for i in range(10**5)]
        k = 50000
        self.assertEqual(sol.mostCompetitive(nums, k), nums[:k])
##        nums = [10**9 for i in range(10**5)] + [1]
##        k = 50000
##        self.assertEqual(sol.mostCompetitive(nums, k), nums[:k - 1] + [1])

if __name__ == '__main__':
    unittest.main()
