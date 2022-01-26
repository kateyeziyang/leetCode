import enum
from typing import List, Optional
import heapq, math, random
from collections import defaultdict, deque, Counter
from bisect import bisect_left

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        allSum = sum(range(len(nums)+1))
        numSum = sum(nums)
        return allSum - numSum

s = Solution()
print(s.missingNumber(nums = [3,0,1]))