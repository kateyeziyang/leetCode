from typing import List, Optional
import heapq, math
from collections import defaultdict, deque,Counter
from bisect import bisect_left

class Solution:
    def minMoves(self, nums: List[int]) -> int:
        minCounts = 0
        minNum = nums[0]
        for i,x in enumerate(nums):
            if x<minNum:
                minCounts += i*(minNum-x)
                minNum = x
            else:
                minCounts += x-minNum
        return minCounts

s = Solution()