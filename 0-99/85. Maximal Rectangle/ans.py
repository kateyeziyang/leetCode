from typing import List, Optional
import heapq, math
from collections import defaultdict, deque,Counter
from bisect import bisect_left

# dp[i][j] 
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        res = 0
        st = deque()
        for i,h in enumerate(heights): # non decreasing stack
            newidx = i
            while st and st[-1][0]>h:
                hei,idx = st.pop()
                res = max(res,hei*(i-idx))
                newidx = idx
            st.append([h,newidx])
        while st:
            hei,idx = st.pop()
            res = max(res,hei*(len(heights)-idx))
        return res

    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        m,n = len(matrix),len(matrix[0])
        cur = [int(x) for x in matrix[0]]
        ans = self.largestRectangleArea(cur)
        for i in range(1,m):
            for j in range(n):
                cur[j] = 0 if matrix[i][j]=="0" else 1+cur[j]
            ans = max(ans,self.largestRectangleArea(cur))
        return ans

s = Solution()
print(s.maximalRectangle(matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]))