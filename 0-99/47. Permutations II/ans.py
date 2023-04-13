from typing import List, Optional
import heapq, math, random
from collections import defaultdict, deque, Counter
from bisect import bisect_left

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        counts = Counter(nums)
        unused = set(counts.keys())
        ans = []

        def backtrack(idx, arr):
            if idx == len(nums):
                ans.append(list(arr))
            
            for k in list(unused):
                counts[k] -= 1
                if not counts[k]: unused.remove(k)
                arr.append(k)
                backtrack(idx + 1, arr)
                arr.pop()
                unused.add(k)
                counts[k] += 1
        
        backtrack(0, [])
        return ans

s = Solution().permuteUnique
assert sorted(s([1,2,3]))==sorted([[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]])
assert sorted(s([1,2,1]))==sorted([[1,1,2],[1,2,1],[2,1,1]])