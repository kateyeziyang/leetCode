from typing import List, Optional
import heapq, math
from collections import defaultdict, deque
from bisect import bisect_left

class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int: # nums[l:r] will sum < k, nums[l:r+1] will sum >= k
        q = deque([[0,0]])
        count = 0
        res = float("inf")
        for i,num in enumerate(nums):
            count += num
            while q and count <= q[-1][1]:
                q.pop()
            while q and count - q[0][1] >= k:
                res = min(res,i+1-q.popleft()[0])
            q.append([i+1,count])
        return res if res != float("inf") else -1
        

# class Solution:
#     def shortestSubarray(self, nums: List[int], k: int) -> int: # nums[l:r] will sum < k, nums[l:r+1] will sum >= k
#         n = len(nums)
#         ans = n
#         totalcount = 0
#         for i in range(n):
#             totalcount += nums[i]
#             partialcount = totalcount
#             for j in range(i,max(-1,i-ans+1),-1):
#                 partialcount -= nums[j]
#                 if totalcount-partialcount >= k:
#                     ans = i-j+1
#                     break
            
#         if ans == n and totalcount < k:
#             ans = -1
#         return ans


s = Solution()
assert s.shortestSubarray([1],1)==1
assert s.shortestSubarray([1,2],4)==-1
assert s.shortestSubarray([2,-1,2],3)==3