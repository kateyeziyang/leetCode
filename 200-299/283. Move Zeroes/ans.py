from typing import List, Optional
import heapq, math
from collections import defaultdict, deque,Counter
from bisect import bisect_left

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def lastOneLoc(i):
            for j in range(len(nums)-1,i,-1):
                if nums[j]!=0:
                    return j
            return -1
        def nextOneLoc(i):
            for j in range(i+1,len(nums)):
                if nums[j]!=0:
                    return j
            return -1
        for i,x in enumerate(nums):
            if x==0:
                nextOne = nextOneLoc(i)
                if nextOne!=-1:
                    nums[i],nums[nextOne] = nums[nextOne],nums[i]
                else:
                    break

s = Solution()