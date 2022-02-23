from typing import List, Optional
import heapq, math
from collections import defaultdict, deque
from bisect import bisect_left

class Solution:
    def reverse(self, x: int) -> int:
        sign = 1 if x>0 else -1
        if sign==-1:
            x = -x
        newx = 0
        while x:
            newx *= 10
            newx += x % 10
            x //= 10
        newx *=sign
        if -2**31<=newx<=2**31-1:
            return newx
        return 0

s = Solution()
print(s.reverse(-123))
print(s.reverse(120))