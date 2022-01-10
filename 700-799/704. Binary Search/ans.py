from typing import List, Optional
import heapq, math
from collections import defaultdict, deque,Counter
from bisect import bisect_left

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        l,r = 0,n-1

        while l<=r:
            mid = (l+r)//2
            nbr = nums[mid]
            if nbr==target:
                return mid
            elif nbr>target:
                r = mid-1
            else:
                l = mid+1
        return -1

s = Solution()
assert s.search(nums = [-1,0,3,5,9,12], target = 9)==4