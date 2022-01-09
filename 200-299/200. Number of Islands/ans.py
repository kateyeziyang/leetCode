from typing import List, Optional
import heapq, math
from collections import defaultdict, deque
from bisect import bisect_left

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def visitIsland(r,c):
            nonlocal visited,res
            q = deque([[r,c]])
            while q:
                i,j = q.popleft()
                for xoff,yoff in [[-1,0],[0,-1],[1,0],[0,1]]:
                    newx,newy = i+xoff,j+yoff
                    if 0<=newx<m and 0<=newy<n and grid[newx][newy]=="1" and (newx,newy) not in visited:
                        visited.add((newx,newy))
                        q.append([newx,newy])
            res += 1

        visited = set()
        m,n = len(grid),len(grid[0])
        res = 0
        for r in range(m):
            for c in range(n):
                if grid[r][c]=="1" and (r,c) not in visited:
                    visited.add((r,c))
                    visitIsland(r,c)
        return res

s = Solution()
assert s.numIslands(grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
])==3
assert s.numIslands(grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
])==1