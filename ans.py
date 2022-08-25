from typing import List, Optional
import heapq, math, random
from collections import defaultdict, deque, Counter
from bisect import bisect_left

class Dnode:
    def __init__(self, val, prev = None, next = None) -> None:
        self.val = val
        self.prev = prev
        self.next = next

s = Solution()