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
# class Solution:
#     def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
#         def setNode(l,r):
#             if l<=r:
#                 m = (l+r)//2
#                 cur = TreeNode(nums[m])
#                 cur.left = setNode(l,m-1)
#                 cur.right = setNode(m+1,r)
#                 return cur
#             return None
#         n = len(nums)
#         return setNode(0,n-1)

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def setNode(nums):
            if not len(nums): return None

            mid = (len(nums)-1)//2
            node = TreeNode(nums[mid])
            node.left = setNode(nums[:mid])
            node.right = setNode(nums[mid+1:])

            return node

        return setNode(nums)

s = Solution()