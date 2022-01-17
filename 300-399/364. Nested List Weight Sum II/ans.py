from typing import List, Optional
import heapq, math, random
from collections import defaultdict, deque, Counter
from bisect import bisect_left

# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
class NestedInteger:
   def __init__(self, value=None):
       """
       If value is not specified, initializes an empty list.
       Otherwise initializes a single integer equal to value.
       """

   def isInteger(self):
       """
       @return True if this NestedInteger holds a single integer, rather than a nested list.
       :rtype bool
       """

   def add(self, elem):
       """
       Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
       :rtype void
       """

   def setInteger(self, value):
       """
       Set this NestedInteger to hold a single integer equal to value.
       :rtype void
       """

   def getInteger(self):
       """
       @return the single integer that this NestedInteger holds, if it holds a single integer
       Return None if this NestedInteger holds a nested list
       :rtype int
       """

   def getList(self):
       """
       @return the nested list that this NestedInteger holds, if it holds a nested list
       Return None if this NestedInteger holds a single integer
       :rtype List[NestedInteger]
       """

class Solution:
    def depthSumInverse(self, nestedList: List[NestedInteger]) -> int:
        q = deque()
        vals = [0]
        for x in nestedList:
            if x.isInteger():
                vals[0] += x.getInteger()
            else:
                for xx in x.getList():
                    q.append(xx)
        while q:
            vals.append(0)
            for _ in range(len(q)):
                x = q.popleft()
                if x.isInteger():
                    vals[-1] += x.getInteger()
                else:
                    for xx in x.getList():
                        q.append(xx)
        maxDepth = len(vals)
        ans = 0
        for i,x in enumerate(vals):
            ans += x*(maxDepth-i)
        return ans


s = Solution()
assert s.depthSumInverse([[1,1],2,[1,1]])==8