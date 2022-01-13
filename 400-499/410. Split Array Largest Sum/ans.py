from typing import List, Optional
import heapq, math
from collections import defaultdict, deque,Counter
from bisect import bisect_left

# backtracking
class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        def helper(i,rem):
            pass
        n = len(nums)
        dp = [[float("inf"),0]*(m+1) for _ in n] # dp[i][j] is the minied largest sum for nums[i:] with j splits
        dp[-1][1] = nums[-1],nums[-1] # only dp[i][j for j <= i] will be filled
        for i in range(n-2,-1,-1):
            dp[i][1][0] = nums[i]+dp[i+1][1]
            dp[i][1][1] = dp[i][1][0]
        # dp[-2][2] max of nums[-2:]
        # dp[-3][2] max of nums[-3],dp[-2][1] nums[-3]+left split of dp[-2][2]
        # dp[-3][3] max of dp[-3][1],dp[-2][2]
        # dp[-4][4] max of dp[-4][1],dp[-3][3]
        # 

s = Solution()