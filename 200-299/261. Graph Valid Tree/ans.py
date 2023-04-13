from typing import List, Optional
import heapq, math, random
from collections import defaultdict, deque, Counter, namedtuple
from bisect import bisect_left

class Solution:
    # union find
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n-1: return False

        disjoinedSets = {}

        # path compression
        def find(node):
            if node not in disjoinedSets:
                disjoinedSets[node] = [-1, 1]
                return node
            if disjoinedSets[node][0] == -1: return node
            root = find(disjoinedSets[node][0])
            disjoinedSets[node][0],disjoinedSets[node][1] = root, 1
            return root
        def merge(rootA, rootB):
            if disjoinedSets[rootA][1] > disjoinedSets[rootB][1]:
                rootA, rootB = rootB, rootA
            disjoinedSets[rootA][0] = rootB
            disjoinedSets[rootB][1] += disjoinedSets[rootA][1]

        for src,dst in edges:
            rootSrc, rootDst = find(src), find(dst)
            if rootSrc == rootDst: return False
            merge(rootSrc, rootDst)
        return True

class Solution:
    # using the fact being fully connected
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n-1: return False
        g = defaultdict(set)
        for src,dst in edges:
            g[src].add(dst)
            g[dst].add(src)
        
        q = [0]
        visited = set([0])
        for node in q:
            for nb in g[node]:
                if nb not in visited:
                    q.append(nb)
                    visited.add(nb)

        return len(visited) == n

class Solution:
    # using the fact being fully connected
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n-1: return False
        g = defaultdict(set)
        for src,dst in edges:
            g[src].add(dst)
            g[dst].add(src)
        
        q = [0]
        visited = set([0])
        for node in q:
            for nb in g[node]:
                if nb not in visited:
                    q.append(nb)
                    visited.add(nb)

        return len(visited) == n

class Solution:
    # pass parent to q
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n-1: return False
        g = defaultdict(set)
        for src,dst in edges:
            g[src].add(dst)
            g[dst].add(src)
        
        q = deque([[0, -1]])
        visited = set([0])
        while q:
            node, parent = q.pop()
            for nb in g[node]:
                if nb == parent: continue
                if nb in visited: return False
                q.append([nb, node])
                visited.add(nb)

        return len(visited) == n

class Solution:
    # remove neighbor
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n-1: return False
        g = defaultdict(set)
        for src,dst in edges:
            g[src].add(dst)
            g[dst].add(src)
        
        q = [0]
        visited = set([0])
        for node in q:
            for nb in g[node]:
                if nb in visited: return False
                g[nb].remove(node)
                q.append(nb)
                visited.add(nb)

        return len(visited) == n

s = Solution().validTree
assert s(5,[[0,1],[0,2],[0,3],[1,4]])==True
assert s(5,[[0,1],[0,2],[0,3],[1,4], [4,0]])==False