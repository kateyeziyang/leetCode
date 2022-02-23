from typing import List, Optional
import heapq, math, random
from collections import defaultdict, deque, Counter
from bisect import bisect_left

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicatesUnsorted(self, head: ListNode) -> ListNode:
        dup = {}
        p = head
        while p:
            val = p.val
            if val not in dup:
                dup[val] = False
            else:
                dup[val] = True
            p = p.next
        phead = ListNode(-1,head)
        prev = phead
        while prev.next:
            if dup[prev.next.val]:
                prev.next = prev.next.next
            else:
                prev = prev.next
        return phead.next


s = Solution()