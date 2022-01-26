from typing import List, Optional
import heapq, math, random
from collections import defaultdict, deque, Counter
from bisect import bisect_left

# hash table or slow and quick pointer
class Solution:
    def isHappy(self, n: int) -> bool:
        def nextNumber(x):
            count = 0
            while x:
                count += (x%10)**2
                x //= 10
            return count
        slow = nextNumber(n)
        quick = nextNumber(slow)
        while slow != quick:
            slow = nextNumber(slow)
            quick = nextNumber(nextNumber(quick))
        return slow==1

s = Solution()
print(s.isHappy(68))