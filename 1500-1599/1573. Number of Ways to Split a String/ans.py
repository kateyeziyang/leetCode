from typing import List, Optional
import heapq, math, random
from collections import defaultdict, deque, Counter
from bisect import bisect_left
from math import comb

class Solution:
    def numWays(self, s: str) -> int:
        numOnes = s.count('1')
        if numOnes%3: return 0
        # special all 0
        if numOnes == 0:
            return comb(len(s)-1,2)

        numOnesPerPart = numOnes//3
        curOnes = 0
        possibleSecondLoc = possibleFirstLoc = 0
        i = 0
        while curOnes <= numOnesPerPart*2:
            c = s[i]
            if c=='1':
                curOnes += 1
            if curOnes == numOnesPerPart:
                possibleFirstLoc += 1
            elif curOnes == numOnesPerPart*2:
                possibleSecondLoc += 1
            i += 1
        return possibleFirstLoc * possibleSecondLoc%(10**9+7)

s = Solution()