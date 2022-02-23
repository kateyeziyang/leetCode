from typing import List, Optional
import heapq, math
from collections import defaultdict, deque
from bisect import bisect_left

# no need to store heights

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        res = 0
        st = deque()
        for i,h in enumerate(heights): # non decreasing stack
            newidx = i
            while st and st[-1][0]>h:
                hei,idx = st.pop()
                res = max(res,hei*(i-idx))
                newidx = idx
            st.append([h,newidx])
        while st:
            hei,idx = st.pop()
            res = max(res,hei*(len(heights)-idx))
        return res

# class Solution:
#     def largestRectangleArea(self, heights: List[int]) -> int:
#         res = 0
#         st = deque()
#         for i,h in enumerate(heights): # non decreasing stack
#             while st and st[-1][0]>h:
#                 hei,idx = st.pop()
#                 res = max(res,hei*(i-idx))
#             st.append([h,i])
#         while st:
#             hei,idx = st.pop()
#             if not st:
#                 res = max(res,hei*len(heights))
#             else:
#                 res = max(res,hei*(len(heights)-idx))
#         return res

s = Solution()
assert s.largestRectangleArea(heights = [2,1,5,6,2,3])==10
assert s.largestRectangleArea([2,1,2])==3
assert s.largestRectangleArea([5,4,1,2])==8