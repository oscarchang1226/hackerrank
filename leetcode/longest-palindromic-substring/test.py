import unittest
from solution import Solution

class TestLongestPalindrome(unittest.TestCase):

    def test_isPalindrome(self):
        sol = Solution()
        self.assertTrue(sol.isPalindrome('aba'))
        self.assertTrue(sol.isPalindrome('bb'))
        self.assertTrue(sol.isPalindrome('a'))
        
        self.assertFalse(sol.isPalindrome('bbaa'))
        self.assertFalse(sol.isPalindrome('ca'))
        self.assertFalse(sol.isPalindrome('caa'))
        self.assertFalse(sol.isPalindrome('cca'))

    def test_solution(self):
        sol = Solution()
        self.assertEqual(sol.longestPalindrome('babad'), 'bab')
        self.assertEqual(sol.longestPalindrome('cbbd'), 'bb')
        self.assertEqual(sol.longestPalindrome('a'), 'a')
        self.assertEqual(sol.longestPalindrome('ac'), 'a')
        self.assertEqual(sol.longestPalindrome('aa'), 'aa')
        self.assertEqual(sol.longestPalindrome('aaaa'), 'aaaa')
        self.assertEqual(sol.longestPalindrome('bbaaa'), 'aaa')
        self.assertEqual(sol.longestPalindrome('aaabb'), 'aaa')
        self.assertEqual(sol.longestPalindrome('aabab'), 'aba')
        self.assertEqual(sol.longestPalindrome('abb'), 'bb')

if __name__ == '__main__':
    unittest.main()
