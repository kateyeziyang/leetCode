from typing import List, Optional
import heapq, math, random
from collections import defaultdict, deque, Counter
from bisect import bisect_left

class Dnode:
    def __init__(self, val, prev = None, next = None) -> None:
        self.val = val
        self.prev = prev
        self.next = next

class MaxStack:

    def __init__(self):
        self.map = defaultdict(deque)
        h = Dnode("head")
        t = Dnode("tail")
        h.next = t
        t.prev = h
        self.dhead = h
        self.dtail = t
        self.maxheap = []

    def push(self, x: int) -> None:
        node = Dnode(x)
        node.prev = self.dtail.prev
        self.dtail.prev.next = node
        node.next = self.dtail
        self.dtail.prev = node
        
        if x not in self.map or not self.map[x]:
            heapq.heappush(self.maxheap, -x)
        self.map[x].append(node)

    def pop(self) -> int:
        node = self.dtail.prev
        node.prev.next = node.next
        node.next.prev = node.prev

        v = node.val
        self.map[v].pop()
        if not self.map[v] and self.maxheap[0] == -v:
            heapq.heappop(self.maxheap)
        return v

    def top(self) -> int:
        return self.dtail.prev.val

    def peekMax(self) -> int:
        while not self.map[-self.maxheap[0]]:
            heapq.heappop(self.maxheap)
        return -self.maxheap[0]

    def popMax(self) -> int:
        while not self.map[-self.maxheap[0]]:
            heapq.heappop(self.maxheap)
        v = -self.maxheap[0]
        node = self.map[v][-1]
        self.map[v].pop()
        if not self.map[v]:
            heapq.heappop(self.maxheap)

        node.prev.next = node.next
        node.next.prev = node.prev
        return v



# Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(5)
# param_3 = obj.top()
# param_2 = obj.pop()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()
m = MaxStack()
m.push(29)
m.push(65)
m.push(-18)