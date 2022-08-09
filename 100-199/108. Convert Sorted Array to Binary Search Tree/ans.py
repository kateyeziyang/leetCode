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
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def setNode(l,r):
            if l<=r:
                m = (l+r)//2
                cur = TreeNode(nums[m])
                cur.left = setNode(l,m-1)
                cur.right = setNode(m+1,r)
                return cur
            return None
        n = len(nums)
        return setNode(0,n-1)

s = Solution()