from typing import List, Optional
import heapq, math, random
from collections import defaultdict, deque, Counter
from bisect import bisect_left

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head: return True
        def reverse(head):
            if not head: return None
            phead = ListNode(-1)
            prev, cur = phead, head
            while cur:
                # tmp = cur.next
                # cur.next = prev
                # prev,cur = cur, tmp
                # check https://stackoverflow.com/questions/8725673/multiple-assignment-and-evaluation-order-in-python
                # prev, cur, cur.next = cur, cur.next, prev # this line doesn't work. why?
                prev, cur.next, cur = cur, prev, cur.next
            head.next = None
            return prev
        def compare(h1,h2):
            p,q = h1,h2
            while p and q:
                if p.val != q.val:
                    return False
                p,q = p.next,q.next
            return True
        slow, fast = head, head
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
        # if fast: # not fast.next, len of list is odd
        #     slow = slow.next
        reversedHead = reverse(slow)
        return compare(head,reversedHead)

s = Solution()
h = ListNode(1,ListNode(2,ListNode(2,ListNode(1))))
print(s.isPalindrome(h))