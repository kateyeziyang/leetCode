from typing import List, Optional
import heapq, math
from collections import defaultdict, deque

"""
this question not hard, even me can do it (after ~2 hours of work)
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        mps = float("-inf")
        def evaluateSubTree(node): # return value, isNotEmpty
            nonlocal mps
            if not node:
                return 0
            leftmps = evaluateSubTree(node.left)
            rightmps = evaluateSubTree(node.right)
            candidates = [node.val,rightmps+node.val,leftmps+node.val,leftmps+rightmps+node.val]
            mps = max(mps, max(candidates))
            return max(candidates[:-1])
        evaluateSubTree(root)
        return mps

# class Solution:
#     def maxPathSum(self, root: Optional[TreeNode]) -> int:
#         def evaluateSubTree(node): # return value, isNotEmpty
#             if not node:
#                 return 0,False
#             leftmps,le = evaluateSubTree(node.left)
#             rightmps,re = evaluateSubTree(node.right)
#             candidates = [node.val,leftmps+rightmps+node.val,rightmps+node.val,leftmps+node.val]
#             if le:
#                 candidates.append(leftmps)
#             if re:
#                 candidates.append(rightmps)
#             return max(candidates),True
#         mps,_ = evaluateSubTree(root)
#         return mps

s = Solution()