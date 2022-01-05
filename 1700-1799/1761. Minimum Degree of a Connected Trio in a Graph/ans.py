from typing import List, Optional
import heapq, math
from collections import defaultdict, deque
from bisect import bisect_left

class Solution:
    def minTrioDegree(self, n: int, edges: List[List[int]]) -> int:
        g = defaultdict(set)
        degree = defaultdict(int)
        for v1,v2 in edges:
            g[min(v1,v2)].add(max(v1,v2))
            degree[v1] += 1
            degree[v2] += 1

        ans = float("inf")
        for v1 in range(1,n+1):
            for v2 in g[v1]:
                for v3 in g[v1]:
                    if v3 in g[v2]:
                        ans = min(ans,degree[v1]+degree[v2]+degree[v3]-6)
        return -1 if ans == float("inf") else ans

# class Solution:
#     def minTrioDegree(self, n: int, edges: List[List[int]]) -> int:
#         g = defaultdict(set)
#         degree = defaultdict(int)
#         for v1,v2 in edges:
#             g[min(v1,v2)].add(max(v1,v2))
#             degree[v1] += 1
#             degree[v2] += 1

#         ans = float("inf")
#         for v1 in range(1,n+1):
#             for v2 in g[v1]:
#                 for v3 in g[v1]:
#                     if v3 in g[v2]:
#                         ans = min(ans,degree[v1]+degree[v2]+degree[v3]-6)
#         return -1 if ans == float("inf") else ans

s = Solution()
# assert s.minTrioDegree(n = 6, edges = [[1,2],[1,3],[3,2],[4,1],[5,2],[3,6]])==3
assert s.minTrioDegree(6,[[6,5],[4,3],[5,1],[1,4],[2,3],[4,5],[2,6],[1,3]])==3