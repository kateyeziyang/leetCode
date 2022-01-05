from typing import List, Optional
import heapq, math
from collections import defaultdict, deque
from bisect import bisect_left

class Solution:
    def uniqueLetterString(self, s: str) -> int:
        n = len(s)
        lmap = {}
        count = 0
        for i,c in enumerate(s):
            if c not in lmap:
                lmap[c] = [-1,i]
            else:
                l,r = lmap[c]
                count += (r-l)*(i-r)
                lmap[c] = [r,i]
        for k in lmap:
            l,r = lmap[k]
            count += (r-l)*(n-r)
        return count

# class Solution:
#     def uniqueLetterString(self, s: str) -> int:
#         lmap = defaultdict(list)
#         n = len(s)
#         for i,c in enumerate(s):
#             lmap[c].append(i)
#         count = 0
#         for k in lmap:
#             for i,v in enumerate(lmap[k]):
#                 left,right = -1, n
#                 if i != 0:
#                     left = lmap[k][i-1]
#                 if i != len(lmap[k])-1:
#                     right = lmap[k][i+1]
#                 nums = right-left-1
#                 count += (v-left)*(right-v)
#         return count

s = Solution()
assert s.uniqueLetterString("LEETCODE")==92