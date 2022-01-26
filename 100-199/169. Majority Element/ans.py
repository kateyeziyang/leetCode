from typing import List, Optional
import heapq, math, random
from collections import defaultdict, deque, Counter
from bisect import bisect_left

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count,curelem = 0,nums[0]
        for i,x in enumerate(nums):
            if x==curelem:
                count += 1
            else:
                if count:
                    count -= 1
                else:
                    count,curelem = 1,x
        return curelem

s = Solution()