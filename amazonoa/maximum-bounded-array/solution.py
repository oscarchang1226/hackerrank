from typing import List
import math

def isValid(n: int, lo: int, up: int, mid: int) -> bool:
    return False

def maximumBoundedArray(n: int, lo: int, up: int) -> List:
    result = None
    mid = n // 2 if n % 2 > 0 else n // 2 - 1
    options = up - lo
    leftSize = options if n % 2 > 0 else options - 1
    maxN = options * 2 + 1
    if (n <= maxN):
        leftSide = [i for i in range(up - leftSize, up)]
        rightSide = [j for j in range(up - 1, up - options - 1, -1)]
        result = leftSide + [up] + rightSide
    return result
