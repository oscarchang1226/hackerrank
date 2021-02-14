import unittest
import solution

class TestCountLevelUpPlayers(unittest.TestCase):

    def test_solution(self):
        testCases = [
            [3, 4, [100, 50, 50, 25], 3],
            [4, 5, [2, 2, 3, 4, 5], 5],
            [0, 5, [2, 2, 2, 2, 2], 0],
            [5, 10**5, [0 for i in range(10**5)], 0],
            [5, 10**5, [1 for i in range(10**5)], 10**5],
            [1, 10**5, [1 for i in range(10**5 - 1)] + [2], 1],
            [1, 10**5, [1 for i in range(10**5 - 1)] + [0], 10**5 - 1]]
        for i in testCases:
            result = solution.count_level_up_players(i[0], i[1], i[2])
            self.assertEqual(result, i[3])

if __name__ == '__main__':
    unittest.main()
