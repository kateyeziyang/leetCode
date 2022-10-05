from typing import List, Optional
import heapq, math, random
from collections import defaultdict, deque, Counter
from bisect import bisect_left

class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        l,r = 0,0
        
        numStep = 0
        while True:
            if l<=n-1<=r: return numStep
            nr = r
            for i in range(l, r+1):
                loc = i+nums[i]
                nr = max(min(loc, n-1), nr)
            l = r+1
            r = nr
            numStep += 1

class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        r = 0
        nr = 0
        
        numStep = 0
        for i in range(n):
            nr = max(nr, i+nums[i])
            if i==r:
                numStep += 1
                r = nr
        return numStep

s = Solution()
print(s.jump([2,3,1,1,4]))