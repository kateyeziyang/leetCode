from typing import List, Optional
import heapq, math, random
from collections import defaultdict, deque, Counter
from bisect import bisect_left

class Solution:
    def smallestRangeII(self, nums: List[int], k: int) -> int:
        nums.sort()
        a, i = nums[-1], nums[0]
        ans = a-i
        for i in range(len(nums)-1):
            c, n = nums[i], nums[i+1]
            ans = min(ans, max(a,c+k)-min(i,n-k))
        return ans
