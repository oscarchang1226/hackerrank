import unittest
from solution import Solution

class TestCountVowelStrings(unittest.TestCase):

    def test_solution(self):
        sol = Solution()
        self.assertEqual(sol.countVowelStrings(1), 5)
        self.assertEqual(sol.countVowelStrings(2), 15)
        self.assertEqual(sol.countVowelStrings(33), 66045)


if __name__ == '__main__':
    unittest.main()
