import unittest

class Solution:

    def myAtoi(self, s: str) -> int:
        # iterate through the s and keep track of results
        # if - is found set neg to True
        # if + is found set neg to False
        # if - is found and next is character set neg to False
        # if next is number keep track of number
        # if number exist and next is character break
        num = ''
        sign_found = False
        neg = False
        nums = '0123456789'
        for c in s:
            
            if c == ' ' and not num and not sign_found:
                continue

            elif not sign_found and c == '-' and not num:
                sign_found = True
                neg = True

            elif not sign_found and c == '+' and not num:
                sign_found = True
                neg = False

            elif c in nums:
                num = '%s%s' % (num, c)

            else:
                break


        num = int(num) if num else 0
        if neg:
            num = -num
        
        if num < -2**31:
            num = -2**31
        elif num > (2**31 - 1):
            num = 2**31 - 1
        return num

class Test(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def test_1(self):
        s = "42"
        expect = 42
        actual = self.solution.myAtoi(s)
        self.assertEqual(expect, actual)

    def test_2(self):
        s = "   -42"
        expect = -42
        actual = self.solution.myAtoi(s)
        self.assertEqual(expect, actual)

    def test_3(self):
        s = "4193 with words"
        expect = 4193
        actual = self.solution.myAtoi(s)
        self.assertEqual(expect, actual)

    def test_4(self):
        s = "00004193 with words"
        expect = 4193
        actual = self.solution.myAtoi(s)
        self.assertEqual(expect, actual)

    def test_5(self):
        2147483648
        s = "with words"
        expect = 0
        actual = self.solution.myAtoi(s)
        self.assertEqual(expect, actual) 

    def test_6(self):
        "words and 987"
        s = "2147483648234 with words"
        expect = 2147483647
        actual = self.solution.myAtoi(s)
        self.assertEqual(expect, actual)    

    def test_7(self):
        
        s = "words and 987"
        expect = 0
        actual = self.solution.myAtoi(s)
        self.assertEqual(expect, actual)

    def test_8(self):
        s = "-+987"
        expect = 0
        actual = self.solution.myAtoi(s)
        self.assertEqual(expect, actual)

    def test_9(self):
        "  +  413"
        s = "   +0 123"
        expect = 0
        actual = self.solution.myAtoi(s)
        self.assertEqual(expect, actual)     

    def test_9(self):
        s = "  +  413"
        expect = 0
        actual = self.solution.myAtoi(s)
        self.assertEqual(expect, actual)    


if __name__ == '__main__':
    unittest.main()