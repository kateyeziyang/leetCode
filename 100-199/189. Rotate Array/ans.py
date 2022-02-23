from typing import List, Optional
import heapq, math, random
from collections import defaultdict, deque, Counter
from bisect import bisect_left

# [4,5,1,2,3], k = 2
# i, (i+k)%n
# [0,..,n-1] n-k ~ n-1
# []

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        if not nums or k%n==0: return 
        def reverse(arr,l,r): # included both points
            mid = (l+r)//2 # l=0,r=2, mid 1; l=0,r=3,mid 1
            for i in range(l,mid+1):
                arr[i],arr[r-(i-l)] = arr[r-(i-l)],arr[i]
        k %= n
        nums.reverse()
        reverse(nums,0,k-1)
        reverse(nums,k,n-1)

# [4,5,1,2,3]        

s = Solution()