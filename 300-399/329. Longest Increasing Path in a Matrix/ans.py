from typing import List, Optional
import heapq, math
from collections import defaultdict, deque,Counter
from bisect import bisect_left

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        def dfs(r,c):
            if (r,c) in memo:
                return memo[(r,c)]
            num = matrix[r][c]
            curIIP = 1
            for roff,coff in[[-1,0],[0,-1],[1,0],[0,1]]:
                newr,newc = r+roff,c+coff
                if 0<=newr<m and 0<=newc<n and matrix[newr][newc]>num:
                    if (newr,newc) not in memo:
                        dfs(newr,newc)
                    curIIP = max(curIIP,1+memo[(newr,newc)])
            memo[(r,c)] = curIIP
            return memo[(r,c)]

        m,n = len(matrix),len(matrix[0])
        memo = {}
        ans = 1
        for r in range(m):
            for c in range(n):
                ans = max(ans,dfs(r,c))
        return ans

# class Solution:
#     def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
#         adjlist = defaultdict(list)
#         sources = []
#         m,n = len(matrix),len(matrix[0])
#         for r in range(m):
#             for c in range(n):
#                 num = matrix[r][c]
#                 isSource = True
#                 for roff,coff in[[-1,0],[0,-1],[1,0],[0,1]]:
#                     newr,newc = r+roff,c+coff
#                     if 0<=newr<m and 0<=newc<n:
#                         if matrix[newr][newc]>num:
#                             adjlist[(r,c)].append([newr,newc])
#                         elif matrix[newr][newc]<num:
#                             isSource = False
#                 if isSource:
#                     sources.append([r,c])
#         ans = 0
#         for r,c in sources:
#             q = deque([[r,c]])
#             count = 0
#             while q:
#                 count += 1
#                 for _ in range(len(q)):
#                     r,c = q.popleft()
#                     if (r,c) in adjlist:
#                         q.extend(adjlist[(r,c)])
#                     else:
#                         ans = max(ans,count)
#         return ans

s = Solution()
print(s.longestIncreasingPath(matrix = [[9,9,4],[6,6,8],[2,1,1]]))
print(s.longestIncreasingPath([[1,2],[2,3]]))