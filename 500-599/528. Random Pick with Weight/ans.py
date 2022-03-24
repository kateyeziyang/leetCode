from typing import List, Optional
import heapq, math, random
from collections import defaultdict, deque, Counter
from bisect import bisect_left
from itertools import accumulate

class Solution:

    def __init__(self, w: List[int]):
        self.total = sum(w)
        self.pref = list(accumulate(w))

    def pickIndex(self) -> int:
        r = random.randint(1,self.total)
        return bisect_left(self.pref,r)


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()

s = Solution([1,1,2])
ans = []
for _ in range(1000):
    ans.append(s.pickIndex())
print(Counter(ans))