from typing import List, Optional
import heapq, math
from collections import defaultdict, deque

class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        m,n = len(dungeon),len(dungeon[0])
        mhps = [[0]*n for i in m]
        curhps = [[0]*n for i in m]
        mhps[0][0] = -min(0,dungeon[0][0])
        curhps[0][0] = max(0, dungeon[0][0])
        for j in range(1,n):
            curhp = curhps[0][j-1]+dungeon[0][j]
            mhps[0][j] = min(-min(0,curhp),mhps[0][j-1])
            curhps[0][j] = max(0,curhp)
        for i in range(1,n):
            curhp = curhps[i-1][0]+dungeon[i][0]
            mhps[i][0] = min(-min(0,curhp),mhps[i-1][0])
            curhps[i][0] = max(0,curhp)
        for i in range(1,m):
            for j in range(1,n):
                curhps_up = curhps[i-1][j]
                curhps_left = curhps[i][j-1]
                maxcur = max(curhps_up,curhps_left)+dungeon[i][j]
                if curhps_up >= curhps_left:

                prevmhps = mhps[i-1][j] if isUp else mhps[i][j-1]
                mhps[i][j] = min(0,-maxcur)

        return min(1,-mhps[0][0])


s = Solution()