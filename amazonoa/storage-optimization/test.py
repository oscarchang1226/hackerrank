import unittest
import solution

class Test(unittest.TestCase):

    def test_solution(self):
        testCases = [
            [6, 6, [4], [2], 4],
            [3, 3, [2], [2], 4],
            [3, 2, [1, 2, 3], [1, 2], 4],]
        for i in testCases:
            result = solution.storageOptimization(i[0], i[1], i[2], i[3])
            self.assertEqual(result, i[4])

if __name__ == '__main__':
    unittest.main()
