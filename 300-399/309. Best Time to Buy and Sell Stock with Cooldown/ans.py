import itertools
import operator
from typing import List, Optional
import heapq, math, random
from collections import defaultdict, deque, Counter
from bisect import bisect_left


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # float('-inf') means unreachable
        reset = 0 # go to buy, or stay reset
        sell = float('-inf') # go to reset
        buy = float('-inf') # go to reset, or stay at buy

        for p in prices:
            reset = max(reset, sell)
            sell = buy + p
            buy = max(buy, reset - p)
        
        return max(reset, sell)

# 3 -1 1 3 4 0 5 7 0 11
# 0 -> 1 -> 3 (upslope)
# because 0->11 too much profit, buy at 0, sell before 1
# sell at 4 if 4-(-1) > 5-0

s = Solution()
s.maxProfit(

[2,3,5,8,3,8,2,6])