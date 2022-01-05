from typing import List, Optional
import heapq, math
from collections import defaultdict, deque
from bisect import bisect_left

# Definition for an Interval.
class Interval:
    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end

class Solution:
    def employeeFreeTime(self, schedule):
        sch = [[s.start,s.end] for p in schedule for s in p]
        sch.sort(key=lambda s:s[0])
        n = len(sch)
        cur,idx = 0,1
        ans = []
        while idx < n:
            if sch[idx][0] > sch[cur][1]:
                ans.append(Interval(sch[cur][1],sch[idx][0]))
            cur = idx if sch[cur][1] < sch[idx][1] else cur
            idx += 1
        return ans

"""
https://leetcode.com/problems/employee-free-time/discuss/170551/Simple-Python-9-liner-beats-97-(with-explanation)
def employeeFreeTime(self, schedule):
    ints = sorted([i for s in schedule for i in s], key=lambda x: x.start)
    res, pre = [], ints[0]
    for i in ints[1:]:
        if i.start <= pre.end and i.end > pre.end:
            pre.end = i.end
        elif i.start > pre.end:
            res.append(Interval(pre.end, i.start))
            pre = i
    return res
    """


s = Solution()