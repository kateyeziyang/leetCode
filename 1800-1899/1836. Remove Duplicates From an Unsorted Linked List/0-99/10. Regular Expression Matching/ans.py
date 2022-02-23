from typing import List, Optional
import heapq, math
from collections import defaultdict, deque
from bisect import bisect_left

class Solution:
    def isMatch(self, s: str, p: str) -> bool: # dp[i][j]: True if s[i:] matches p[j:]
        m,n = len(s),len(p)
        dp = [[False]*(n+1) for _ in range(m+1)]

        dp[m][n] = True
        # empty string matches ()*()*
        for j in range(n-2,-1,-2):
            if p[j+1] != "*": break
            dp[m][j] = dp[m][j+2]
        
        for i in range(m-1,-1,-1):
            for j in range(n-1,-1,-1):
                if p[j+1:j+2] == "*":
                    dp[i][j] = dp[i][j+2]
                    if s[i]==p[j] or p[j]==".":
                        dp[i][j] |= dp[i+1][j]
                else:
                    dp[i][j] = dp[i+1][j+1] and (s[i]==p[j] or p[j]==".")
        return dp[0][0]



"""
Feeling I'm either a fool or a genius to write this code...
oh, it's called NFA?! Nondeterministic Finite Automata
"""

# class Solution:
#     def isMatch(self, s: str, p: str) -> bool:
#         def removeRepeatStars(s):
#             news = list(s)
#             i = 0
#             while i < len(news)-3:
#                 if news[i+1]=="*" and news[i+3]=="*":
#                     if news[i]==news[i+2] or news[i]==".":
#                         news = news[:i+2]+news[i+4:]
#                     elif news[i+2]==".":
#                         news = news[:i]+news[i+2:]
#                     else:
#                         i += 2
#                 else:
#                     i+=1
#             return news
#         p = removeRepeatStars(p)
#         if (not s) and p:
#             for i in range(0,len(p)-1,2):
#                 if i+1 >= len(p) or p[i+1]!="*":
#                     return False
#             return True
#         if not p:
#             return s==""
#         q = deque([0])
#         for i,c in enumerate(p):
#             if not q:
#                 return False
#             if c == "*": continue
#             for _ in range(len(q)):
#                 idx = q.popleft()
#                 if idx == len(s):
#                     cont = False
#                     for id in range(i,len(p),2):
#                         if id+1>=len(p) or p[id+1]!="*":
#                             cont = True
#                     if cont:
#                         continue
#                     return True
#                 if i != len(p)-1:
#                     if p[i+1] == "*":
#                         if c != ".":
#                             q.append(idx)
#                             if s[idx]==c:
#                                 j = 1
#                                 while idx+j<len(s) and s[idx+j]==c:
#                                     q.append(idx+j)
#                                     j += 1
#                                 q.append(idx+j)
#                         else:
#                             q.extend(range(idx,len(s)+1))
#                         continue
#                 if c == "."or c == s[idx]:
#                     q.append(idx+1)
#         if not q:
#             return False
#         while q:
#             idx = q.popleft()
#             if idx == len(s):
#                 return True
#         return False

s = Solution()
assert s.isMatch("","")==True
assert s.isMatch("ABC","")==False
assert s.isMatch("","ABC")==False
assert s.isMatch("ABC","ABC")==True
assert s.isMatch("",".*.*a*")==True
assert s.isMatch("","a*a*.*a*")==True
assert s.isMatch("","aa*")==False
assert s.isMatch("a","aa*")==True
assert s.isMatch("aaa","aa*")==True
assert s.isMatch("aabba","a*bb")==False
assert s.isMatch("aabba","a*bba")==True
assert s.isMatch("aabba","a*b.*")==True
assert s.isMatch("aabba","a*bba*")==True
assert s.isMatch("a","agesgse")==False
assert s.isMatch("aab","c*a*b")==True
assert s.isMatch("mississippi","mis*is*p*.")==False
assert s.isMatch("ab",".*c")==False
assert s.isMatch("aaa","a*a")==True