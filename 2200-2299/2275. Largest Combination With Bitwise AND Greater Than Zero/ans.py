from typing import List, Optional
import heapq, math, random
from collections import defaultdict, deque, Counter
from bisect import bisect_left

class Solution:
    def largestCombination(self, candidates: List[int]) -> int:
        numOnesOnSignificantDigit = defaultdict(int)

        for candidate in candidates:
            c = 0
            while candidate:
                if candidate&1:
                    numOnesOnSignificantDigit[c] += 1
                c += 1
                candidate >>= 1
        return max(numOnesOnSignificantDigit.values())

s = Solution()
print(s.largestCombination([16,17,71,62,12,24,14]))