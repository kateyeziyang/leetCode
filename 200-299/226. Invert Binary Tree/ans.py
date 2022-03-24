from curses.ascii import isblank
from typing import List, Optional
import heapq, math, random
from collections import defaultdict, deque, Counter
from bisect import bisect_left

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def invertNode(node):
            if node:
                node.left,node.right = node.right,node.left
                invertNode(node.left)
                invertNode(node.right)
        invertNode(root)
        return root

s = Solution()