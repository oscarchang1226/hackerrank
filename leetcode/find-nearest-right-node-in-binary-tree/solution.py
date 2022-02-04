from bdb import Breakpoint
from lib2to3.pytree import Node
from typing import Optional
import unittest
from o_tools.node import Node as TreeNode

'''
Given the root of a binary tree and a node u in the tree, return the nearest 
node on the same level that is to the right of u, or return null if u is the 
rightmost node in its level.
'''

class Solution:

    def findNearestRightNode(self, root: TreeNode, u: TreeNode) -> Optional[TreeNode]:
        stack = [root]
        children = []
        while stack or children:
            if not children:
                for parent in stack:   
                    if parent:   
                        children.append(parent.left)  
                        children.append(parent.right)
                stack = children.copy()

            found = False
            for child in children:
                if child == u:
                    found = True
                elif child and found:
                    return child
            children = []
            if found:
                return TreeNode(None)


class Test(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def test_1(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.left.right = u = TreeNode(4)
        root.right = TreeNode(3)
        root.right.left = TreeNode(5)
        root.right.right = TreeNode(6)
        expect = 5
        actual = self.solution.findNearestRightNode(root, u)
        self.assertEqual(expect, actual.val)

    def test_2(self):
        root = TreeNode(3)
        root.right = TreeNode(4)
        root.right.left = u = TreeNode(2)
        expect = None
        actual = self.solution.findNearestRightNode(root, u)
        self.assertEqual(expect, actual.val)

if __name__ == '__main__':
    unittest.main()
