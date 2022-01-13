from typing import List, Optional
import heapq, math
from collections import defaultdict, deque,Counter
from bisect import bisect_left

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m,n = len(s),len(p)
        dp = [[False]*(n+1) for _ in range(m+1)]
        dp[0][0] = True
        for j in range(1,n+1):
            if p[j-1] != "*": break
            dp[0][j]=True

        for j in range(1,n+1):
            for i in range(1,m+1):
                if (dp[i-1][j-1] and p[j-1] in [s[i-1],"?"]):
                    dp[i][j] = True
                elif p[j-1]=="*":
                    dp[i][j] = dp[i][j-1]
                    dp[i][j] |= dp[i-1][j]
        return dp[-1][-1]

s = Solution()
# s.isMatch("aa","a")
s.isMatch("abcabczzzde","*abc???de*")