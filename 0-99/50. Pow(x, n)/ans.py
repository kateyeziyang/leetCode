from typing import List, Optional
import heapq, math
from collections import defaultdict, deque,Counter
from bisect import bisect_left

class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n<=3: return x**n
        if n<0:
            x = 1/x
            n = -n
        ans = 1
        curProd = x
        i = n
        while i:
            if i%2:
                ans *= curProd
            curProd *= curProd
            i //= 2
        return ans

# class Solution:
#     def myPow(self, x: float, n: int) -> float:
#         def helper(i):
#             if i<=2:
#                 return x**i
#             tmp = helper(i//2)**2 * x**(i%2)
#             return helper(i//2)**2 * x**(i%2)
#         return helper(n)

s = Solution()
# print(s.myPow(2.1,3),2.1**3)
# print(s.myPow(2,-5),2**-5)
s.myPow(2,19)