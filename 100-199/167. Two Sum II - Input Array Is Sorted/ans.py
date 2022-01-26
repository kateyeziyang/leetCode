from typing import List, Optional
import heapq, math, random
from collections import defaultdict, deque, Counter
from bisect import bisect_left

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        l,r=0,n-1
        while l<r:
            cur = numbers[l]+numbers[r]
            if cur==target:
                return [l+1,r+1]
            elif cur<target:
                l+=1
            else:
                r-=1

s = Solution()