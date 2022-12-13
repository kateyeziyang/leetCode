from typing import List, Optional
import heapq, math, random
from collections import defaultdict, deque, Counter
from bisect import bisect_left

class Solution:
    def numberOfSteps(self, num: int) -> int:
        s = bin(num)[2:]
        return s.count('1')-1+len(s)

s = Solution()