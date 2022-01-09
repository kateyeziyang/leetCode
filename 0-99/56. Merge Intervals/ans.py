from typing import List, Optional
import heapq, math
from collections import defaultdict, deque
from bisect import bisect_left

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        ans = []
        sortedIntervals = sorted(intervals)
        left,right = sortedIntervals[0]
        for interval in sortedIntervals:
            s,e = interval
            if s > right:
                ans.append([left,right])
                left,right = s,e
            else:
                right = max(right,e)
        ans.append([left,right])
        return ans

s = Solution()
assert s.merge([[1,3],[2,6],[8,10],[15,18]])==[[1,6],[8,10],[15,18]]
assert s.merge([[1,4],[4,5]])==[[1,5]]