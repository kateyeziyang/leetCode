from typing import List, Optional
import heapq, math, random
from collections import defaultdict, deque, Counter
from bisect import bisect_left

# dict: key=mod 60, value=count of such songs
# iterate from 0 to 29, for each add min(dict[i],dict[60-i]) to total

class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        mods = defaultdict(int)
        for t in time:
            mods[t%60] += 1
        ans = 0
        for i in range(1,30):
            ans += mods[i]*mods[60-i]
        for i in [0,30]:
            ans += mods[i]*(mods[i]-1)//2
        return ans

s = Solution()