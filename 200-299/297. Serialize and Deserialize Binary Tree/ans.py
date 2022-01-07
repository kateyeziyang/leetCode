from typing import List, Optional
import heapq, math
from collections import defaultdict, deque
from bisect import bisect_left

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        def helper(node):
            if node:
                ans.append(str(node.val))
                helper(node.left)
                helper(node.right)
            else:
                ans.append("#")
        ans = []
        helper(root)
        return " ".join(ans)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        def helper():
            val = next(vals)
            if val != "#":
                node = TreeNode(int(val))
                node.left = helper()
                node.right = helper()
                return node
        vals = iter(data.split(" "))
        return helper()

c = Codec()
r = TreeNode(5)
r.left = TreeNode(2)
r.right = TreeNode(9)
r.right.right = TreeNode(-5)
s = c.serialize(r)
r2 = c.deserialize(s)
pass