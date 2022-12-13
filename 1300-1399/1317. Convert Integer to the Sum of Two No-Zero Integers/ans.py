from typing import List, Optional
import heapq, math, random
from collections import defaultdict, deque, Counter
from bisect import bisect_left

class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        i = 1
        while True:
            if '0' not in str(i)+str(n-i): return [i,n-i]
            i+=1

s = Solution()