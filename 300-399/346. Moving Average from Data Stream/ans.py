from typing import List, Optional
import heapq, math, random
from collections import defaultdict, deque, Counter
from bisect import bisect_left

class MovingAverage:
    def __init__(self, size: int):
        self.total = 0
        self.num = 0
        self.limit = size
        self.deq = deque()

    def next(self, val: int) -> float:
        if self.num == self.limit:
            self.total = self.total - self.deq.popleft() + val
        else:
            self.num += 1
            self.total += val
        self.deq.append(val)
        return self.total / self.num

# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)

s = Solution()