from typing import List
import heapq
from collections import defaultdict, deque

# class Solution:
#     def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
#         q = deque()
        
#         def cleanup(i):
#             if q and q[0]<=i-k:
#                 q.popleft()
            
#             while q and nums[q[-1]]<=nums[i]:
#                 q.pop()
            
#             q.append(i)
        
#         maxK = nums[0]
#         for i in range(k):
#             cleanup(i)
#             if nums[i]>maxK:
#                 maxK = nums[i]
        
#         ans = [maxK]
#         for i in range(k, len(nums)):
#             cleanup(i)
#             ans.append(nums[q[0]])
#         return ans

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        ans = [0] * n
        dQueue = deque()

        for i in range(n):
            while dQueue and dQueue[-1][0] <= nums[i]:
                dQueue.pop()
            if dQueue and dQueue[0][1] <= i-k:
                dQueue.popleft()
            dQueue.append([nums[i],i])
            ans[i] = dQueue[0][0]
        
        return ans[k-1:]


s = Solution()
print(s.maxSlidingWindow(nums = [1,3,-1,-3,5,3,6,7], k = 3))
"""
length k max heap, O(n log k)
"""