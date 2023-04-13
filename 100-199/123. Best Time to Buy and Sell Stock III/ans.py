from typing import List, Optional
import heapq, math, random
from collections import defaultdict, deque, Counter
from bisect import bisect_left

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        sell0,buy1,sell1,buy2,sell2 = 0,float('-inf'),float('-inf'),float('-inf'),float('-inf')

        for p in prices:
            buy1,sell1,buy2,sell2 = max(buy1,sell0-p),max(sell1,buy1+p),max(buy2,sell1-p),max(sell2,buy2+p)
        
        return max(sell0, sell1, sell2)

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        leftProfit, rightProfit = [0] * n, [0] * n

        minPrice = prices[0]
        for i in range(1, n):
            p = prices[i]
            diff = p - minPrice
            leftProfit[i] = max(diff, leftProfit[i-1])
            minPrice = min(minPrice, p)
        maxPrice = prices[-1]
        for i in range(n-2, -1, -1):
            p = prices[i]
            diff = maxPrice - p
            rightProfit[i] = max(diff, rightProfit[i+1])
            maxPrice = max(maxPrice, p)
        
        for i in range(n):
            leftProfit[i] = leftProfit[i] + rightProfit[i]
        
        return max(leftProfit)

s = Solution()
s.maxProfit(

[2,1,2,0,1])