from typing import List, Optional
import heapq, math, random
from collections import defaultdict, deque, Counter
from bisect import bisect_left

class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        if not x and not y: return 0
        qa, qb = deque([(0,0)]), deque([(x,y)])
        offsets = [(1,2), (1,-2), (-1, 2), (-1,-2), (2,1),(2,-1),(-2,1),(-2,-1)]
        ans = 0
        visiteda, visitedb = {(0,0)}, {(x,y)}
        while True:
            ans += 1
            for _ in range(len(qa)):
                i,j = qa.popleft()
                for ioff,joff in offsets:
                    inew, jnew = i+ioff,j+joff
                    if (inew, jnew) not in visiteda:
                        if (inew, jnew) in visitedb:
                            return ans
                        visiteda.add((inew,jnew))
                        qa.append((inew,jnew))
            ans += 1
            for _ in range(len(qb)):
                i,j = qb.popleft()
                for ioff,joff in offsets:
                    inew, jnew = i+ioff,j+joff
                    if (inew, jnew) not in visitedb:
                        if (inew, jnew) in visiteda:
                            return ans
                        visitedb.add((inew,jnew))
                        qb.append((inew,jnew))




s = Solution()
t=[
    (1,2),
    (2,-1),
    (-8,4),
    (-1,-3)
]
for tc in t:
    print(s.minKnightMoves(*tc))