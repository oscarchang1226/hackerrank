import unittest
import solution

class TestFinalInstances(unittest.TestCase):

    def test_solution(self):
        testCases = [
            [2, [25, 23, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 76, 80], 2],
            [1, [3, 5, 10, 80], 2],
            [5, [6, 30, 5, 4, 8, 19, 89], 3],
            [2 * 10**8, [61], 2 * 10**8],
            [2 * 10**8, [61, 10], 10**8],
            [10**8, [30, 95, 4, 8, 19, 89], 2 * 10**8]]
        for i in testCases:
            result = solution.final_instances(i[0], i[1])
            self.assertEqual(result, i[2])

if __name__ == '__main__':
    unittest.main()
