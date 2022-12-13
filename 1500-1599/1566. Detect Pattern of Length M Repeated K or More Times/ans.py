from typing import List, Optional
import heapq, math, random
from collections import defaultdict, deque, Counter
from bisect import bisect_left

class Solution:
    def containsPattern(self, arr: List[int], m: int, k: int) -> bool:
        c = 0

        for i,x in enumerate(arr):
            if (i+m)<len(arr) and x==arr[i+m]:
                c += 1
                if c == (k-1)*m: return True
            else:
                c = 0
        return False



s = Solution()
s.containsPattern(arr = [1,2,4,4,4,4], m = 1, k = 3)