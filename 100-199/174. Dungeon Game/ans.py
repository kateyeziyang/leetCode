from typing import List, Optional
import heapq, math
from collections import defaultdict, deque

class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        m,n = len(dungeon),len(dungeon[0])
        uprow,downrow = [0]*n,[0]*n
        isUp = False

        for i in range(m-1,-1,-1):
            for j in range(n-1,-1,-1):
                currow = uprow if isUp else downrow
                nextrow = uprow if not isUp else downrow
                minhp = None
                if i<m-1:
                    minhp = nextrow[j]
                if j<n-1:
                    minhp = currow[j+1] if not minhp else min(minhp,currow[j+1])
                minhp = 1 if not minhp else minhp
                currow[j] = max(1,minhp-dungeon[i][j])
            isUp = not isUp
        return currow[0]

# class Solution:
#     def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
#         m,n = len(dungeon),len(dungeon[0])
#         dp = [[0]*n for i in range(m)]
#         for i in range(m-1,-1,-1):
#             for j in range(n-1,-1,-1):
#                 minhp = None
#                 if i<m-1:
#                     minhp = dp[i+1][j]
#                 if j<n-1:
#                     minhp = dp[i][j+1] if not minhp else min(minhp,dp[i][j+1])
#                 minhp = 1 if not minhp else minhp
#                 dp[i][j] = max(1,minhp-dungeon[i][j])
#         return dp[0][0]

s = Solution()
assert s.calculateMinimumHP(dungeon = [[-2,-3,3],[-5,-10,1],[10,30,-5]])==7
assert s.calculateMinimumHP([[-3],[-7]])==11