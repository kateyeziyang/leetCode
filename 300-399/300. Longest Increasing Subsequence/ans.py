from typing import List, Optional
import heapq, math, random
from collections import defaultdict, deque, Counter
from bisect import bisect_left

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1]*n # dp[i] is longest including nums[i]

        for i in range(1,n):
            for j in range(i-1,-1,-1):
                if nums[j]<nums[i]:
                    dp[i] = max(dp[i],dp[j]+ 1)
        return max(dp)

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        q = deque([[nums[0],1,float('-inf')]])

        for i in range(1,n):
            cur = 0
            while q and q[-1][0]<nums[i]: # while prev elem is less, pop and update longest
                cur = max(cur,q.pop()[1])
            if q and q[-1][0]==nums[i] and q[-1][1]>cur: # if prev is equal and bigger
                cur = q.pop()[1]
            else:
                cur += 1
            q.append([nums[i],cur])
            ans = max(ans,cur)
            
        return ans
# official solution too smart...
s = Solution()
print(s.lengthOfLIS(nums = [10,9,2,4,5,3,7,101,18]))