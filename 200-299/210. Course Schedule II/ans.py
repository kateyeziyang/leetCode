from typing import List, Optional
import heapq, math, random
from collections import defaultdict, deque, Counter
from bisect import bisect_left

# class Solution:
#     # Topo
#     def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
#         g = defaultdict(list)
#         inDegrees = [0] * numCourses

#         for course, prev in prerequisites:
#             g[prev].append(course)
#             inDegrees[course] += 1
        
#         nodes = [i for i in range(numCourses) if inDegrees[i] == 0]
#         ans = []
#         for course in nodes:
#             ans.append(course)
#             for nextCourse in g[course]:
#                 inDegrees[nextCourse] -= 1
#                 if not inDegrees[nextCourse]:
#                     nodes.append(nextCourse)
#         return ans if len(ans) == numCourses else []

class Solution:
    # DFS, is reverse post ordering=topological sort
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        if not len(prerequisites): return list(range(numCourses))
        g = defaultdict(list)
        for course, preq in prerequisites:
            g[preq].append(course)
            
        visited = [False] * numCourses
        popped = [False] * numCourses
        ans = []
        for k in range(numCourses):
            if popped[k]: continue
            st = deque([k])
            while st:
                node = st[-1]
                if visited[node]:
                    st.pop()
                    if not popped[node]:
                        ans.append(node)
                        popped[node] = True
                else:
                    visited[node] = True
                    for nb in g[node]:
                        if popped[nb]: continue
                        if visited[nb]: return []
                        st.append(nb)
        return reversed(ans) if len(ans) == numCourses else []

s = Solution().findOrder
assert s(8,[[1,0],[2,6],[1,7],[6,4],[7,0],[0,5]])==[5,4,6,3,2,0,7,1]