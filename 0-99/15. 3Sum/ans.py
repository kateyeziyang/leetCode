from typing import List, Optional
import heapq, math
from collections import defaultdict, deque,Counter
from bisect import bisect_left

# if use nums, no extra space
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        numCounts = Counter(nums)
        negs,poses = [i for i in numCounts if i<0],[i for i in numCounts if i>=0]
        ans = set()
        for neg in negs:
            for pos in poses:
                if -neg==pos:
                    if pos:
                        if 0 in numCounts:
                            ans.add((neg,0,pos))
                    else:
                        if numCounts[0] >= 3:
                            ans.add((0,0,0))
                else:
                    if -neg<pos:
                        if 2*neg != -pos:
                            if -pos-neg in numCounts:
                                ans.add((min(neg,-pos-neg),max(neg,-pos-neg),pos))
                        else:
                            if numCounts[neg] >= 2:
                                ans.add((neg,neg,pos))
                    else:
                        if 2*pos != -neg:
                            if -pos-neg in numCounts:
                                ans.add((neg,min(pos,-pos-neg),max(pos,-pos-neg)))
                        else:
                            if numCounts[pos] >= 2:
                                ans.add((neg,pos,pos))
        tmp = [] if numCounts[0]<3 else [[0,0,0]]
        return [list(triplet) for triplet in ans]+tmp

s = Solution()
# print(s.threeSum(nums = [-1,0,1,2,-1,-4]))
print(s.threeSum([3,0,-2,-1,1,2]))