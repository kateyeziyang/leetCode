from typing import List, Optional
import heapq, math, random
from collections import defaultdict, deque, Counter
from bisect import bisect_left

"""
recursion: build DP for length 1~maxLength

Suppose we know number of good string start with 0/1 of all binary strings of length 1 ~ l-1.
The number of good strings start with 1 of all binary strings of length l can be calculated as such:
(N * oneGroup) of "1", concatenated by any good strings start with 0 of length l-(N*oneGroup)
"""

class Solution:
    def goodBinaryStrings(self, minLength: int, maxLength: int, oneGroup: int, zeroGroup: int) -> int:
        goodCounts = [0] * (maxLength + 1)
        goodCounts[0] = 1
        modNumber = (10**9+7)

        for i in range(min(oneGroup, zeroGroup), maxLength+1):
            goodCounts[i] = (goodCounts[i-oneGroup]+goodCounts[i-zeroGroup])%modNumber
        return sum(goodCounts[minLength:])%modNumber

"""
class goodCount:
    goodStrStartsWith0 = 0
    goodStrStartsWith1 = 0

class Solution:
    def goodBinaryStrings(self, minLength: int, maxLength: int, oneGroup: int, zeroGroup: int) -> int:
        goodCounts = [goodCount() for _ in range(maxLength + 1)]
        goodCounts[0].goodStrStartsWith1 = 1
        goodCounts[0].goodStrStartsWith0 = 1

        for i in range(min(oneGroup, zeroGroup), maxLength+1):
            goodCounts[i].goodStrStartsWith0 = sum(goodCounts[i-j*zeroGroup].goodStrStartsWith1 for j in range(1, i//zeroGroup+1))
            goodCounts[i].goodStrStartsWith1 = sum(goodCounts[i-j*oneGroup].goodStrStartsWith0 for j in range(1, i//oneGroup+1))
        return sum(goodCount.goodStrStartsWith0 + goodCount.goodStrStartsWith1 for goodCount in goodCounts[minLength:maxLength+1]) % (10**9+7)
"""
s = Solution()
tests = [
    [3,3,3,1],
    [3,3,3,2],
    [3,3,3,4],
    [3,3,2,2],
    [4,4,2,2],
    [4,4,1,2],
    [5,5,2,3],
    [2,3,1,2] # 11,00, 100,001,111
]

for t in tests:
    a, b, c, d = t
    print(s.goodBinaryStrings(a, b, c, d))