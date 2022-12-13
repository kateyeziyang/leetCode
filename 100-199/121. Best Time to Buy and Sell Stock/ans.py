from typing import List, Optional
import heapq, math, random
from collections import defaultdict, deque, Counter
from bisect import bisect_left

# # for a day in the future, max profit = future day price - lowest previous price
# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
#         if not prices: return 0
#         minPrice = prices[0]
#         ans = float("-inf")
#         for x in prices:
#             ans = max(ans, x-minPrice)
#             minPrice = min(minPrice,x)
#         return ans if ans != float("-inf") else 0

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minPrice = prices[0]
        ans = 0
        for p in prices:
            ans = max(ans, p-minPrice)
            minPrice = min(p, minPrice)
        return ans

s = Solution()