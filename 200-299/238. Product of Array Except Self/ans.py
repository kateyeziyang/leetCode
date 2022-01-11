from typing import List, Optional
import heapq, math
from collections import defaultdict, deque,Counter
from bisect import bisect_left

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        def helper(arr,i):
            nb = i-1 if i%2 else i+1
            l = len(arr)
            newarr = [1]*(l//2)
            for i in range(0,len(newarr)):
                newarr[i] = arr[2*i]*arr[2*i+1]
            if l%2:
                newarr.append(arr[-1])
            return arr[nb] * helper(newarr,i//2)
        l = len(nums)
        ans = [1]*l
        for i,x in enumerate(ans):
            ans[i]  = helper(nums,i)

s = Solution()