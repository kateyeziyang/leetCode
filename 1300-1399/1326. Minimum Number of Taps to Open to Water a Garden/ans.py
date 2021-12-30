from typing import List
import heapq, math
from collections import defaultdict, deque

class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        jump = [0]*(n+1)
        for i,r in enumerate(ranges):
            right = min(n,i+r)
            jump[max(0,i-r)] = max(jump[max(0,i-r)],right)
        count = start = end = 0
        while start <= end:
            if end == n:
                return count
            start, end = end+1, max(jump[start:end+1])
            count += 1
        if end == n:
            return count
        return -1
"""

5
[3,4,1,1,0,0]

s,e = 0,0
s,e = 1,5
s,e = 6,
"""

s = Solution()
s.minTaps(5,[3,4,1,1,0,0])