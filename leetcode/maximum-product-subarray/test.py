import unittest
from solution import Solution

class MaximumProductSubarrayTest(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def test_case_1(self):
        input = [2,3,-2,4]
        expected = 6
        result = self.solution.maxProduct(input)
        self.assertEqual(result, expected)

    def test_case_2(self):
        input = [-2,0,-1]
        expected = 0
        result = self.solution.maxProduct(input)
        self.assertEqual(result, expected)

    def test_case_3(self):
        input = [-2]
        expected = -2
        result = self.solution.maxProduct(input)
        self.assertEqual(result, expected)

    def test_case_4(self):
        input = [-3, -4]
        expected = 12
        result = self.solution.maxProduct(input)
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()