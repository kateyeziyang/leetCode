from typing import List, Optional
import heapq, math
from collections import defaultdict, deque
from bisect import bisect_left

class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        def getCoprime(i,j):
            xi,yi = points[i]
            xj,yj = points[j]
            dx,dy = xi-xj,yi-yj
            if dx==0:
                return float("inf"),float("inf")
            if dy==0:
                return 0,0
            if dx<0:
                dx,dy = -dx,-dy
            cop = math.gcd(xj-xi,yj-yi)
            return dx//cop,dy//cop
        def helper(i):
            lines = defaultdict(lambda:1)
            maxPoints = 0
            for j in range(i+1,len(points)):
                linerepr = getCoprime(i,j)
                lines[linerepr] += 1
                maxPoints = max(maxPoints,lines[linerepr])
            return maxPoints
        if len(points)<3: return len(points)
        res = 2
        for i in range(len(points)):
            res = max(res,helper(i))
        return res
s = Solution()
assert s.maxPoints([[1,1],[2,2],[3,3]])==3
assert s.maxPoints(points = [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]])==4
assert s.maxPoints([[2,4],[1,2],[1,3],[1,-1]])==3