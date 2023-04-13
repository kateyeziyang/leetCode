from typing import List, Optional
import heapq, math, random
from collections import defaultdict, deque, Counter
from bisect import bisect_left

"""
# Definition for a Node.
"""
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node: return None
        nodes = [None] * 101
        newStart = Node(node.val)
        nodes[node.val] = newStart
        
        q = deque([node])
        while q:
            curNode = q.popleft()
            newNeighbors = nodes[curNode.val].neighbors
            for nb in curNode.neighbors:
                v = nb.val
                if not nodes[v]:
                    nodes[v] = Node(v)
                    q.append(nb)
                newNeighbors.append(nodes[v])
        return newStart

s = Solution()