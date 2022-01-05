from typing import List
import heapq, math
from collections import defaultdict, deque

class MedianFinder:

    def __init__(self):
        self.maxhp = [] # len(maxhp)-len(minhp) = {0,1}
        self.minhp = [] 

    def addNum(self, num: int) -> None:
        if len(self.maxhp)-len(self.minhp):
            val = heapq.heappushpop(self.maxhp,-num)
            heapq.heappush(self.minhp,-val)
            return
        if self.minhp and num > self.minhp[0]:
            val = heapq.heappushpop(self.minhp,num)
            heapq.heappush(self.maxhp,-val)
        else:
            heapq.heappush(self.maxhp,-num)


    def findMedian(self) -> float:
        val = self.maxhp[0]
        if len(self.maxhp)-len(self.minhp):
            ans = -val
        else:
            val2 = self.minhp[0]
            ans = (-val+val2)/2
        return ans

obj = MedianFinder()
obj.addNum(1)
obj.addNum(2)
param_2 = obj.findMedian()