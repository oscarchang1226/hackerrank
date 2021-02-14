from typing import List
import math

def final_instances(n: int, l: List[int]) -> int:
    timer = 0
    while(timer < len(l)):
        util = l[timer]
        if (util < 25 and n > 1):
            n = math.ceil(n / 2)
            timer += 10
        elif (util > 60 and (n * 2 <= 2 * 10**8)):
            n = n * 2
            timer += 10
        timer += 1
    return n
