from typing import List, Optional
import heapq, math
from collections import defaultdict, deque,Counter
from bisect import bisect_left

class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        ans = 1
        for i in range(len(nums)-1,-1,-1):
            ans = max(1,ans-nums[i])
        return ans

s = Solution()
s.minStartValue(
[-3,2,-3,4,2])