from typing import List, Optional
import heapq, math
from collections import defaultdict, deque,Counter
from bisect import bisect_left

# can binary search on k
# only save previous row
class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        m,n = len(grid),len(grid[0])
        if m==1 and n==1:
            return 0
        q = deque([[0,0,k]])
        visited = [[[False]*(k+1) for _ in range(n)] for _ in range(m)]
        for i in range(k+1):
            visited[0][0][i] = True
        count = 0
        while q:
            count += 1

            for _ in range(len(q)):
                r,c,remain = q.popleft()
                for roff,coff in [[1,0],[-1,0],[0,1],[0,-1]]:
                    newr,newc = r+roff,c+coff
                    if newr==m-1 and newc==n-1:
                        return count
                    if 0<=newr<m and 0<=newc<n:
                        if grid[newr][newc]:
                            if remain and not visited[newr][newc][remain-1]:
                                q.append([newr,newc,remain-1])
                                visited[newr][newc][remain-1] = True
                        elif not visited[newr][newc][remain]:
                            q.append([newr,newc,remain])
                            visited[newr][newc][remain] = True
        return -1

s = Solution()
print(s.shortestPath(grid = [[0,0,0],[1,1,0],[0,0,0],[0,1,1],[0,0,0]], k = 1))
print(s.shortestPath(grid = [[0,1,1],[1,1,1],[1,0,0]], k = 1))