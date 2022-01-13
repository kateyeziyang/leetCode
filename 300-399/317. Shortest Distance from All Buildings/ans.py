from typing import List, Optional
import heapq, math
from collections import defaultdict, deque,Counter
from bisect import bisect_left

# from all houses to all empty lands
# at 2nd,3rd.. houses, only visit those visited by previous houses
# a matrix similar to grid, but each entry is cur total distance
# to avoid creating visited matrix for empty cells every time, change grid to -1,-2,-3...
class Solution:
    def shortestDistance(self, grid: List[List[int]]) -> int:
        def bfs(i,j):
            nonlocal val
            q = deque([[i,j]])
            count = 0

            while q:
                count += 1
                for _ in range(len(q)):
                    r,c = q.popleft()
                    for roff,coff in [[1,0],[-1,0],[0,-1],[0,1]]:
                        nr,nc = r+roff,c+coff
                        if 0<=nr<m and 0<=nc<n and grid[nr][nc]==val:
                            grid[nr][nc] -= 1
                            dists[nr][nc] += count
                            q.append([nr,nc])
            val -= 1
        val = 0
        m,n = len(grid),len(grid[0])
        dists = [[0]*n for _ in range(m)]
        numBuildings = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j]==1:
                    numBuildings += 1
                    bfs(i,j)
        ans = float("inf")
        for i in range(m):
            for j in range(n):
                if grid[i][j]==-numBuildings:
                    ans = min(ans,dists[i][j])
        return -1 if ans == float("inf") else ans

s = Solution()
print(s.shortestDistance([[1,0,2,0,1],[0,0,0,0,0],[0,0,1,0,0]]))