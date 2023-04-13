from typing import List, Optional
import heapq, math, random
from collections import defaultdict, deque, Counter
from bisect import bisect_left

class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        ans = []

        def backtracking(cur, remaining, arr, remainingSlots):
            if remaining == 0 and remainingSlots == 0:
                ans.append(list(arr))
            if cur >= 9 or remainingSlots <= 0: return

            for i in range(cur+1, min(remaining, 9)+1):
                arr.append(i)
                backtracking(i, remaining-i, arr, remainingSlots-1)
                arr.pop()

        backtracking(0, n, [], k)
        return ans


# https://leetcode.com/problems/combination-sum-iii/discuss/60624/Clean-167-liners-(AC)
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        def cs(k,n,cap):
            if not k:
                return [[]] * (not n)
            return [comb + [last]
                for last in range(1,cap)
                for comb in cs(k-1,n-last,last)
            ]
        return cs(k,n,10)


s = Solution().combinationSum3
assert(s(3,7))==[[1,2,4]]