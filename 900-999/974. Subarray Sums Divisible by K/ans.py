from re import L
from typing import List, Optional
import heapq, math, random
from collections import defaultdict, deque, Counter
from bisect import bisect_left

class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        d = defaultdict(int)

        curSum = 0
        for num in nums:
            curSum += num
            d[curSum%k] += 1
        
        ans = d[0]
        for val in d.values():
            ans += (val-1)*val//2
        return ans
s = Solution()