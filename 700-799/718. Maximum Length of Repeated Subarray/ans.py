from typing import List, Optional
import heapq, math, random
from collections import defaultdict, deque, Counter
from bisect import bisect_left

# class Solution:
    # def findLength(self, nums1: List[int], nums2: List[int]) -> int:
    #     m,n = len(nums1), len(nums2)
        
    #     # dp[i][j] = max len ending at nums1[i], nums2[j]
    #     dp = [[0]*n for _ in range(m)]
    #     maxLen = 0
        
    #     for i in range(m):
    #         for j in range(n):
    #             if nums1[i]==nums2[j]:
    #                 dp[i][j] = 1
    #                 if i-1>=0 and j-1>=0:
    #                     dp[i][j] += dp[i-1][j-1]
    #                 maxLen = max(maxLen, dp[i][j])
    #     return maxLen
    
class Solution(object):
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        if len(nums1)>len(nums2):
            nums1,nums2 = nums2, nums1
        m,n = len(nums1), len(nums2)
        maxLen = 0
        
        for move in range(m+n):
            countContinue = 0
            overlapLeft = max(m, move)
            overlapRight = min(m+n, move+m)
            for i in range(overlapLeft, overlapRight):
                if nums1[i-move]==nums2[i-m]:
                    countContinue+=1
                    maxLen = max(maxLen, countContinue)
                else:
                    countContinue = 0
        return maxLen

s = Solution()
print(s.findLength([1,3,2,5],[3,2,5,1]))
print(s.findLength([1,3,2,5],[3,2,5]))
print(s.findLength([1,3,2,5],[3,2]))
print(s.findLength([1,3,2,5],[5,3,2]))