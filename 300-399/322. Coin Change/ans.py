from typing import List, Optional
import heapq, math, random
from collections import defaultdict, deque, Counter
from bisect import bisect_left

# # BFS
# class Solution:
#     def coinChange(self, coins: List[int], amount: int) -> int:
#         if amount == 0: return 0
#         coins = sorted(list(set(coins)))
#         i = 1
#         curmin = 0
#         visited = set([0])
#         q = deque([0])
#         while curmin < amount:
#             curmin = float('inf')
#             for _ in range(len(q)):
#                 v = q.popleft()
#                 for c in coins:
#                     if v+c not in visited:
#                         if v+c == amount:
#                             return i
#                         visited.add(v+c)
#                         q.append(v+c)
#                         curmin = min(curmin, v+c)
#             i += 1
#         return -1

# topdown
# class Solution:
#     def coinChange(self, coins: List[int], amount: int) -> int:
#         if amount == 0: return 0
#         self.coins = sorted(list(set(coins)), reverse=True)
#         result = self.recursion(amount)
        
#         return result if result != float('inf') else -1
    
#     @lru_cache
#     def recursion(self, amount):
#         if amount == 0: return 0
#         if amount < 0: return float('inf')
#         minAmount = float('inf')
#         for c in self.coins:
#             minAmount = min(minAmount, 1+self.recursion(amount-c))
#         return minAmount

# bottom up
# class Solution:
#     def coinChange(self, coins: List[int], amount: int) -> int:
#         if amount == 0: return 0
#         coins = sorted(list(set(coins)))
#         dp = [float('inf')]*(amount+1)
#         dp[0] = 0
#         for i in range(1, amount+1):
#             for c in coins:
#                 idx = i-c
#                 if idx >= 0:
#                     dp[i] = min(dp[i], 1+dp[idx])
#         return dp[-1] if dp[-1] != float('inf') else -1

s = Solution()