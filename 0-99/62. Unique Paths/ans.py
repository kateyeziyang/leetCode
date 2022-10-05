from typing import List, Optional
import heapq, math, random
from collections import defaultdict, deque, Counter
from bisect import bisect_left

# class Solution:
#     def uniquePaths(self, m: int, n: int) -> int:
#         dp = [[0]*(n+1) for _ in range(m+1)]
#         dp[0][1] = 1
#         for i in range(1, m+1):
#             for j in range(1, n+1):
#                 dp[i][j] = dp[i-1][j] +dp[i][j-1]
#         return dp[-1][-1]

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        from math import factorial
        m,n = m-1,n-1
        # m balls, n+1 boxes, allow empty box
        return factorial(m+n)//factorial(n)//factorial(m)

s = Solution()

# 2x2 -> 2!/1!/1
# 3x2 -> 3!/1!/2!
# 2x4

# 1 0 0