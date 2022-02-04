import unittest
import solution

class Test(unittest.TestCase):

    def test_solution(self):
        testCases = [
            [4, ['RIGHT', 'UP', 'DOWN', 'LEFT', 'DOWN', 'DOWN'], 12]]
        for i in testCases:
            result = solution.roverPosition(i[0], i[1])
            self.assertEqual(result, i[2])

if __name__ == '__main__':
    unittest.main()
