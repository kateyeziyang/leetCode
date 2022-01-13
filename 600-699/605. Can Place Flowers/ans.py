from typing import List, Optional
import heapq, math
from collections import defaultdict, deque, Counter
from bisect import bisect_left

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if n==0:
            return True
        for i,fl in enumerate(flowerbed):
            if (i==0 or not flowerbed[i-1]) and not flowerbed[i] and (i==len(flowerbed)-1 or not flowerbed[i+1]):
                n-=1
                flowerbed[i]=1
                if n==0:
                    return True
        return False

s = Solution()
s.canPlaceFlowers([1,0,0,0,1,0,0],2)