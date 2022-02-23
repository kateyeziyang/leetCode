from typing import List, Optional
import heapq, math
from collections import defaultdict, deque, Counter
from bisect import bisect_left

class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        l,r = 0,n-1
        ans = 0
        while l<r:
            ans = max(ans,min(height[l],height[r])*(r-l))
            if height[l]<height[r]:
                l += 1
            else:
                r -= 1
        return ans

s = Solution()
print(s.maxArea(height = [1,8,6,2,5,4,8,3,7]))