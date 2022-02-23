from typing import List, Optional
import heapq, math, random
from collections import defaultdict, deque, Counter
from bisect import bisect_left

class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        if k==1: return 1
        sq = math.floor(n**0.5)
        cur = 1
        for i in range(2,sq+1):
            if n%i==0:
                cur += 1
                if cur == k:
                    return i
        start = sq-1 if sq**2==n else sq
        for i in range(start,0,-1):
            if n%i==0:
                cur += 1
                if cur == k:
                    return n//i
        return -1


# brute force
class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        if k==1: return 1
        cur = 2
        curi = 1
        while cur <= n:
            if n%cur==0:
                curi += 1
                if curi == k:
                    return cur
            cur += 1
        return -1

s = Solution()