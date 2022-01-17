from typing import List, Optional
import heapq, math, random
from collections import defaultdict, deque, Counter
from bisect import bisect_left

class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        def bfs(r,c):
            q = deque([[r,c]])
            grid[r][c] = islandidx
            count = 0
            while q:
                count += 1
                i, j = q.popleft()
                for roff,coff in dirs:
                    ni,nj = i+roff,j+coff
                    if 0<=ni<m and 0<=nj<n and grid[ni][nj]==1:
                        grid[ni][nj] = islandidx
                        q.append([ni,nj])
            islandArea[islandidx] = count
        dirs = [[1,0],[0,1],[-1,0],[0,-1]]
        islandArea = {}
        islandidx = -1
        m,n = len(grid),len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j]==1:
                    bfs(i,j)
                    islandidx -= 1
        if sum(islandArea.values())==m*n:
            return m*n
        ans = float("-inf")
        for i in range(m):
            for j in range(n):
                if grid[i][j]==0:
                    changedArea = 1
                    visited = set()
                    for roff,coff in dirs:
                        ni,nj = i+roff,j+coff
                        if 0<=ni<m and 0<=nj<n and grid[ni][nj]!=0 and grid[ni][nj] not in visited:
                            changedArea += islandArea[grid[ni][nj]]
                            visited.add(grid[ni][nj])
                    ans = max(ans,changedArea)
        return ans

s = Solution()
# print(s.largestIsland(grid = [[1,0],[0,1]]))
print(s.largestIsland(grid = [[1,1,0],[1,0,1],[1,1,0]]))