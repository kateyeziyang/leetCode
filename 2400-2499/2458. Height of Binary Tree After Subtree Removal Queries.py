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

"""
1. tree node has random value assigned
2. want to achieve O(n) - Independent
  need to have a method to know height after removing one node

how removing node impact height?
1. on height path (including equal case)
2. not on height path

Include a "height after removing myself" value on each node, as a dictionary
On each node, distance from root variable
Or, incremental lists containing dist->node -> num node in dist+1
When I remove a node, I need to know whether it impact height
    that relates to other part of the tree
"""

class Solution:
    def treeQueries(self, root: Optional[TreeNode], queries: List[int]) -> List[int]:

s = Solution()