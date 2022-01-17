from enum import EnumMeta
import enum
from typing import List, Optional
import heapq, math, random
from collections import defaultdict, deque, Counter
from bisect import bisect_left

class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        count = 0
        prefs = {}
        for i,x in enumerate(nums):
            count += x
            if (count%k==0 and i>=1) or (count%k in prefs and i-prefs[count%k]>1):
                return True
            if count%k not in prefs:
                prefs[count%k] = i
        return False

s = Solution()
print(s.checkSubarraySum([0],1))