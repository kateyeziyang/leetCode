from typing import List, Optional
import heapq, math, random
from collections import defaultdict, deque, Counter
from bisect import bisect_left

# dp
# 1, 1; 2, 2; 3, 2+1;
# dp[i] = dp[i-1]+dp[i-2]
class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 3: return n
        dp = [0]*(n+1)
        dp[1] = 1
        dp[2] = 2
        for i in range(3,n+1):
            dp[i] = dp[i-1]+dp[i-2]
        return dp[-1]

# n = 4, cs(3) + cs(2) = 5
# 1,1,1,1
# 2,1,1
# 1,2,1
# 1,1,2
# 2,2

s = Solution()