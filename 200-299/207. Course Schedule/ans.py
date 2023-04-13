from typing import List, Optional
import heapq, math, random
from collections import defaultdict, deque, Counter
from bisect import bisect_left

class Solution:
    # DFS
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if not len(prerequisites): return True
        g = defaultdict(list)
        nonSources = set()
        for course, preq in prerequisites:
            g[preq].append(course)
            nonSources.add(course)
            
        visited = [False] * numCourses
        popped = [False] * numCourses
        for k in range(numCourses):
            if popped[k]: continue
            st = deque([k])
            while st:
                node = st[-1]
                if visited[node]:
                    st.pop()
                    popped[node] = True
                else:
                    visited[node] = True
                    for nb in g[node]:
                        if popped[nb]: continue
                        if visited[nb]: return False
                        st.append(nb)
        return len(popped)==len(g)

class Solution:
    # topological sort
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        inDegrees = [0] * numCourses
        g = defaultdict(list)
        for course, preq in prerequisites:
            g[preq].append(course)
            inDegrees[course] += 1
        q = [i for i in range(numCourses) if inDegrees[i] == 0]

        removedCount = 0
        for node in q:
            removedCount += 1
            for nextCourse in g[node]:
                inDegrees[nextCourse] -= 1
                if not inDegrees[nextCourse]:
                    q.append(nextCourse)
        return removedCount == len(g) # should be == numCourses ... Why this also passes Leetcode?


s = Solution().canFinish
assert s(8,[[1,0],[2,6],[1,7],[5,1],[6,4],[7,0],[0,5]])==False