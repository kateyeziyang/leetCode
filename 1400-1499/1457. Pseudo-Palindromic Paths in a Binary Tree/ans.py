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

# DFS + backtracking
# class Solution:
#     def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
#         def changeCount(node):
#             nonlocal numOdd
#             if d[node.val]:
#                 d[node.val] = False
#                 numOdd += 1
#             else:
#                 d[node.val] = True
#                 numOdd -= 1
#         d = defaultdict(lambda: True)
#         numOdd = 0
#         stack = deque([root])
#         seen = set()
#         ans = 0
        
#         while stack:
#             node = stack[-1]
#             changeCount(node)
#             if node in seen:
#                 stack.pop()
#                 continue
#             seen.add(node)
#             if not node.left and not node.right:
#                 ans += numOdd <= 1
#             if node.left:
#                 stack.append(node.left)
#             if node.right:
#                 stack.append(node.right)
#         return ans

class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:

s = Solution()