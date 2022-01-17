from typing import List, Optional
import heapq, math, random
from collections import defaultdict, deque, Counter
from bisect import bisect_left

class Solution:
    def removeDuplicates(self, s: str) -> str:
        st = deque()
        for c in s:
            if not st or st[-1]!=c:
                st.append(c)
                continue
            while st and st[-1]==c:
                st.pop()
        return "".join(st)

s = Solution()