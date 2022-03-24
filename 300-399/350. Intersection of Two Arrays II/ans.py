from typing import List, Optional
import heapq, math, random
from collections import defaultdict, deque, Counter
from bisect import bisect_left

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        c1 = Counter(nums1)
        c2 = Counter(nums2)
        if len(c2)<len(c1):
            c1,c2 = c2,c1
        ans = []
        for k,v in c1.items():
            if k in c2:
                ans.extend([k]*min(v,c2[k]))
        return ans

s = Solution()