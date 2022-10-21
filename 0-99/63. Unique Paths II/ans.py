from typing import List, Optional
import heapq, math, random
from collections import defaultdict, deque, Counter
from bisect import bisect_left

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        def getVal(i,j):
            if i<0 or j<0 or obstacleGrid[i][j]==1:
                return 0
            return obstacleGrid[i][j]
        if (obstacleGrid[0][0] == 1 or obstacleGrid[-1][-1] == 1):
            return 0
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        obstacleGrid[0][0] = -1
        for i in range(m):
            for j in range(n):
                if (i==0 and j==0) or obstacleGrid[i][j]==1:
                    continue
                obstacleGrid[i][j] = getVal(i-1,j)+getVal(i,j-1)
        return -obstacleGrid[-1][-1]

s = Solution()