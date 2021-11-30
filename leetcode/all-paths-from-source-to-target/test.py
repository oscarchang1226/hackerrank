
import unittest
from solution import Solution

class TestAllPathsSourceTarget(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def test_sample_0(self):
        expected = []
        result = self.solution.allPathsSourceTarget([])
        self.assertEqual(result, expected)

    def test_sample_1(self):
        graph = [[1,2],[3],[3],[]]
        expected = [[0,1,3],[0,2,3]]
        result = self.solution.allPathsSourceTarget(graph)
        self.assertEqual(result, expected)

    def test_sample_2(self):
        graph = [[4,3,1],[3,2,4],[3],[4],[]]
        expected = [[0,4],[0,3,4],[0,1,3,4],[0,1,2,3,4],[0,1,4]]
        result = self.solution.allPathsSourceTarget(graph)
        self.assertEqual(result, expected)

    def test_sample_3(self):
        graph = [[1],[]]
        expected = [[0,1]]
        result = self.solution.allPathsSourceTarget(graph)
        self.assertEqual(result, expected)

    def test_sample_4(self):
        graph = [[1,2,3],[2],[3],[]]
        expected = [[0,1,2,3],[0,2,3],[0,3]]
        result = self.solution.allPathsSourceTarget(graph)
        self.assertEqual(result, expected)

    def test_sample_5(self):
        graph = [[1,3],[2],[3],[]]
        expected = [[0,1,2,3],[0,3]]
        result = self.solution.allPathsSourceTarget(graph)
        self.assertEqual(result, expected)

    def test_sample_6(self):
        graph = [[2],[],[1]]
        expected = [[0, 2]]
        result = self.solution.allPathsSourceTarget(graph)
        self.assertEqual(result, expected)



if __name__ == '__main__':
    unittest.main()