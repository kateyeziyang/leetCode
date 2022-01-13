from typing import List, Optional
import heapq, math
from collections import defaultdict, deque, Counter
from bisect import bisect_left

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        numsSum = sum(nums)
        count = 0
        for i,x in enumerate(nums):
            if 2*count==numsSum-x:
                return i
            count += x
        return -1

s = Solution()