from typing import List, Optional
import heapq, math
from collections import defaultdict, deque,Counter
from bisect import bisect_left

# dp[i][i] length of repeating string start at s[i],s[j]
class Solution:
    def longestRepeatingSubstring(self, s: str) -> int:
        n = len(s)
        dp = [[0]*n for _ in range(n)]
        ans = 0
        for i in range(n-1):
            if s[i]==s[n-1]:
                dp[i][n-1] = 1

        for i in range(n-2,-1,-1):
            for j in range(n-2,i,-1):
                if s[i]==s[j]:
                    dp[i][j] = 1+dp[i+1][j+1]
                    ans = max(ans,dp[i][j])
        return ans

s = Solution()
print(s.longestRepeatingSubstring("abbaba"))
print(s.longestRepeatingSubstring(s = "aabcaabdaab"))