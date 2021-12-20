from typing import List
from collections import defaultdict, deque

class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source == target:
            return 0
        stopBoards = defaultdict(list)
        for bus,route in enumerate(routes):
            for stop in route:
                stopBoards[stop].append(bus)
        
        q = deque([source])
        visitedBus = set()
        ans = 0
        while q:
            ans += 1
            numStop = len(q)

            for i in range(numStop):
                curStop = q.popleft()
                for bus in stopBoards[curStop]:
                    if bus not in visitedBus:
                        visitedBus.add(bus)
                        for stop in routes[bus]:
                            if stop == target:
                                return ans
                            q.append(stop)
        return -1

s = Solution()
assert s.numBusesToDestination(routes = [[1,2,7],[3,6,7]], source = 1, target = 6) == 2
assert s.numBusesToDestination([[7,12],[4,5,15],[6],[15,19],[9,12,13]], source = 15, target = 12) == -1

"""
intuitive: graph
node is stop
edges come from routes
need to know start node,
from each node, we want to know all neighbor
dict of set

observation: there is no need to take a bus more than once
find least number of buses to take, is just the shortest path (number of levels) in BFS

it's interesting how you store bus in the map, rather than what stop is reachable. This save us from storing too many things.
Let's say number of stop is s, number of bus is b
for each popped stop, we spend some time on each bus that will stop by.
For each bus that is not visited, we add all stops in its routes to the queue. (this will take number of elements in routes time in total, but will be dominated).
O(s+s*b)
"""