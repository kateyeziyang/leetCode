from typing import List, Optional
import heapq, math, random
from collections import defaultdict, deque, Counter
from bisect import bisect_left

# for number x, if exists later y,z that forms 3-sum, then later entry has same value before y
# also works.
# two sum: store sum-x in dict, if cur in dict, then has two sum
# three sum: store sum-x,1 in dict, sum-x-y,0 in dict, for cur, add extra -cur,0 entry to dict,
# and check if cur,0 in dict. If yes, ++
# 7,1,2 6,0,1 6,1,2 5,0,4

class Solution:
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        rems = [defaultdict(int),defaultdict(int)]
        ans = 0
        for x in arr:
            if x in rems[0]:
                ans += rems[0][x]
            for k in rems[1]:
                if k-x >= 0:
                    rems[0][k-x] += rems[1][k]
            rems[1][target-x] += 1
        return ans%(10**9 + 7)


s = Solution()
print(s.threeSumMulti(arr = [1,1,2,2,3,3,4,4,5,5], target = 8))