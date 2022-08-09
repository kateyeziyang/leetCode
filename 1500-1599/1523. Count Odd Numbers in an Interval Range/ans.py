from typing import List, Optional
import heapq, math, random
from collections import defaultdict, deque, Counter
from bisect import bisect_left

class Solution:
    def countOdds(self, low: int, high: int) -> int:
        if low % 2 != 1:
            low += 1
        if high % 2 != 1:
            high -= 1
        return (high-low)//2+1

s = Solution()