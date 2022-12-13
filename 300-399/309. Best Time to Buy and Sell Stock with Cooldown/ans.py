import itertools
import operator
from typing import List, Optional
import heapq, math, random
from collections import defaultdict, deque, Counter
from bisect import bisect_left

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 1: return 0
        margins = list(map(operator.sub, itertools.islice(prices,1,None), prices))
        n = len(margins)

        dp = [0]*n
        dp[0] = max(0, margins[0])
        if n == 1: return dp[-1]
        dp[1] = max(dp[0], margins[1], dp[0]+margins[1])
        if n == 2: return dp[-1]
        dp[2] = max(dp[0], dp[1], margins[3], margins[2]+margins[3], margins[1]+margins[2]+margins[3])
        for i in range(3, n):
            dp[i] = max(dp[i-3:i])
            if margins[i-1] >= 0:
                dp[i] = max(dp[i], dp[i-1] + margins[i])
            else:
                if margins[i-2] <= 0:
                    dp[i] = max(dp[i], dp[i-2] + margins[i])
                else:
                    dp[i] = max(dp[i], dp[i-3] + margins[i])
        return dp[-1]




class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0
        n = len(prices)
        prev = 0
        pprev = 0

        for i in range(n - 1):
            cur = prices[i+1]-prices[i]
            if cur > 0:
                if prev or not pprev:
                    ans += cur
                else:
                    if prices[i+1] <= prices[i-1]:
                        if cur <= pprev:
                            cur = 0
                        else:
                            ans += cur-pprev
                    else:
                        ans += max(prices[i+1]-prices[i-1], cur-pprev)
            else:
                cur = 0
            pprev, prev = prev, cur

        return ans

# 3 -1 1 3 4 0 5 7 0 11
# 0 -> 1 -> 3 (upslope)
# because 0->11 too much profit, buy at 0, sell before 1
# sell at 4 if 4-(-1) > 5-0

s = Solution()
s.maxProfit(

[2,3,5,8,3,8,2,6])