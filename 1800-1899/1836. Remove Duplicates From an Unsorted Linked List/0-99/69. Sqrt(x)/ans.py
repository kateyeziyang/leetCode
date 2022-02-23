from typing import List, Optional
import heapq, math, random
from collections import defaultdict, deque, Counter
from bisect import bisect_left

class Solution:
    def mySqrt(self, x: int) -> int:
        if x<2:return x
        l,r = 1,x//2
        while l<=r:
            mid = (l+r)//2
            if mid**2<=x and (mid+1)**2>x:
                return mid
            if mid**2<x:
                l=mid+1
            else:
                r=mid-1

s = Solution()
print(s.mySqrt(9))