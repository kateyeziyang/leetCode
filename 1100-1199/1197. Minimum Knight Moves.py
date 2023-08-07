from typing import List, Optional
import heapq, math, random
from collections import defaultdict, deque, Counter
from bisect import bisect_left

class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        if y < x: x, y = y, x
        q = deque([(0,0)])
        while True:
            a,b = q.popleft()


s = Solution()