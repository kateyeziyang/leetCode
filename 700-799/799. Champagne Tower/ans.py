from typing import List, Optional
import heapq, math, random
from collections import defaultdict, deque, Counter
from bisect import bisect_left

class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        tower = [[0]*k for k in range(1, 101)]
        tower[0][0] = poured

        for i in range(1, query_row+1):
            for j in range(i+1):
                l = max(0, tower[i-1][j-1]-1 if j-1>=0 else 0)
                r = max(0, tower[i-1][j]-1 if j<=i-1 else 0)
                tower[i][j] = (l+r)/2
        return min(1, tower[query_row][query_glass])

# poured = 5, row = 2, glass = 1
# 5
# 2 2
# 0.5 1 0.5
s = Solution()
print(s.champagneTower(5,2,1))