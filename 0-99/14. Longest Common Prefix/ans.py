from typing import List, Optional
import heapq, math
from collections import defaultdict, deque
from bisect import bisect_left

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        pref = strs[0]
        for i in range(1,len(strs)):
            count = 0
            for a,b in zip(pref,strs[i]):
                if a==b:
                    count += 1
                else:
                    break
            pref = pref[:count]
        return pref

s = Solution()
assert s.longestCommonPrefix(["flower","flow","flight"])=="fl"
assert s.longestCommonPrefix(["ab","a"])=="a"