class Solution:

    def __init__(self, i: int):
        self.num = i

    def guess(self, n: int):
        if self.num == n:
            return 0
        return 1 if self.num > n else -1
    
    def guessNumber(self, n: int) -> int:
        # print()
        # print(n)
        i = self.guess(n)
        lo = 1
        hi = n
        count = 10
        while hi > lo:
            if hi - lo == 1:
                # print(hi, lo)
                if self.guess(hi) == 0:
                    return hi
                else:
                    return lo
            n = lo + (hi - lo) // 2
            i = self.guess(n)
            # print('lo: %d, hi: %d, n: %d, i: %d' %(lo, hi, n, i))
            if i > 0:
                lo = n
            elif i < 0:
                hi = n
            else:
                return n
        return n
