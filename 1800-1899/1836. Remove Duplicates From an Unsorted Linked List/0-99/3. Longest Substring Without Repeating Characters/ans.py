from typing import List, Optional
import heapq, math
from collections import defaultdict, deque
from bisect import bisect_left

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        repeatMap = defaultdict(lambda:[-1,-1])
        ans = 0
        prevDuplicate = -1
        for i,c in enumerate(s):
            left = max(prevDuplicate,repeatMap[c][0])
            ans = max(ans,i-1-left)
            if repeatMap[c][1] != -1:
                prevDuplicate = max(prevDuplicate,repeatMap[c][1])
            repeatMap[c][0],repeatMap[c][1] = [repeatMap[c][1],i]
        for l,r in repeatMap.values():
            left = max(prevDuplicate,l)
            ans = max(ans,len(s)-1-left)
            if r != -1:
                prevDuplicate = max(prevDuplicate,r)
        return ans

s = Solution()
assert s.lengthOfLongestSubstring(s = "abcabcbb")==3
assert s.lengthOfLongestSubstring(s = "bbbbb")==1
assert s.lengthOfLongestSubstring(s = "pwwkew")==3