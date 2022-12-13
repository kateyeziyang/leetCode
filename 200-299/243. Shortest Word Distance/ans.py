from typing import List, Optional
import heapq, math, random
from collections import defaultdict, deque, Counter
from bisect import bisect_left

class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        loc1,loc2 = float('-inf'),float('-inf')
        first1,first2=0,0
        ans = float('inf')

        for i,w in enumerate(wordsDict):
            if w==word1:
                if not first1: first1=i
                loc1 = i
                ans = min(ans,loc1-loc2)
            elif w==word2:
                if not first2: first2=i
                loc2 = i
                ans = min(ans,loc2-loc1)
        # ans = min(ans, [first1-loc2,first2-loc1])
        return ans

s = Solution()