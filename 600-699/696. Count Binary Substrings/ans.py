from typing import List, Optional
import heapq, math
from collections import defaultdict, deque
from bisect import bisect_left

class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        if len(s) < 2: return 0
        startl = 0
        startr = -1
        ans = 0
        for i in range(1,len(s)):
            c = s[i]
            if s[startl]==c:
                if startr != -1:
                    ans += min(i-startr,startr-startl)
                    startl,startr = startr,i
            else:
                if startr == -1:
                    startr = i
        ans += max(0,min(len(s)-startr,startr-startl))
        return ans


s = Solution()
assert s.countBinarySubstrings("00110011")==6
assert s.countBinarySubstrings(s = "10101")==4
assert s.countBinarySubstrings("000")==0