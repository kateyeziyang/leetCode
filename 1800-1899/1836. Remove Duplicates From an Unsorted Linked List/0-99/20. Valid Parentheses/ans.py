from typing import List, Optional
import heapq, math
from collections import defaultdict, deque
from bisect import bisect_left

class Solution:
    def isValid(self, s: str) -> bool:
        st = deque()
        corrBrackets = {")":"(","]":"[","}":"{"}
        leftBrackets = {"(","[","{"}
        for c in s:
            if c in leftBrackets:
                st.append(c)
                continue
            if not st or st[-1]!=corrBrackets[c]:
                return False
            st.pop()
        return True if not st else False

s = Solution()