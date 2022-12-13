from typing import List, Optional
import heapq, math, random
from collections import defaultdict, deque, Counter
from bisect import bisect_left

class Solution:
    def maximum69Number (self, num: int) -> int:
        s = str(num)

        for i,c in enumerate(s):
            if c=='6':
                return int(s[:i]+'9'+s[i+1:])
        return num

s = Solution()