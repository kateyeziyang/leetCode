from typing import List, Optional
import heapq, math, random
from collections import defaultdict, deque, Counter
from bisect import bisect_left

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        counts = Counter(candidates)
        nums = list(counts.keys())
        ans = []

        def backtracking(idx, remaining, arr):
            if remaining == 0:
                ans.append(list(arr))
                return
            if idx == len(nums): return

            k = nums[idx]
            if k <= remaining:
                numAppended = 0
                rem = remaining
                for _ in range(counts[k]):
                    rem -= k
                    if rem < 0: break
                    arr.append(k)
                    numAppended += 1
                    backtracking(idx+1, rem, arr)
                del arr[-numAppended:]
            backtracking(idx+1, remaining, arr)

        backtracking(0, target, [])
        return ans

s = Solution().combinationSum2
assert sorted(s([10,1,2,7,6,1,5], 8)) == sorted([[1,1,6],[1,2,5],[1,7],[2,6]])
assert sorted(s([5,1,5,4,3,3], 4)) ==  sorted([[1,3],[4]])