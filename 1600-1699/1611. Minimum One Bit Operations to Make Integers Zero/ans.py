from typing import List, Optional
import heapq, math
from collections import defaultdict, deque
from bisect import bisect_left

class Solution:
    def minimumOneBitOperations(self, n: int) -> int:
        def changeToZero(i):
            nonlocal ans
            if s[i]=="0":
                return
            if i!=l-1:
                changeToOne(i+1)
                for j in range(i+2,l):
                    changeToZero(j)
            ans += 1
            s[i] = "0"

        def changeToOne(i):
            nonlocal ans
            if s[i]=="1":
                return
            if i!=l-1:
                changeToOne(i+1)
                for j in range(i+2,l):
                    changeToZero(j)
            ans += 1
            s[i] = "1"
        s = bin(n)[2:]
        s = list(s)
        l = len(s)
        ans = 0
        for i in range(0,l):
            changeToZero(i)
        return ans

s = Solution()
assert s.minimumOneBitOperations(3)==2
assert s.minimumOneBitOperations(6)==4