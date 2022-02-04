import unittest
import solution

class TestMinimumContainerSize(unittest.TestCase):

    def test_solution(self):
        testCases = [
            [[10, 2, 20, 5, 15, 10, 1], 3, 31],
            [[10, 2, 20, 5, 15, 10, 1], 5, 43],
            [[5, 4, 2, 4, 3, 4, 5, 4], 4, 16],
            [[22, 12, 1, 14, 17], 2, 39]]
        for i in testCases:
            result = solution.minimumContainerSize(i[0], i[1])
            self.assertEqual(result, i[2])

if __name__ == '__main__':
    unittest.main()
