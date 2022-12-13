from typing import List, Optional
import heapq, math, random
from collections import defaultdict, deque, Counter
from bisect import bisect_left

class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        cityCounts = defaultdict(int)
        for a,b in roads:
            cityCounts[a] += 1
            cityCounts[b] += 1
        return sum(v*i for v,i in zip(sorted(cityCounts.values(),reverse=True),range(n,n-len(cityCounts),-1)))

s = Solution()
# 4 3 2 2 1 5 4 3 2 1