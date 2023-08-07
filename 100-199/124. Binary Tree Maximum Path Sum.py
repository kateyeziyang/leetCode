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
    ans = float("-inf")

    def buildOneDirectionMaxSum(self, node):
        """
        For each node, build the max sum of the path from one of its decendants to itself 
        """
        if not node: return
        self.buildOneDirectionMaxSum(node.left)
        self.buildOneDirectionMaxSum(node.right)
        maxLeft = node.left.oneDirectionSum if node.left else 0
        maxRight = node.right.oneDirectionSum if node.right else 0
        node.oneDirectionSum = node.val + max(0, maxLeft, maxRight)
        self.ans = max(self.ans, node.val + max(0, maxLeft) + max(0, maxRight))

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.buildOneDirectionMaxSum(root)
        return self.ans

s = Solution()