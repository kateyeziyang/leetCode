from typing import List, Optional
import heapq, math
from collections import defaultdict, deque

class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        if x==0 and y==0: return 0
        offset = {(1,2),(-1,2),(1,-2),(-1,-2),(2,1),(2,-1),(-2,1),(-2,-1)}
        v1,v2 = set([(0,0)]),set([(x,y)])
        q1,q2 = deque([(0,0)]),deque([(x,y)])
        c = 0
        while True:
            c += 1

            for i in range(len(q1)):
                curx,cury = q1.popleft()
                for xoff,yoff in offset:
                    newx,newy = curx+xoff,cury+yoff
                    if (newx,newy) in v2:
                        return 2*c - 1
                    if (newx,newy) not in v1:
                        v1.add((newx,newy))
                        q1.append((newx,newy))
            for i in range(len(q2)):
                curx,cury = q2.popleft()
                for xoff,yoff in offset:
                    newx,newy = curx+xoff,cury+yoff
                    if (newx,newy) in v1:
                        return 2*c
                    if (newx,newy) not in v2:
                        v2.add((newx,newy))
                        q2.append((newx,newy))

s = Solution()
assert s.minKnightMoves(x = 5, y = 5)==4
assert s.minKnightMoves(x = 3, y = 4)==3