from typing import List, Optional
import heapq, math
from collections import defaultdict, deque
from bisect import bisect_left

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def reverseK(head): # should not reverse, if number of nodes start at head is less than k
            cur, next = head,head.next
            cur.next = None
            count = 1
            while next:
                count += 1
                tmp = next.next
                next.next = cur
                cur,next = next, tmp
                if count == k:
                    reversedHead,restHead=cur,next
                    break
            else:
                # reset all changes
                cur, next = cur, cur.next
                cur.next = None
                while next:
                    tmp = next.next
                    next.next = cur
                    cur,next = next, tmp
                reversedHead,restHead=cur,None
            return reversedHead,restHead
        if k==1: return head
        curHead,nextCurHead = None,head
        restHead = head
        returnHead = None
        while restHead:
            reversedHead,restHead = reverseK(restHead)
            if curHead:
                curHead.next = reversedHead
            curHead,nextCurHead = nextCurHead, restHead
            if not returnHead:
                returnHead = reversedHead
        return returnHead
s = Solution()
h = ListNode(1)
h.next = ListNode(2)
h.next.next = ListNode(3)
h.next.next.next = ListNode(4)
h.next.next.next.next = ListNode(5)
h.next.next.next.next.next = ListNode(6)
h.next.next.next.next.next.next = ListNode(7)
h.next.next.next.next.next.next.next = ListNode(8)
h.next.next.next.next.next.next.next.next = ListNode(9)
cur = s.reverseKGroup(h,3)
res = [3,2,1,6,5,4,9,8,7]
for i in range(9):
    assert cur.val == res[i]
    cur = cur.next