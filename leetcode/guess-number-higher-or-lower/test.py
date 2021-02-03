import unittest
from solution import Solution

class TestGuessNumber(unittest.TestCase):

    def test_guess(self):
        sol = Solution(6)
        self.assertEqual(sol.guess(7), -1)
        self.assertEqual(sol.guess(6), 0)
        self.assertEqual(sol.guess(5), 1)

    def test_solution(self):
        sol = Solution(6)
        self.assertEqual(sol.guessNumber(10), 6)
        sol = Solution(1)
        self.assertEqual(sol.guessNumber(1), 1)
        sol = Solution(1)
        self.assertEqual(sol.guessNumber(2), 1)
        sol = Solution(2)
        self.assertEqual(sol.guessNumber(2), 2)
        sol = Solution(1702766719)
        self.assertEqual(sol.guessNumber(2126753390), 1702766719)

if __name__ == '__main__':
    unittest.main()
