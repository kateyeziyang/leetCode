from typing import List, Optional
import heapq, math
from collections import defaultdict, deque,Counter
from bisect import bisect_left

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        ans = 1
        hp = []
        openCount = 0
        for start,end in sorted(intervals,key=lambda x:x[0]):
            while hp and hp[0]<=start:
                heapq.heappop(hp)
                openCount -= 1
            heapq.heappush(hp,end)
            openCount += 1
            ans = max(ans,openCount)
        return ans

s = Solution()
assert s.minMeetingRooms([[0,30],[5,10],[5,8],[15,20]])==3
assert s.minMeetingRooms([[7,10],[2,4]])==1