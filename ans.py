from typing import List, Optional
import heapq, math, random
from collections import defaultdict, deque, Counter
from bisect import bisect_left
import itertools



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
            if node_list[ptr] is not None:
                new = TreeNode(node_list[ptr])
                c.right = new
                curr2.append(new)
            ptr += 1
        curr = curr2
    return root