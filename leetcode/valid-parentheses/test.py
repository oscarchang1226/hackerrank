import unittest
from solution import Solution

class TestValidParentheses(unittest.TestCase):

    def test_solution(self):
        sol = Solution()
        
        self.assertTrue(sol.isValid('()'))
        self.assertTrue(sol.isValid('()[]{}'))
        self.assertTrue(sol.isValid('{[]}'))
        self.assertTrue(sol.isValid('{[()(){(())}]}'))
        self.assertTrue(sol.isValid('{{[[(()())]]}}'))

        self.assertFalse(sol.isValid('(]'))
        self.assertFalse(sol.isValid('(('))
        self.assertFalse(sol.isValid('()}}'))
        self.assertFalse(sol.isValid('(('))
        self.assertFalse(sol.isValid('([)]'))
        self.assertFalse(sol.isValid('{{[[(()[())]]}}'))

if __name__ == '__main__':
    unittest.main()
