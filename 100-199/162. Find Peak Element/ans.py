from typing import List, Optional
import heapq, math
from collections import defaultdict, deque, Counter
from bisect import bisect_left

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n = len(nums)
        l,r = 0, n-1
        while l<= r:
            m = (l+r)//2
            midv = nums[m]
            if (m==0 or nums[m-1]<midv) and (m==n-1 or nums[m+1]<midv):
                return m
            elif (m==0 or nums[m-1]<midv) and (m==n-1 or nums[m+1]>midv):
                l = m+1
            else:
                r = m-1

s = Solution()