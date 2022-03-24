from curses.ascii import isblank
from typing import List, Optional
import heapq, math, random
from collections import defaultdict, deque, Counter
from bisect import bisect_left

# https://leetcode.com/problems/dinner-plate-stacks/discuss/366331/C%2B%2BPython-Two-Solutions
class DinnerPlates:

    def __init__(self, capacity: int):
        self.c = capacity
        self.q = []
        self.stacks = []

    def push(self, val: int) -> None:
        while self.q and self.q[0]<len(self.stacks) and len(self.stacks[self.q[0]])==self.c:
            heapq.heappop(self.q)
        if not self.q:
            heapq.heappush(self.q,len(self.stacks))
        if self.q[0]==len(self.stacks):
            self.stacks.append([])
        self.stacks[self.q[0]].append(val)

    def pop(self) -> int:
        while self.stacks and not self.stacks[-1]:
            self.stacks.pop()
        return self.popAtStack(len(self.stacks)-1)
    
    def popAtStack(self, index: int) -> int:
        if 0<=index<len(self.stacks) and self.stacks[index]:
            if len(self.stacks[index])==self.c: # I add this line!
                heapq.heappush(self.q,index)
            return self.stacks[index].pop()
        return -1
    
s = Solution()