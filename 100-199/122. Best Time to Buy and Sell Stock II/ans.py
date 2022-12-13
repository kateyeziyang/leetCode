from typing import List, Optional
import heapq, math, random
from collections import defaultdict, deque, Counter
from bisect import bisect_left
import operator, itertools

# (7,1),(1,5)
# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
#         if len(prices) <= 1: return 0
#         n = len(prices)
#         ans = 0
#         for i in range(n-1):
#             ans += max(0,prices[i+1]-prices[i])
#         return ans

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # ans = 0
        return sum(max(0,x) for x in map(operator.sub, itertools.islice(prices,1,None), prices))

        for i in range(len(prices)-1):
            ans += max(0, prices[i+1]-prices[i])
"""
[3,0,1,4,5,2]
ans = 0,1,4, 5,

time O(n)
space O(1)
"""

s = Solution()