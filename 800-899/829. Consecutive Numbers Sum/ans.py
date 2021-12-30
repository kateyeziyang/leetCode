from typing import List
import heapq,math
from collections import defaultdict, deque

"""
n = x + ... + (x+k-1)
= (2x+k-1)*k/2
=xk+k(k-1)/2
x=n/k-(k-1)/2 >= 1 -- needs to be an positive integer (2n-k**2+k)/2k
n/k-(k+1)/2 >= 0
2n >= k^2+k
2n+1/4 >= (k+1/2)^2
|k+1/2| <= sqrt(2n+1/4) because k is of cource bigger than -1/2, can take absolute off
k <= sqrt(2n+1/4)-1/2
try k from 0 to above bound
test if x is an integer
"""

class Solution:
    def consecutiveNumbersSum(self, n: int) -> int:
        bound = math.floor((2*n+1/4)**0.5-0.5)
        count = 1
        for k in range(2,bound+1):
            if (2*n-k**2+k)%(2*k)==0:
                count += 1
        return count

s = Solution()