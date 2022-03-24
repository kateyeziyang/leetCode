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
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        isBalanced = True
        def dfs(node):
            nonlocal isBalanced
            if not node:
                return -1
            ldep,rdep = dfs(node.left),dfs(node.right)
            if abs(ldep-rdep)>1:
                isBalanced = False
            return 1+max(ldep,rdep)
        dfs(root)
        return isBalanced
            

s = Solution()