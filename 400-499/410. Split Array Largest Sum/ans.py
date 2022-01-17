from typing import List, Optional
import heapq, math
from collections import defaultdict, deque,Counter
from bisect import bisect_left

# https://leetcode.com/problems/split-array-largest-sum/solution/
# class Solution:
#     def splitArray(self, nums: List[int], m: int) -> int:
#         n = len(nums)
#         memo = [[0] * (m + 1) for _ in range(n)]
        
#         # Create a prefix sum array of nums.
#         prefix_sum = [0] + list(itertools.accumulate(nums))
        
#         for subarray_count in range(1, m + 1):
#             for curr_index in range(n):
#                 # Base Case: If there is only one subarray left, then all of the remaining numbers
#                 # must go in the current subarray. So return the sum of the remaining numbers.
#                 if subarray_count == 1:
#                     memo[curr_index][subarray_count] = prefix_sum[n] - prefix_sum[curr_index]
#                     continue

#                 # Otherwise, use the recurrence relation to determine the minimum largest subarray sum
#                 # between curr_index and the end of the array with subarray_count subarrays remaining.
#                 minimum_largest_split_sum = prefix_sum[n]
#                 for i in range(curr_index, n - subarray_count + 1):
#                     # Store the sum of the first subarray.
#                     first_split_sum = prefix_sum[i + 1] - prefix_sum[curr_index]

#                     # Find the maximum subarray sum for the current first split.
#                     largest_split_sum = max(first_split_sum, memo[i + 1][subarray_count - 1])

#                     # Find the minimum among all possible combinations.
#                     minimum_largest_split_sum = min(minimum_largest_split_sum, largest_split_sum)

#                     if first_split_sum >= minimum_largest_split_sum:
#                         break
            
#                 memo[curr_index][subarray_count] = minimum_largest_split_sum
        
#         return memo[0][m]

# DP: for each index, decide where to spend next split
# bottom-up: start from only 1 splitted array
# very important: prune the search by using right sum
# class Solution:
#     def splitArray(self, nums: List[int], m: int) -> int:
#         n = len(nums)
#         if m>=n: return max(nums)
#         dp = [[float("inf")]*m for _ in range(n)]
#         dp[0][0] = nums[0]
#         for i in range(1,n):
#             dp[i][0] = nums[i]+dp[i-1][0]
#         for i in range(1,n):
#             for j in range(1,min(i+1,m)):
#                 # if j>i:
#                 #     dp[i][j] = max(dp[i-1][j-1],nums[i])
#                 #     break
#                 minSplit = max(dp[i][0]-dp[i-1][0],dp[i-1][j-1])
#                 for k in range(i-2,j-2,-1):
#                     rightSum = dp[i][0]-dp[k][0]
#                     minSplit = min(minSplit, max(rightSum,dp[k][j-1]))
#                     if rightSum >= minSplit:
#                         break
#                 dp[i][j] = minSplit
#         return dp[-1][-1]

class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        def canSplit(k):
            arrCount = 1
            curSubSum = 0
            for x in nums:
                if x>k or arrCount>m:
                    return False
                if curSubSum+x>k:
                    arrCount += 1
                    curSubSum = x
                else:
                    curSubSum += x
            return arrCount<=m
        total = sum(nums)
        r = total
        l = 0
        while l<r:
            mid = (l+r)//2
            if canSplit(mid):
                r = mid
            else:
                l = mid+1
        return r


s = Solution()
print(s.splitArray([1,2,3,4,5,6],2))
print(s.splitArray([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,50,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,100,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,150,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,200,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,250,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,300,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,350,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,400,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,450,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,500,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,550,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,600,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,650,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,700,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,750,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,800,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,850,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,900,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,950,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],50))
print(s.splitArray([2,3,1,2,4,3],5))