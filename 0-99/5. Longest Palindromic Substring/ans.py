import enum
from typing import List, Optional
import heapq, math, random
from collections import defaultdict, deque, Counter
from bisect import bisect_left

# guess each char is the center of palindrome
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s)<2: return s
        def getPalindrome(i):
            nonlocal ans
            l = r = i
            while l-1>=0 and r+1<n and s[l-1]==s[r+1]:
                l -= 1
                r += 1
            if r-l+1>len(ans):
                ans = s[l:r+1]
        def getPalindrome2(i):
            nonlocal ans
            l,r = i,i+1
            if s[l]==s[r]:
                while l-1>=0 and r+1<n and s[l-1]==s[r+1]:
                    l -= 1
                    r += 1
                if r-l+1>len(ans):
                    ans = s[l:r+1]
        n = len(s)
        ans = ""
        for i in range(n-1):
            getPalindrome(i)
            getPalindrome2(i)
        getPalindrome(n-1)
        return ans

# dynamic programming O(n^2)
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s)<2: return s
        n = len(s)
        dp = [[False]*n for _ in range(n)]
        for i in range(n):
            dp[i][i] = True
        ans = s[0]
        for i in range(n):
            for j in range(i):
                if i-j>1:
                    if dp[j+1][i-1] and s[i]==s[j]:
                        dp[j][i] = True
                        if len(ans)<i-j+1:
                            ans = s[j:i+1]
                else:
                    if s[i]==s[j]:
                        dp[j][i] = True
                        if len(ans)<i-j+1:
                            ans = s[j:i+1]
        return ans
# brute force O(n^3)
# class Solution:
#     def longestPalindrome(self, s: str) -> str:
#         ans = ""
#         for i in range(len(s)):
#             for j in range(i+1):
#                 if (i-j+1)>len(ans) and s[j:i+1]==s[j:i+1][::-1]:
#                     ans = s[j:i+1]
#         return ans
# class Solution:
#     def longestPalindrome(self, s: str) -> str:
        
s = Solution()
print(s.longestPalindrome("aaaa"))