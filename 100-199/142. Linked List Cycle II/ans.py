from typing import List, Optional
import heapq, math, random
from collections import defaultdict, deque, Counter
from bisect import bisect_left

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head: return None
        # start at 0
        # when slow enters cycle, it's has A steps (A=from head to start of cycle)
        # at this time, fast has 2A steps, its distance to start of cycle is A%C (C=length of cycle)
        # now in order to catch up with slow, fast need C-(A%C) steps
        # they will meet at C-(A%C) steps from start of cycle
        # now, let a third pointer points to head, and let third and slow moves
        # they will meet at start of cycle, because
        # when third at start of cycle, it has A steps
        # if slow takes A steps from (C-(A%C) steps from start of cycle)
        # (C-(A%C)+A)%C = (C-A+A)%C = 0
        slow,fast = head,head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow==fast:
                third = head
                while third != slow:
                    third = third.next
                    slow = slow.next
                return third
        return None

s = Solution()