import unittest
from typing import List

class Trie:

    def __init__(self):
        self.children = {}
        self.group = []

class Solution:

    def __init__(self):
        self.c_vals = {c: idx for idx,c in enumerate('abcdefghijklmnopqrstuvwxyz')}
        self.trie = Trie()
        self.groups = []

    def calDist(self, prev: str, curr: str) -> int:
        dist = 0
        if curr in self.c_vals:
            if prev == 'a' and curr == 'z':
                dist = -1
            elif prev == 'z' and curr == 'a':
                dist = 1
            else:
                prev_v = self.c_vals[prev]
                curr_v = self.c_vals[curr]
                dist = curr_v - prev_v
        return dist


    def getSeq(self, s: str):
        seq = []
        prev = s[0]
        for c in s[1:]:
            seq.append(self.calDist(prev, c))
        return seq

    def insert(self, s: str):
        seq = self.getSeq(s)
        current = self.trie
        for i in seq:
            if i not in current.children:
                current.children[i] = Trie()
            current = current.children[i]
        if not current.group:
            current.group = []
            self.groups.append(current)
        current.group.append(s)
        

    '''
    We can shift a string by shifting each of its letters to its successive
    letter.

    For example, "abc" can be shifted to be "bcd".
    We can keep shifting the string to form a sequence.

    For example, we can keep shifting "abc" to form the sequence:
    "abc" -> "bcd" -> ... -> "xyz".
    Given an array of strings strings, group all strings[i] that belong to 
    the same shifting sequence. You may return the answer in any order.
    '''
    def groupStringsOld(self, strings: List[str]) -> List[List[str]]:
        # unique case is the char 'z' value to compare from prev is 25 but 
        # to the next is -1
        for s in strings:
            self.insert(s) # if new trie node created add to self.groups
        return [node.group for node in self.groups]

    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        d = {}
        for s in strings:
            k = tuple((ord(s[i + 1]) - ord(s[i])) % 26 for i in range(len(s) - 1))
            print(k)
            if k not in d:
                d[k] = []
            d[k].append(s)
        return d.values()

class Test(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()
        self.maxDiff = None

    def test_1(self):
        strings = ["abc","bcd","acef","xyz","az","ba","a","z"]
        expect = [["acef"],["a","z"],["abc","bcd","xyz"],["az","ba"]]
        actual = self.solution.groupStrings(strings)
        self.assertCountEqual(expect, actual)

    def test_2(self):
        strings = ["a"]
        expect = [["a"]]
        actual = self.solution.groupStrings(strings)
        self.assertCountEqual(expect, actual)    

    def test_3(self):
        strings = ['az', 'ba']
        expect = [['az', 'ba']]
        actual = self.solution.groupStrings(strings)
        self.assertCountEqual(expect, actual)      

    def test_4(self):
        strings = ['ab', 'ba']
        expect = [['ab'], ['ba']]
        actual = self.solution.groupStrings(strings)
        self.assertCountEqual(expect, actual) 

    def test_5(self):
        strings = ["fpbnsbrkbcyzdmmmoisaa","cpjtwqcdwbldwwrryuclcngw","a","fnuqwejouqzrif","js","qcpr","zghmdiaqmfelr","iedda","l","dgwlvcyubde","lpt","qzq","zkddvitlk","xbogegswmad","mkndeyrh","llofdjckor","lebzshcb","firomjjlidqpsdeqyn","dclpiqbypjpfafukqmjnjg","lbpabjpcmkyivbtgdwhzlxa","wmalmuanxvjtgmerohskwil","yxgkdlwtkekavapflheieb","oraxvssurmzybmnzhw","ohecvkfe","kknecibjnq","wuxnoibr","gkxpnpbfvjm","lwpphufxw","sbs","txb","ilbqahdzgij","i","zvuur","yfglchzpledkq","eqdf","nw","aiplrzejplumda","d","huoybvhibgqibbwwdzhqhslb","rbnzendwnoklpyyyauemm"]  
        expect = [["a","d","i","l"],["eqdf","qcpr"],["lpt","txb"],["yfglchzpledkq","zghmdiaqmfelr"],["kknecibjnq","llofdjckor"],["cpjtwqcdwbldwwrryuclcngw","huoybvhibgqibbwwdzhqhslb"],["lbpabjpcmkyivbtgdwhzlxa","wmalmuanxvjtgmerohskwil"],["iedda","zvuur"],["js","nw"],["lebzshcb","ohecvkfe"],["dgwlvcyubde","ilbqahdzgij"],["lwpphufxw","zkddvitlk"],["qzq","sbs"],["dclpiqbypjpfafukqmjnjg","yxgkdlwtkekavapflheieb"],["mkndeyrh","wuxnoibr"],["firomjjlidqpsdeqyn","oraxvssurmzybmnzhw"],["gkxpnpbfvjm","xbogegswmad"],["fpbnsbrkbcyzdmmmoisaa","rbnzendwnoklpyyyauemm"],["aiplrzejplumda","fnuqwejouqzrif"]]
        actual = self.solution.groupStrings(strings)
        self.assertCountEqual(expect, actual)

if __name__ == '__main__':
    unittest.main()