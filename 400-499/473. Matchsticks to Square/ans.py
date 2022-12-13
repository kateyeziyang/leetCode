from typing import List, Optional
import heapq, math, random
from collections import defaultdict, deque, Counter
from bisect import bisect_left

class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        perimeter = sum(matchsticks)
        if perimeter % 4 != 0: return False
        sideLength = perimeter // 4
        if list(filter(lambda x: x > sideLength, matchsticks)): return False
        matchsticks.sort(reverse=True)

        sticks = [sideLength] * 4
        x = 0

        def backtrack(idx):
            nonlocal x
            x += 1
            if x % 1000 == 0:
                print("hey")
            if all([True if x == 0 else False for x in sticks]):
                return True
            if idx == len(matchsticks): return False

            val = matchsticks[idx]
            for j in range(4):
                if val <= sticks[j]:
                    sticks[j] -= val
                    if backtrack(idx + 1): return True
                    sticks[j] += val
            return False
        
        return backtrack(0)

s = Solution()
# print(s.makesquare([5969561,8742425,2513572,3352059,9084275,2194427,1017540,2324577,6810719,8936380,7868365,2755770,9954463,9912280,4713511]))
print(s.makesquare([14,10,10,10,10,10,10,10,10,10,10,10,8,9,19]))