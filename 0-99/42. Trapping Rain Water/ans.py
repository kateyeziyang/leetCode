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
from typing import List
class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        maxLefts,maxRights=[0]*n,[0]*n
        maxLeft,maxRight=0,0

        for i,v in enumerate(height):
            maxLefts[i]=maxLeft
            if v > maxLeft:
                maxLeft = v
        for i in range(n-1,-1,-1):
            maxRights[i]=maxRight
            if height[i] > maxRight:
                maxRight = height[i]
        totalTrapped=0
        for i,v in enumerate(height):
            cap = min(maxLefts[i],maxRights[i])
            curTrapped = 0 if cap <= v else cap-v
            totalTrapped+=curTrapped
        return totalTrapped

l = [0,1,0,2,1,0,1,3,2,1,2,1]
s = Solution()
print(s.trap(l))

l = [4,2,0,3,2,5]
s = Solution()
print(s.trap(l))

"""
most confusing part: why can anyone find out the stack solution? It's not intuitive at all
"""