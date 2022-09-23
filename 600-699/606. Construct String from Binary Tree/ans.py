from typing import List, Optional
import heapq, math, random
from collections import defaultdict, deque, Counter
from bisect import bisect_left

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
# class Solution:
#     def tree2str(self, root: Optional[TreeNode]) -> str:
#         def dfs(node):
#             result.append(str(node.val))
#             if node.left:
#                 result.append('(')
#                 dfs(node.left)
#                 result.append(')')
#             elif node.right:
#                 result.append('()')
#             if node.right:
#                 result.append('(')
#                 dfs(node.right)
#                 result.append(')')

#         if not root: return []

#         result = []
#         dfs(root)
#         return ''.join(result)

# class Solution:
#     def tree2str(self, root: Optional[TreeNode]) -> str:
#         result = []
#         stack = deque([[root,0]])

#         while stack:
#             node,numSuffixPar = stack.pop()
#             result.append('(')
#             result.append(str(node.val))
#             if not node.left and not node.right:
#                 result.append(')'*numSuffixPar)
#                 continue
#             if node.right:
#                 stack.append([node.right,1+numSuffixPar])
#                 numSuffixPar = 0
#                 if not node.left:
#                     result.append('()')
#             if node.left:
#                 stack.append([node.left,1+numSuffixPar])
#         return ''.join(result[1:])

class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        result = []
        stack = deque([root])
        visited = set()

        while stack:
            node = stack[-1]
            if node in visited:
                result.append(')')
                stack.pop()
                continue
            visited.add(node)
            result.append('('+str(node.val))
            if node.right:
                stack.append(node.right)
                if not node.left:
                    result.append('()')
            if node.left:
                stack.append(node.left)
        return ''.join(result)[1:-1]

s = Solution()
def tree_constructor(node_list: List[int]) -> TreeNode:
    root = TreeNode(node_list[0])
    curr = [root]
    ptr = 1

    while ptr < len(node_list):
        curr2 = []
        for c in curr:
            if node_list[ptr] is not None:
                new = TreeNode(node_list[ptr])
                c.left = new
                curr2.append(new)
            ptr += 1
            if ptr >= len(node_list):
                break
            if node_list[ptr] is not None:
                new = TreeNode(node_list[ptr])
                c.right = new
                curr2.append(new)
            ptr += 1
            if ptr >= len(node_list):
                break
        curr = curr2
    return root
# tree_constructor([1,2,3,4])
print(s.tree2str(tree_constructor([1,2,3,4])))