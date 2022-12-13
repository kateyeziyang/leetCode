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

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        for i in range(1, len(nums)):
            if nums[i] < nums[i-1]:
                return i-1
        return len(nums) - 1

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n = len(nums)
        l, r = 0, n-1
        while l < r: # =?
            mid = (l + r)//2
            midv = nums[mid]
            midlv = float('-inf') if mid==0 else nums[mid-1]
            midrv = float('-inf') if mid==n-1 else nums[mid+1]
            if midlv < midv and midv > midrv:
                return mid

            if midlv > midv: # why can someone think of this?
                r = mid-1
            else:
                l = mid+1
        return l

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n = len(nums)
        l, r = 0, n-1
        while l < r:
            mid = (l + r)//2
            midv = nums[mid]
            midrv = float('-inf') if mid==n-1 else nums[mid+1]

            if midrv > midv: # r can never equal to mid
                l = mid + 1
            else:
                r = mid
        return l

s = Solution()