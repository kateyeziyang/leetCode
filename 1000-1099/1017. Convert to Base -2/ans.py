from typing import List, Optional
import heapq, math, random
from collections import defaultdict, deque, Counter
from bisect import bisect_left

class Solution:
    def baseNeg2(self, n: int) -> str:
        if n == 0: return '0'
        ans = []
        while n:
            a, b = divmod(n, -2)
            if b<0:
                a, b = a+1, b+2
            ans.append(str(b))
            n = a
        return ''.join(ans[::-1])

s = Solution()