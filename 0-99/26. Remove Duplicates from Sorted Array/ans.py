from typing import List, Optional
import heapq, math, random
from collections import defaultdict, deque, Counter
from bisect import bisect_left

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums: return None
        l,r=0,1
        while r<len(nums):
            if nums[r]!=nums[l]:
                l+=1
                nums[l]=nums[r]
            r+=1
        return l

s = Solution()