from typing import List, Optional
import heapq, math, random
from collections import defaultdict, deque, Counter
from bisect import bisect_left

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(node):
            if not node: return False
            result = node.val == 1
            lResult = dfs(node.left)
            if not lResult:
                node.left = None
            rResult = dfs(node.right)
            if not rResult:
                node.right = None
            return result or lResult or rResult
        
        fakeRoot = TreeNode(1, root)
        dfs(fakeRoot)
        return fakeRoot.left


s = Solution()