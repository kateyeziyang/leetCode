from curses.ascii import isblank
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
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def dfs(a,b):
            if not a and not b: return True
            if not a or not b: return False
            return a.val==b.val and dfs(a.left,b.left) and dfs(a.right,b.right)
        return dfs(p,q)

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root and not subRoot: return False
        val = subRoot.val
        def dfs(node):
            if node:
                if node.val==val and self.isSameTree(node,subRoot):
                    return True
                return dfs(node.left) or dfs(node.right)
            return False
        return dfs(root)

s = Solution()