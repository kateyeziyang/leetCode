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
# class Solution:
#     def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
#         ans = []
#         def DFS(ascendant, node, isRight):
#             if not node.left and not node.right:
#                 curIteration.append(node.val)
#                 if not isRight:
#                     ascendant.left = None
#                 else:
#                     ascendant.right = None
#             if node.left:
#                 DFS(node,node.left,0)
#             if node.right:
#                 DFS(node,node.right,1)
#         fakeroot = TreeNode(-1,root)
#         while fakeroot.left:
#             curIteration = []
#             DFS(fakeroot,fakeroot.left,0)
#             ans.append(curIteration)
#         return ans

s = Solution()