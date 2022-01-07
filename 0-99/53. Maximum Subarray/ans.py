from typing import List, Optional
import heapq, math
from collections import defaultdict, deque
from bisect import bisect_left

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        minPrefixCount = 0
        maxValue = float("-inf")
        count = 0
        for i, num in enumerate(nums):
            count += num
            maxValue = max(maxValue,count-minPrefixCount)
            minPrefixCount = min(minPrefixCount,count)
        return maxValue

s = Solution()
assert s.maxSubArray(nums = [-2,1,-3,4,-1,2,1,-5,4])==6