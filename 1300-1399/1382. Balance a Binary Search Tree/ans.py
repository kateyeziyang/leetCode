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
    def balanceBST(self, root: TreeNode) -> TreeNode:
        def balance(node):
            if not node: return 0, []
            if not node.left and node.right: return 1, [node]

            (lh, lhm), (rh, rhm) = balance(node.left), balance(node.right)
            if abs(lh-rh) <= 1: return max(lh, rh) + 1, [lhm] if lhm else node
            if lh<rh:
                
            else:

        balance(root)

s = Solution()