import unittest
import solution

class TestSplitArray(unittest.TestCase):

    def test_solution(self):
        testCases = [
            [[7,2,5,10,8], 2, 18],
            [[1,2,3,4,5], 2, 9],
            [[1,4,4], 3, 4]]
        for i in testCases:
            result = solution.splitArray(i[0], i[1])
            self.assertEqual(result, i[2])

if __name__ == '__main__':
    unittest.main()
