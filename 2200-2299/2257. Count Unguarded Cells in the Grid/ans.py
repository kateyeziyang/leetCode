from typing import List, Optional
import heapq, math, random
from collections import defaultdict, deque, Counter
from bisect import bisect_left
from enum import Enum

class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        mat = [[0]*n for _ in range(m)]

        for r,c in guards+walls:
            mat[r][c] = 1

        dirs = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        for r,c in guards:
            for roff,coff in dirs:
                curr,curc = r+roff,c+coff
                while 0<=curr<m and 0<=curc<n and mat[curr][curc]!=1:
                    mat[curr][curc] = 2
                    curr,curc = curr+roff,curc+coff
        
        return sum(row.count(0) for row in mat)


s = Solution()
print(s.countUnguarded(m = 4, n = 6, guards = [[0,0],[1,1],[2,3]], walls = [[0,1],[2,2],[1,4]]))
print(s.countUnguarded(6
,10
,[[0,6],[2,2],[2,5],[1,2],[4,9],[2,9],[5,6],[4,6]]
,[[1,5]]))