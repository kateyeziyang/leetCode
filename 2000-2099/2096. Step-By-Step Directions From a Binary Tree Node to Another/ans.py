from site import addpackage
from typing import List, Optional
import heapq, math, random
from collections import defaultdict, deque, Counter
from bisect import bisect_left

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        nodes = {}
        def addParent(node):
            nodes[node.val] = node
            if node.left:
                node.left.parent = node
                addParent(node.left)
            if node.right:
                node.right.parent = node
                addParent(node.right)
        addParent(root)

        startParents = set()
        startParentsNumUps = {}
        numUps = 0
        ptr = nodes[startValue]
        while ptr:
            startParents.add(ptr)
            startParentsNumUps[ptr] = numUps
            numUps += 1
            if ptr == root:
                break
            ptr = ptr.parent
        
        dest = nodes[destValue]
        if dest in startParents:
            return 'U'*startParentsNumUps[dest]
        
        ptr = dest
        path = []
        while ptr not in startParents:
            if ptr.parent.left == ptr:
                path.append('L')
            else:
                path.append('R')
            ptr = ptr.parent
        return 'U'*startParentsNumUps[ptr]+"".join(path[::-1])

s = Solution()