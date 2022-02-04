import unittest
from typing import List

class Solution:
    def findAnagramsOld(self, s: str, p: str) -> List:
        res = []
        freq = {}
        seen = {}
        for c in p:
            freq[c] = freq.get(c, 0) + 1

        for i in range(len(s) - len(p) + 1):
            freq_copy = freq.copy()
            word = s[i:(i + len(p))]
            if word in seen:
                is_anagram = seen[word]

            else:
                is_anagram = True
                for w in word:
                    if w not in freq_copy or freq_copy[w] == 0:
                        is_anagram = False
                        break
                    freq_copy[w] -= 1
                seen[word] = is_anagram
            if is_anagram:
                res.append(i)
        return res

    def findAnagrams(self, s: str, p: str) -> List:
        res = []
        # TODO
        return res


class Test(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def test_1(self):
        s = 'cbaebabacd'
        p = 'abc'
        expect = [0, 6]
        actual = self.solution.findAnagrams(s, p)
        self.assertCountEqual(expect, actual)

    def test_2(self):
        s = 'abab'
        p = 'ab'
        expect = [0, 1, 2]
        actual = self.solution.findAnagrams(s, p)
        self.assertCountEqual(expect, actual)

    def test_3(self):
        s = ''
        p = 'ab'
        expect = []
        actual = self.solution.findAnagrams(s, p)
        self.assertCountEqual(expect, actual)

    def test_4(self):
        s = 'a' * (3 * 10**4)
        p = 'a'
        expect = [i for i in range(3 * 10**4)]
        actual = self.solution.findAnagrams(s, p)
        self.assertCountEqual(expect, actual)    

if __name__ == '__main__':
    unittest.main()