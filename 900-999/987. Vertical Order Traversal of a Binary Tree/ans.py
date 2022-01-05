from typing import List, Optional
import heapq, math
from collections import defaultdict, deque
from bisect import bisect_left

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        d = {}
        st = deque([(root,0,0)])
        while st:
            node,rownum,colnum = st.pop()
            if colnum not in d:
                d[colnum] = {rownum:[node.val]}
            else:
                if rownum not in d[colnum]:
                    d[colnum][rownum] = [node.val]
                else:
                    d[colnum][rownum].append(node.val)
            if node.right:
                st.append((node.right,rownum+1,colnum+1))
            if node.left:
                st.append((node.left,rownum+1,colnum-1))
        ans = []
        for k in sorted(d.keys()):#get min and max col nums to reduce this sort!
            tmp = []
            for row in sorted(d[k].keys()):
                tmp.extend(sorted(d[k][row]))
            ans.append(tmp)
        return ans

s = Solution()