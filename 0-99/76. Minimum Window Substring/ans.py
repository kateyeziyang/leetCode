from typing import List, Optional
import heapq, math
from collections import defaultdict, deque, Counter
from bisect import bisect_left

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        m,n = len(s),len(t)
        tcounts = Counter(t)
        uniques = len(tcounts.keys())
        l = r = 0
        uniquesCounts = 0
        curCounts = defaultdict(int)
        ans = 0,m-1

        while r<m:
            while r<m and uniquesCounts != uniques:
                if s[r] in tcounts:
                    curCounts[s[r]] += 1
                    if curCounts[s[r]]==tcounts[s[r]]:
                        uniquesCounts += 1
                        if uniquesCounts == uniques:
                            break
                r += 1
            if uniquesCounts != uniques:
                break
            while uniques == uniques:
                if s[l] in tcounts:
                    if curCounts[s[l]]==tcounts[s[l]]:
                        uniquesCounts -= 1
                    curCounts[s[l]] -= 1
                    l += 1 # l-1,r is a minimum window
            if (r-l+1) < (ans[1]-ans[0]):
                ans = l,r
            r+=1
        if ans==(0,m-1) and uniquesCounts!=uniques:
            return ""
        return ans

# https://leetcode.com/problems/minimum-window-substring/solution/
# class Solution:
#     def minWindow(self, s: str, t: str) -> str:
#         if not t or not s: return ""
#         dict_t = Counter(t)
#         required = len(dict_t)

#         l,r = 0,0
#         formed = 0
#         windows_counts = {}
#         ans = float("inf"),None,None

#         while r<len(s):
#             char = s[r]
#             windows_counts[char] = windows_counts.get(char,0)+1
#             if char in dict_t and windows_counts[char]==dict_t[char]:
#                 formed += 1
#             while l <= r and formed == required:
#                 char = s[l]
#                 if r-l + 1 < ans[0]:
#                     ans = r-l+1,l,r
#                 windows_counts[char] -= 1
#                 if char in dict_t and windows_counts[char] < dict_t[char]:
#                     formed -= 1
#                 l += 1
#             r += 1
#         return "" if ans[0]==float("inf") else s[ans[1]:ans[2]+1]

s = Solution()