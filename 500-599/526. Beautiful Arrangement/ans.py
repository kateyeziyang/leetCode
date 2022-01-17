from typing import List, Optional
import heapq, math
from collections import defaultdict, deque, Counter
from bisect import bisect_left

class Solution:
    def countArrangement(self, n: int) -> int:
        def bt(i):
            nonlocal ans
            if i==n+1:
                ans += 1
                return
            for num in range(1,n+1):
                if not used[num] and (num%i==0 or i%num==0):
                    used[num]=True
                    bt(i+1)
                    used[num]=False
        used = [False]*(n+1)
        ans = 0
        bt(1)
        return ans

s = Solution()
print(s.countArrangement(1))
print(s.countArrangement(2))