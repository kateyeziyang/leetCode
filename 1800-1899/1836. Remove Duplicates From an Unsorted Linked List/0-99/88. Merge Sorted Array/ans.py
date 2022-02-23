from typing import List, Optional
import heapq, math
from collections import defaultdict, deque,Counter
from bisect import bisect_left

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i,j=m-1,n-1
        loc = m+n-1
        while i>=0 and j>=0:
            if nums1[i]>=nums2[j]:
                nums1[loc]=nums1[i]
                loc,i=loc-1,i-1
            else:
                nums1[loc]=nums2[j]
                loc,j=loc-1,j-1
        if j>=0:
            nums1[0:j+1] = nums2[0:j+1]
        return

s = Solution()
nums1 = [1,2,3,0,0,0]
nums2 = [2,5,6]
s.merge(nums1, 3, nums2, 3)
print(nums1)