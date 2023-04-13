from typing import List, Optional
import heapq, math, random
from collections import defaultdict, deque, Counter
from bisect import bisect_left, bisect_right

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        n = len(candidates)
        ans = []

        def backtracking(idx, remaining, arr):
            nonlocal ans
            if remaining == 0:
                ans.append(arr)
                return
            if idx == n: return

            endIdx = bisect_right(candidates, remaining, idx)
            for i in range(idx, endIdx):
                backtracking(i, remaining - candidates[i], arr + [candidates[i]])

        backtracking(0, target, [])
        return ans

s = Solution().combinationSum
assert s([8,2,3,7,6,5,1,4], 5) == 7 # 1*5,1*3+2,1+2*2,2+3,1*2+3,1+4,5,