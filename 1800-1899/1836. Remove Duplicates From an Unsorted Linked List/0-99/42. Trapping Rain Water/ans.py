import enum
from re import L
from typing import List, Optional
import heapq, math, random
from collections import defaultdict, deque, Counter
from bisect import bisect_left

class Solution:
    def trap(self, height: List[int]) -> int:
        return self.trap4(height)

    # brute force O(n^2)
    def trap1(self, height: List[int]) -> int:
        ans = 0
        n = len(height)
        for i,h in enumerate(height):
            prev,next = 0,0
            if i>0:
                prev = max(height[0:i])
            if i+1<n:
                next = max(height[i+1:n])
            if prev<=h or next<=h: # cannot trap water at this loc if any is lower or equal to h
                continue
            ans += min(prev,next)-h
        return ans
    
    # stored max values
    def trap2(self, height: List[int]) -> int:
        n = len(height)
        curleftMax,currightMax = 0,0
        leftmax = [0]*n
        rightmax = [0]*n
        for i in range(n):
            curleftMax = max(curleftMax,height[i])
            leftmax[i] = curleftMax
            currightMax = max(currightMax,height[n-1-i])
            rightmax[n-1-i] = currightMax
        ans = 0
        for i,h in enumerate(height):
            ans += max(min(leftmax[i],rightmax[i])-h,0)
        return ans

    def trap3(self, height: List[int]) -> int:
        if not height: return 0
        n = len(height)
        st = deque([0])
        ans = 0
        i = 1
        while i<n:
            while st and height[st[-1]] < height[i]:
                loc = st.pop()
                if st:
                    ans += (min(height[st[-1]],height[i])-height[loc])*(i-st[-1]-1)
            st.append(i)
            i += 1
        return ans
    
    def trap4(self, height: List[int]) -> int:
        n = len(height)
        l,r = 0,n-1
        lmax,rmax=l,r
        ans = 0
        while l+1<r:
            if height[l]<=height[r]:
                if height[l+1]<height[lmax]:
                    ans += height[lmax]-height[l+1]
                else:
                    lmax = l+1
                l += 1
            else:
                if height[r-1]<height[rmax]:
                    ans += height[rmax]-height[r-1]
                else:
                    rmax = r-1
                r -= 1
        return ans

    def trap5(self, height: List[int]) -> int:
        if len(height)<=2:return 0
        n = len(height)
        l,r = 1,n-2
        lmax,rmax=height[0],height[n-1]
        ans = 0
        while l<=r:
            if lmax<rmax:
                if height[l]<lmax:
                    ans += lmax-height[l]
                else:
                    lmax = height[l]
                l += 1
            else:
                if height[r]<rmax:
                    ans += rmax-height[r]
                else:
                    rmax = height[r]
                r -= 1
        return ans

l = [0,1,0,2,1,0,1,3,2,1,2,1]
s = Solution()
print(s.trap(l))

l = [4,2,0,3,2,5]
s = Solution()
print(s.trap(l))
"""
Start from the left, find first peak (first location such that next bar's height is lower) of bars, to its right will be the first possible place to trap any water.
Suppose the peak is at location i. 

Q: when will h[i]-h[i+1] amount of water be trapped at location i+1?
A: if any bars to the right of i+1 has a height that is at least h[i].

Q: when will at least some water be trapped at location i+1?
A: if any bars to the right of i+1 has a height that is at least h[i+1].

At i+1, the amount of water trapped is max(0,min(max(heights of bars to the left of i+1), max(heights of bars to the right of i+1))-h[i+1])
At each location, we want to know max left height and max right height.

Go through the array from left to the right once, we can find all peaks (and tell the max left height at all locations).
Go through the array from the right to the left, we can tell the max right height at all locations.
After we gain such information, we can calcuate amount of water trapped at each location.
"""
# from typing import List
# class Solution:
#     def trap(self, height: List[int]) -> int:
#         n = len(height)
#         maxLefts,maxRights=[0]*n,[0]*n
#         maxLeft,maxRight=0,0

#         for i,v in enumerate(height):
#             maxLefts[i]=maxLeft
#             if v > maxLeft:
#                 maxLeft = v
#         for i in range(n-1,-1,-1):
#             maxRights[i]=maxRight
#             if height[i] > maxRight:
#                 maxRight = height[i]
#         totalTrapped=0
#         for i,v in enumerate(height):
#             cap = min(maxLefts[i],maxRights[i])
#             curTrapped = 0 if cap <= v else cap-v
#             totalTrapped+=curTrapped
#         return totalTrapped

"""
most confusing part: why can anyone find out the stack solution? It's not intuitive at all
"""