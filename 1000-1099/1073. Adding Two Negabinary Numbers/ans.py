from typing import List, Optional
import heapq, math, random
from collections import defaultdict, deque, Counter
from bisect import bisect_left

class Solution:
    def addNegabinary(self, arr1: List[int], arr2: List[int]) -> List[int]:
        ans = self.arrToInt(arr1) + self.arrToInt(arr2)
        return self.baseNeg2(ans)
    
    def arrToInt(self, arr):
        return sum(((-2)**i)*v for i,v in enumerate(reversed(arr)))
    
    def baseNeg2(self, n: int) -> str:
        if n == 0: return [0]
        ans = []
        while n:
            a, b = divmod(n, -2)
            if b<0:
                a, b = a+1, b+2
            ans.append(b)
            n = a
        return ans[::-1]

s = Solution()
print(s.arrToInt([1,1,0,1]))
print(s.addNegabinary(arr1 = [1,1,1,1,1], arr2 = [1,0,1]))