from typing import List, Optional
import heapq, math
from collections import defaultdict, deque
from bisect import bisect_left

class Solution:
    # def findItinerary(self, tickets):
    #     targets = defaultdict(list)
    #     for a, b in sorted(tickets)[::-1]:
    #         targets[a] += b,
    #     route, stack = [], ['JFK']
    #     while stack:
    #         while targets[stack[-1]]:
    #             stack += targets[stack[-1]].pop(),
    #         route += stack.pop(),
    #     return route[::-1]

    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        g = defaultdict(list)
        tickets.sort(reverse=True)
        for dep,arr in tickets:
            g[dep] += arr,
        it = []
        st = deque(["JFK"])
        while st:
            while g[st[-1]]:
                st += g[st[-1]].pop(),
            it += st.pop(),
        return it[::-1]

s = Solution()
assert s.findItinerary(tickets = [["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]])==["JFK","MUC","LHR","SFO","SJC"]
assert s.findItinerary(tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]])==["JFK","ATL","JFK","SFO","ATL","SFO"]
assert s.findItinerary([["JFK","KUL"],["JFK","NRT"],["NRT","JFK"]])