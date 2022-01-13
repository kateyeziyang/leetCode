from typing import List, Optional
import heapq, math
from collections import defaultdict, deque,Counter
from bisect import bisect_left

# https://leetcode.com/problems/longest-duplicate-substring/solution/
class Solution:
    def search(self,L,a,MOD,n,nums):
        h=0
        for i in range(L):
            h = (h*a+nums[i])%MOD
        
        seen = defaultdict(list)
        seen[h].append(0)

        aL = pow(a,L,MOD)
        for start in range(1,n-L+1):
            h = (h*a-nums[start-1]*aL+nums[start+L-1])%MOD
            if h in seen:
                curSubstr = nums[start:start+L]
                if any(curSubstr == nums[index:index+L] for index in seen[h]):
                    return start
            seen[h].append(start)
        return -1

    def longestDupSubstring(self, s: str) -> str:
        MOD = 10**9+7
        a = 26
        n = len(s)
        nums = [ord(s[i])-ord("a") for i in range(n)]
        start = -1
        left,right = 1,n-1
        while left<=right:
            L = left+(right-left)//2
            start_of_duplicate = self.search(L,a,MOD,n,nums)
            if start_of_duplicate != -1:
                left = L+1
                start = start_of_duplicate
            else:
                right = L-1
        return s[start:start+left-1]

# edit from 1062 will TLE
# class Solution:
#     def longestDupSubstring(self, s: str) -> str:
#         n = len(s)
#         dp = [[0]*n for _ in range(n)]
#         ans = 0
#         idx = -1
#         for i in range(n-1):
#             if s[i]==s[n-1]:
#                 dp[i][n-1] = 1
#                 if dp[i][n-1] > ans:
#                     ans = max(ans,dp[i][n-1])
#                     idx = i

#         for i in range(n-2,-1,-1):
#             for j in range(n-2,i,-1):
#                 if s[i]==s[j]:
#                     dp[i][j] = 1+dp[i+1][j+1]
#                     if dp[i][j] > ans:
#                         ans = max(ans,dp[i][j])
#                         idx = i
#         return s[idx:idx+ans]

s = Solution()