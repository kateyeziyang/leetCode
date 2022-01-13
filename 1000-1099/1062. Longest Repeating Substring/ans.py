from typing import List, Optional
import heapq, math
from collections import defaultdict, deque,Counter
from bisect import bisect_left

# https://leetcode.com/problems/longest-repeating-substring/discuss/429950/Python-DP-solution-with-explanations-and-follow-up
# class Solution:
#     def longestRepeatingSubstring(self,S: str) -> int:
#         if not S:
#             return 0
#         n = len(S)
#         dp = [[0 for j in range(n + 1)] for i in range(n + 1)]
#         res = 0
#         for i in range(1, n+1):
#                 for j in range(i+1, n+1):
#                     dp[i][j] = dp[i-1][j-1] + 1 if S[i-1] == S[j-1] else 0
#                     res = max(res, dp[i][j])
#         return res

# dp[i][i] length of repeating string start at s[i],s[j]
# wrong but accepted
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
# print(s.longestRepeatingSubstring("abbaba"))
# print(s.longestRepeatingSubstring(s = "aabcaabdaab"))
print(s.longestRepeatingSubstring("aa"))