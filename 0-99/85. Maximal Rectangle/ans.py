from typing import List, Optional
import heapq, math
from collections import defaultdict, deque,Counter
from bisect import bisect_left

# dp[i][j] 
class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        m,n = len(matrix,len(matrix[0]))
        ans = 0
        for i in range(m-1,-1,-1):
            for j in range(n-1,-1,-1):


s = Solution()