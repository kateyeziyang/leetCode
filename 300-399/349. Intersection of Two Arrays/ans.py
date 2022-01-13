from typing import List, Optional
import heapq, math
from collections import defaultdict, deque,Counter
from bisect import bisect_left

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if len(nums2)<len(nums1):
            nums1,nums2=nums2,nums1
        nums1.sort()
        nums2.sort()
        m,n = len(nums1),len(nums2)
        p,q = 0,0
        ans = []
        while p<m and q<n:
            if nums1[p]==nums2[q]:
                if not ans or ans[-1]!=nums1[p]:
                    ans.append(nums1[p])
                p,q = p+1,q+1
            elif nums1[p]<nums2[q]:
                p += 1
            else:
                q += 1
        return ans
                

# class Solution:
#     def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
#         if len(nums2)<len(nums1):
#             nums1,nums2=nums2,nums1
#         set1 = set(nums1)
#         set2 = set(nums2)
#         return set1.intersection(set2)

s = Solution()
s.intersection([4,9,5],[9,4,9,8,4])