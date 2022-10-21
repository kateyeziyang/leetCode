from typing import List, Optional
import heapq, math, random
from collections import defaultdict, deque, Counter
from bisect import bisect_left

class Solution:
    def rob(self, nums: List[int]) -> int:
        def helper(l, r):
            n = r-l+1
            if n<=2: return max(nums[l:r+1])
            dp = [0]*n
            dp[0] = nums[l]
            dp[1] = max(dp[0], nums[l+1])
            for i in range(2, n):
                dp[i] = max(dp[i-2]+nums[i+l], dp[i-1])
            return dp[-1]
        n = len(nums)
        if n==1: return nums[0]
        return max(helper(0,n-2), helper(1, n-1))

s = Solution()