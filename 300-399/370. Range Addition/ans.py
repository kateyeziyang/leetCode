from typing import List, Optional
import heapq, math, random
from collections import defaultdict, deque, Counter
from bisect import bisect_left

class Solution:
    def getModifiedArray(self, length: int, updates: List[List[int]]) -> List[int]:
        incs = [0]*length
        arr = [0]*length
        for s,e,i in updates:
            incs[s] += i
            if e+1<length:
                incs[e+1] -= i
        curinc = 0
        for i in range(1,length):
            incs[i] += incs[i-1]
        return incs


class Solution:
    def getModifiedArray(self, length: int, updates: List[List[int]]) -> List[int]:
        ans = [0] * length
        for s, e, i in updates:
            ans[s] += i
            if e+1 < length:
                ans[e+1] -= i
        for i in range(1, length):
            ans[i] = ans[i-1] + ans[i]
        return ans

s = Solution()