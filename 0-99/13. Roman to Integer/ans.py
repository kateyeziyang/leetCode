from typing import List, Optional
import heapq, math
from collections import defaultdict, deque,Counter
from bisect import bisect_left

class Solution:
    def romanToInt(self, s: str) -> int:
        romanMap = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        subMap = {"I":{"V","X"},"X":{"L","C"},"C":{"D","M"}}
        count = 0
        for i,c in enumerate(s):
            if c in subMap and i+1<len(s) and s[i+1] in subMap[c]:
                count -= romanMap[c]
            else:
                count += romanMap[c]
        return count

s = Solution()