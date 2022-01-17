from typing import List, Optional
import heapq, math, random
from collections import defaultdict, deque, Counter
from bisect import bisect_left

class Solution:
    def maxLength(self, ribbons: List[int], k: int) -> int:
        def canCutK(ribLen):
            count = 0
            for rib in ribbons:
                count += rib//ribLen
                if count >= k:
                    return True
            return False
        l,r = 1, max(ribbons)
        ans = 0

        while l<=r:
            mid = (l+r)//2
            if canCutK(mid):
                ans = mid
                l = mid+1
            else:
                r = mid-1
        return ans

s = Solution()