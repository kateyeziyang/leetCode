from typing import List, Optional
import heapq, math, random
from collections import defaultdict, deque, Counter
from bisect import bisect_left

class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

# hey, no need to have two dictionarys, let key be ptr and val be prev

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head: return None
        d = {}
        nd = {}
        ptr = head
        idx = 0
        prevHead = Node(-1)
        prev = prevHead
        while ptr:
            prev.next = Node(ptr.val)
            prev = prev.next
            nd[idx] = prev
            d[ptr] = idx
            ptr = ptr.next
            idx += 1
        ptr = head
        nptr = prevHead.next
        while ptr:
            if ptr.random:
                nptr.random = nd[d[ptr.random]]
            nptr = nptr.next
            ptr = ptr.next
        return prevHead.next

s = Solution()