from curses.ascii import isblank
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
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return None
        ans = []
        q = deque([root])
        height = 1
        while q:
            for _ in range(len(q)):
                node = q.popleft()
                if len(ans) != height:
                    ans.append([])
                ans[-1].append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            height += 1
        return ans

s = Solution()