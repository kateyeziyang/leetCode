from typing import List, Optional
import heapq, math
from collections import defaultdict, deque,Counter
from bisect import bisect_left

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def DFS(node):
            if not node:
                return -1
            node.leftDepth = 1+DFS(node.left)
            node.rightDepth = 1+DFS(node.right)
            return max(node.leftDepth,node.rightDepth)
        def helper(node):
            nonlocal ans
            if node:
                ans = max(ans,node.leftDepth+node.rightDepth)
                helper(node.left)
                helper(node.right)
        ans = 0
        DFS(root)
        helper(root)
        return ans

s = Solution()
r=TreeNode(1)
r.left=TreeNode(2)
r.left.right=TreeNode(3)
r.left.right.right=TreeNode(4)
r.left.right.right.right=TreeNode(5)
r.left.right.right.left=TreeNode(6)
r.left.right.right.left.right=TreeNode(7)
r.right=TreeNode(8)
r.right.right=TreeNode(9)
print(s.diameterOfBinaryTree(r))