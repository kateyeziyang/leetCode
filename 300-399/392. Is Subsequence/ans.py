from typing import List, Optional
import heapq, math, random
from collections import defaultdict, deque, Counter
from bisect import bisect_left

# brute force
# class Solution:
    # def isSubsequence(self, s: str, t: str) -> bool:
    #     if not s: return True
    #     if not t: return False
    #     if s[0]==t[0]:
    #         return self.isSubsequence(s[1:], t[1:]) or self.isSubsequence(s, t[1:])
    #     return self.isSubsequence(s, t[1:])

# implicit memo
# class Solution:
#     def __init__(self):
#         self.dp = {}
    
#     def isSubsequence(self, s: str, t: str) -> bool:
#         if not s: return True
#         if not t: return False
#         if (s,t) in self.dp:
#             return self.dp[(s,t)]
#         result = self.isSubsequence(s, t[1:]) or (self.isSubsequence(s[1:],t[1:]) if s[0]==t[0] else False) # It's my first time knowing that OR has higher precedence than logical OR
#         self.dp[(s,t)] = result
#         return result

# explicit memo
# class Solution:
    
#     def isSubsequence(self, s: str, t: str) -> bool:
#         # print("s:{} t:{}".format(s,t))
#         if not s: return True
#         if not t: return False
#         m,n = len(s), len(t)
#         if m > n: return False
#         if m == n: return s==t # does this help? 
#         dp = [[False] * (n+1) for _ in range(min(m+1,n+1))]
#         # dp[i][j] - s[:i] is subseq of t[:j]
#         for j in range(n+1):
#             dp[0][j] = True
#         for j in range(1,n+1):
#             for i in range(1,min(m+1,j+1)):
#                 dp[i][j] = dp[i][j-1] or (dp[i-1][j-1] if s[i-1]==t[j-1] else False)
#             if dp[m][j]: return True
#         return False

# 1d dp
# class Solution:
#     def isSubsequence(self, s: str, t: str) -> bool:
#         # print("s:{} t:{}".format(s,t))
#         if not s: return True
#         if not t: return False
#         m,n = len(s), len(t)
#         if m > n: return False
#         if m == n: return s==t # does this help? 
#         dp = [0] * (n+1)
#         for i in range(1, n+1):
#             k = dp[i-1]
#             if k==m: return True
#             if s[k] == t[i-1]:
#                 dp[i] = k+1
#             else:
#                 dp[i] = k
#         return dp[n]==m

# pointer
# class Solution:
#     def isSubsequence(self, s: str, t: str) -> bool:
#         # print("s:{} t:{}".format(s,t))
#         if not s: return True
#         if not t: return False
#         m,n = len(s), len(t)
#         if m > n: return False
#         if m == n: return s==t # does this help? 
#         p = 0
#         for i in range(n):
#             if s[p]==t[i]:
#                 p += 1
#                 if p==m:
#                     ret

s = Solution()
s.isSubsequence("abc","ahbgdc")