from typing import List, Optional
import heapq, math, random
from collections import defaultdict, deque, Counter
from bisect import bisect_left

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        enum = list(enumerate(nums))
        enum.sort(key=lambda i: i[1])
        l, r = 0, len(nums)-1

        while l < r:
            v = enum[l][1] + enum[r][1]
            if v == target:
                return [enum[l][0], enum[r][0]]
            if v > target:
                r -= 1
            else:
                l += 1

s = Solution()