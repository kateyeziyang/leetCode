from typing import List, Optional
import heapq, math
from collections import defaultdict, deque, Counter
from bisect import bisect_left

# https://leetcode.com/problems/minimum-window-substring/solution/
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s: return ""
        dict_t = Counter(t)
        required = len(dict_t)

        l,r = 0,0
        formed = 0
        windows_counts = {}
        ans = float("inf"),None,None

        while r<len(s):
            char = s[r]
            windows_counts[char] = windows_counts.get(char,0)+1
            if char in dict_t and windows_counts[char]==dict_t[char]:
                formed += 1
            while l <= r and formed == required:
                char = s[l]
                if r-l + 1 < ans[0]:
                    ans = r-l+1,l,r
                windows_counts[char] -= 1
                if char in dict_t and windows_counts[char] < dict_t[char]:
                    formed -= 1
                l += 1
            r += 1
        return "" if ans[0]==float("inf") else s[ans[1]:ans[2]+1]

s = Solution()