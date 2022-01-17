from typing import List, Optional
import heapq, math, random
from collections import defaultdict, deque, Counter
from bisect import bisect_left

class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        n = len(s)
        if k>n:
            return s
        st = deque()
        for c in s:
            if st and st[-1][0]==c:
                if st[-1][1]==k-1:
                    st.pop()
                else:
                    st[-1][1] += 1
            else:
                st.append([c,1])
        buf = []
        for c,count in st:
            buf.append(c*count)
        return "".join(buf)

s = Solution()
print(s.removeDuplicates("pbbcggttciiippooaais", k = 2))