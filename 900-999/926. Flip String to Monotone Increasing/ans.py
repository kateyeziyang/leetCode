from typing import List, Optional
import heapq, math, random
from collections import defaultdict, deque, Counter
from bisect import bisect_left

class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        binCount = Counter(s)
        curOnes,restZeros = 0,binCount["0"]
        ans = curOnes+restZeros
        for c in s:
            if c=="0":
                restZeros -= 1
                ans = min(ans,curOnes+restZeros)
            else:
                curOnes += 1
        return ans

s = Solution()