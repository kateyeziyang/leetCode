from typing import List, Optional
import heapq, math
from collections import defaultdict, deque, Counter
from bisect import bisect_left

class Solution:
    def arrangeCoins(self, n: int) -> int:
        k = math.floor(math.sqrt(2*n))
        while True:
            if (k**2+k)//2<=n<(k+1)*(k+2)//2:
                return k
            k += 1

s = Solution()
s.arrangeCoins(5)