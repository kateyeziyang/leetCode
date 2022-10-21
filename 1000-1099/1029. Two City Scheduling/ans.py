from typing import List, Optional
import heapq, math, random
from collections import defaultdict, deque, Counter
from bisect import bisect_left
from itertools import accumulate

# class Solution:
#     def twoCitySchedCost(self, costs: List[List[int]]) -> int:
#         ans = float('inf')
#         n = len(costs)//2
#         q = deque([[0,0]])
#         i = 0
#         acosts = [x[0] for x in costs]
#         bcosts = [x[1] for x in costs]
#         preACosts = list(accumulate(acosts))
#         preBCosts = list(accumulate(bcosts))
#         ASum = sum(acosts)
#         BSum = sum(bcosts)
#         while i < 2*n:
#             # if i == 2*n:
#             #     for _ in range(len(q)):
#             #         ans = min(ans, q.popleft()[1])
#             #     break
#             for _ in range(len(q)):
#                 numA, cost = q.popleft()
#                 numB = i - numA
#                 if numA == n:
#                     cost += BSum-preBCosts[i-1]
#                     ans = min(ans, cost)
#                     continue
#                 elif numB == n:
#                     cost += ASum-preACosts[i-1]
#                     ans = min(ans, cost)
#                     continue
#                 q.append([numA+1, cost+costs[i][0]])
#                 q.append([numA, cost+costs[i][1]])
#             i += 1
#         return ans

class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        costs.sort(key=lambda x: x[0]-x[1])
        n = len(costs)//2
        return sum([x[0] for x in costs[:n]]) + sum([x[1] for x in costs[n:]])

# [[0,1],[1,100],[]]
# [[0, 200], [100, 200], [0, 0], [0, 0]]
s = Solution()