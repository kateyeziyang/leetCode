from typing import List, Optional
import heapq, math
from collections import defaultdict, deque
from bisect import bisect_left

# For each char, how many times it will be the unique character of a substring?
# find left and right starting from this location, left range * right range
# hash map stored seen chars
class Solution:
    def uniqueLetterString(self, s: str) -> int:
        lmap = {}
        ans = 0
        for i,c in enumerate(s):
            if c not in lmap:
                lmap[c] = [-1,i]
            else:
                ans += (lmap[c][1]-lmap[c][0])*(i-lmap[c][1])
                lmap[c][0],lmap[c][1] = lmap[c][1],i
        for l,r in lmap.values():
            ans += (r-l)*(len(s)-r)
        return ans

# class Solution:
#     def uniqueLetterString(self, s: str) -> int:
#         n = len(s)
#         lmap = {}
#         count = 0
#         for i,c in enumerate(s):
#             if c not in lmap:
#                 lmap[c] = [-1,i]
#             else:
#                 l,r = lmap[c]
#                 count += (r-l)*(i-r)
#                 lmap[c] = [r,i]
#         for k in lmap:
#             l,r = lmap[k]
#             count += (r-l)*(n-r)
#         return count

s = Solution()
assert s.uniqueLetterString("LEETCODE")==92