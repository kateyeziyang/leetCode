from typing import List, Optional
import heapq, math, random
from collections import defaultdict, deque, Counter
from bisect import bisect_left

from transformers import VisionTextDualEncoderConfig

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0]:
            return -1
        dirs = [[1,0],[0,1],[-1,0],[0,-1],[1,1],[1,-1],[-1,1],[-1,-1]]
        q = deque([[0,0]])
        n = len(grid)
        if n == 1:
            return -1 if grid[0][0] else 1
        if grid[-1][-1]:
            return -1
        visited = [[0]*n for _ in range(n)]
        visited[0][0] = 1
        dist = 1
        while q:
            dist += 1
            for _ in range(len(q)):
                i,j = q.popleft()
                for ioff,joff in dirs:
                    newi,newj = i+ioff,j+joff
                    if 0<=newi<n and 0<=newj<n and not visited[newi][newj]:
                        if newi==n-1 and newj==n-1:
                            return dist
                        visited[newi][newj] = 1
                        if not grid[newi][newj]:
                            q.append([newi,newj])
            pass
        return -1



s = Solution()
print(s.shortestPathBinaryMatrix([[0,0,0],[1,1,0],[1,1,0]]))