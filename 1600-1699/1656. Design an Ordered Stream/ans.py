from typing import List, Optional
import heapq, math, random
from collections import defaultdict, deque, Counter, OrderedDict
from bisect import bisect_left

class OrderedStream:

    def __init__(self, n: int):
        self.ptr = 1
        self.d = {}

    def insert(self, idKey: int, value: str) -> List[str]:
        self.d[idKey] = value
        if idKey == self.ptr:
            while self.ptr in self.d:
                self.ptr += 1
            ans = []
            for i in range(idKey, self.ptr):
                ans.append(self.d[i])
            return ans
        return []

# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)

s = Solution()