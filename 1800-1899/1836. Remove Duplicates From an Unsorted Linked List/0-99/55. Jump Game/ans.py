from typing import List, Optional
import heapq, math, random
from collections import defaultdict, deque, Counter
from bisect import bisect_left

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        l = r = 0
        n = len(nums)
        while l<=r:
            oldr = r
            for i in range(l,r+1):
                r = max(r,i+nums[i])
            l,r = oldr+1,min(r,n-1)
        return r==n-1

s = Solution()
print(s.canJump([2,3,1,1,4]))