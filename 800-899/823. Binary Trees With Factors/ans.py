from typing import List, Optional
import heapq, math, random
from collections import defaultdict, deque, Counter
from bisect import bisect_left

class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        numTrees = 0
        arr.sort()
        factors = defaultdict(list)
        uniqs = set(arr)
        for i in range(len(arr)):
            for j in range(i, len(arr)):
                idx = arr[i]*arr[j]
                if idx in uniqs:
                    factors[idx].append((i,j))
        dp = defaultdict(lambda: 1) # num of trees with number as node
        for i,k in enumerate(arr):
            if k in factors:
                count = 0
                for il,ir in factors[k]:
                    coeff = 2 if il!=ir else 1
                    count += coeff*dp[il]*dp[ir]
                dp[i] += count
            numTrees += dp[i]
        return numTrees%(10**9 + 7)

s = Solution()