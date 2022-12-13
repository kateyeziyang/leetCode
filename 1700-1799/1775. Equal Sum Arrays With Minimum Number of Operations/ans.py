from typing import List, Optional
import heapq, math, random
from collections import defaultdict, deque, Counter
from bisect import bisect_left

class Solution:
    def minOperations(self, nums1: List[int], nums2: List[int]) -> int:
        count1 = Counter(nums1)
        count2 = Counter(nums2)
        sum1, sum2 = sum(k*v for k,v in count1.items()), sum(k*v for k,v in count2.items())
        if sum1>sum2:
            sum1,sum2,count1,count2,nums1,nums2 = sum2,sum1,count2,count1,nums2,nums1
        target = sum2-sum1
        if target > (6*len(nums1)-sum1)+(sum2-len(nums2)): return False

        ans = 0
        for i in range(5,0,-1):
            if target <= 0: break
            numOps = min(-(target // -i),count1[6-i]+count2[i+1])
            target -= numOps*i
            ans += numOps

        return ans if ans>=0 else -1



s = Solution()