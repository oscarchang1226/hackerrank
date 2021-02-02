import unittest
from solution import ListNode
from solution import Solution

class TestMergeKLists(unittest.TestCase):

    def test_solution(self):
        sol = Solution();
        l = [
            ListNode(1, ListNode(4, ListNode(5))),
            ListNode(1, ListNode(3, ListNode(4))),
            ListNode(2, ListNode(6))]
        self.assertEqual(sol.mergeKLists(l).toArray(), [1, 1, 2, 3, 4, 4, 5, 6])
        self.assertEqual(sol.mergeKLists([]), None)
        self.assertEqual(sol.mergeKLists([None]), None)
        l = [None, ListNode(1)]
        self.assertEqual(sol.mergeKLists(l).toArray(), [1])

if __name__ == '__main__':
    unittest.main()
