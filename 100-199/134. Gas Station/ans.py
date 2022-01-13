from typing import List, Optional
import heapq, math
from collections import defaultdict, deque, Counter
from bisect import bisect_left

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        curTank,totalTank = 0,0
        start = 0
        for i,g in enumerate(gas):
            totalTank += g-cost[i]
            curTank += g-cost[i]
            if curTank < 0:
                curTank = 0
                start = i+1
        return -1 if totalTank < 0 else start

s = Solution()
print(s.canCompleteCircuit(gas = [1,2,3,4,5], cost = [3,4,5,1,2]))