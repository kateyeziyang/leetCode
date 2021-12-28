from typing import List
import heapq
from collections import defaultdict, deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque()
        
        def cleanup(i):
            if q and q[0]<=i-k:
                q.popleft()
            
            while q and nums[q[-1]]<=nums[i]:
                q.pop()
            
            q.append(i)
        
        maxK = nums[0]
        for i in range(k):
            cleanup(i)
            if nums[i]>maxK:
                maxK = nums[i]
        
        ans = [maxK]
        for i in range(k, len(nums)):
            cleanup(i)
            ans.append(nums[q[0]])
        return ans

s = Solution()
print(s.maxSlidingWindow(nums = [1,3,-1,-3,5,3,6,7], k = 3))
"""
length k max heap, O(n log k)
"""