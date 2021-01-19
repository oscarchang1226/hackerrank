import math

class Solution:
    def longestPalindrome(self, s: str) -> str:
        palindrome = s if self.isPalindrome(s) else None
        n = len(s) - 1
        #print()
        #print('--- %s ---' % (s))
        while palindrome is None:
            if n == 1:
                palindrome = s[0]
            else:
                for i in range(len(s) - n + 1):
                    end = i + n
                    substring = s[i : end]
                    #print('%d. %s' %(i, substring))
                    if self.isPalindrome(substring):
                        palindrome = substring
                        break
            n -= 1
        return palindrome
            

    def isPalindrome(self, s: str) -> bool:
        return s == s[::-1]
'''
let n be the length of s
while not found
    iterate through s while extract substring with length of n
        if substring is palindrome
            set substring to found
            break
        else
            continue

5 5 1
5 4 2
5 3 3
5 2 4
5 1
'''
