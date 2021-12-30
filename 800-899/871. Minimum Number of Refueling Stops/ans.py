from typing import List, Optional
import heapq, math
from collections import defaultdict, deque
from bisect import bisect_left

class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        if startFuel >= target:
            return 0
        n = len(stations)
        heap = []
        i = 0
        for s,f in stations:
            if s > startFuel:
                break
            heapq.heappush(heap,-f)
            i += 1
        curFuel = startFuel
        c = 0
        while curFuel < target:
            c += 1
            if not heap:
                return -1
            curFuel += -heapq.heappop(heap)
            for j in range(i,n):
                if stations[j][0] > curFuel:
                    break
                heapq.heappush(heap,-stations[j][1])
                i += 1
        return c
            

# class Solution:
#     def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
#         stations = [[0,0]]+stations
#         def mrs(loc,fuel):
#             if stations[loc][0]+fuel>=target:
#                 return 0
#             if fuel<0:
#                 return float("inf")
#             if loc == len(stations)-1:
#                 if stations[loc][0]+fuel+stations[loc][1]<target:
#                     return float("inf")
#                 return 1
#             dist = stations[loc+1][0]-stations[loc][0]
#             mrsNotFuel = mrs(loc+1,fuel-dist)
#             mrsFuel = mrs(loc+1,fuel-dist+stations[loc][1])
#             if mrsNotFuel == float("inf") and mrsFuel == float("inf"):
#                 return float("inf")
#             return min(mrsNotFuel,mrsFuel+1)
#         ans = mrs(0,startFuel)
#         if ans == float("inf"):
#             return -1
#         return ans

"""
goal: all (including used) fuels exceed target amount
must consider all stations w/ position <= startfuel, whether to take each one

1. DP
start from end, move backwords, track needed fuels
state (loc, fuel)

2. Jump array
"""

s = Solution()
assert s.minRefuelStops(target = 100, startFuel = 10, stations = [[10,60],[20,30],[30,30],[60,40]])==2
assert s.minRefuelStops(100,50,[[50,50]])==1
assert s.minRefuelStops(100,1,[[10,100]])==-1
assert s.minRefuelStops(100,50,[[25,25],[50,50]])==1