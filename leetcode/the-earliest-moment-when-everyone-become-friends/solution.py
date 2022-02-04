import unittest
from typing import List

class Solution:
    def earliestAcq(self, logs: List[List[int]], n: int) -> int:
        logs.sort(key = lambda x: x[0])
        acq = [{} for i in range(n)]
        all_acq = n * (n - 1)
        cur_acq = 0
        for log in logs:
            t = log[0]
            a1 = log[1]
            a2 = log[2]

            # Are friends already?
            if acq[a1].get(a2, 0) == 0:
                acq[a1][a2] = 1
                cur_acq += 1

            if acq[a2].get(a1, 0) == 0:
                acq[a2][a1] = 1
                cur_acq += 1


            # Get friends with acq[ax].keys()
            # if it is a new acq cur += 1
            for i in acq[a2].keys():
                if i == a1:
                    continue
                if i not in acq[a1]:
                    acq[a1][i] = 1
                    cur_acq += 1

            for j in acq[a1].keys():
                if j == a2:
                    continue
                if j not in acq[a2]:
                    acq[a2][j] = 1
                    cur_acq += 1

            print(t, acq, cur_acq, all_acq)
            if cur_acq == all_acq:
                return t
        return 0

class Test(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def test_1(self):
        logs = [[20190101,0,1],[20190104,3,4],[20190107,2,3],[20190211,1,5],[20190224,2,4],[20190301,0,3],[20190312,1,2],[20190322,4,5]]
        n = 6
        expect = 20190301
        actual = self.solution.earliestAcq(logs, n)
        self.assertEqual(expect, actual)


if __name__ == '__main__':
    unittest.main()
