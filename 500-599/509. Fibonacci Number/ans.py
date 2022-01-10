from typing import List, Optional
import heapq, math
from collections import defaultdict, deque,Counter
from bisect import bisect_left

class Solution:
    def fib(self, n: int) -> int:
        if n<2: return n
        x,y=0,1
        for i in range(2,n+1):
            x,y=y,x+y
        return y

s = Solution()