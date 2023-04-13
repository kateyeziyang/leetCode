from typing import List, Optional
import heapq, math, random
from collections import defaultdict, deque, Counter
from bisect import bisect_left

class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        buy, sell = float('-inf'), 0

        for p in prices:
            buy = max(buy, sell - p)
            sell = max(sell, buy + p - fee)
        
        return sell

s = Solution()