from typing import List, Optional
import heapq, math
from collections import defaultdict, deque,Counter
from bisect import bisect_left

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left,right = [0]*n,[0]*n
        lbase,rbase=1,1
        for i in range(n):
            lbase *= nums[i]
            rbase *= nums[n-1-i]
            left[i] = lbase 
            right[n-1-i] = rbase
        ans = [0]*n
        ans[0] = right[1]
        ans[-1] = left[-2]
        for i in range(1,n-1):
            ans[i] = left[i-1]*right[i+1]
        return ans


s = Solution()