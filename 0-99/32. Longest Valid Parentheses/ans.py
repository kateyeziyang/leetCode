from typing import List, Optional
import heapq, math
from collections import defaultdict, deque,Counter
from bisect import bisect_left

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        st = deque([-1])
        ans = count = 0
        for i,c in enumerate(s):
            if c=="(":
                st.append(i)
                count += 1
            else:
                st.pop()
                count += 1
                if not st:
                    st.append(i)

# there is only one type of bracket, anyway...

# class Solution:
#     def longestValidParentheses(self, s: str) -> int:
#         st = deque()
#         res = 0
#         count = 0
#         parMap = {"}":"{",")":"(","]":"["}
#         countMap = {0:[-1,-1]}
#         for i,c in enumerate(s):
#             if c in parMap:
#                 if not st or st[-1]!=parMap[c]:
#                     st.clear()
#                     for count,val in countMap.items():
#                         if val[1]!=-1:
#                             res = max(res,val[1]-val[0])
#                     countMap = {0:[i,-1]}
#                     continue
#                 res = max(res,countMap[len(st)][1]-countMap[len(st)][0])
#                 countMap[len(st)][0],countMap[len(st)][1] = -1,-1
#                 st.pop()
#                 count += 1
#                 countMap[len(st)][1] = i
#             else:
#                 st.append(c)
#                 if len(st) not in countMap or countMap[len(st)][0]==-1:
#                     countMap[len(st)] = [i,-1]
#         for count,val in countMap.items():
#             if val[1]!=-1:
#                 res = max(res,val[1]-val[0])
#         return res

s = Solution()
assert s.longestValidParentheses("(()))((())()")==6
assert s.longestValidParentheses("()(()")==2
assert s.longestValidParentheses(")()())")==4