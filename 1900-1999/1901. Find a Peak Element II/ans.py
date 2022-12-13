from typing import List, Optional
import heapq, math, random
from collections import defaultdict, deque, Counter
from bisect import bisect_left

class Solution:
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        m = len(mat)
        l, r = 0, m-1
        n = len(mat[0])

        while l < r:
            mid = (l+r)//2
            # max_val, max_idx = max((v, i) for (i, v) in enumerate(mat[mid]))
            max_idx = max(range(n), key=lambda i: mat[mid][i])
            # max_rval = mat[mid+1][max_idx]
            # if max_rval > mat[mid][max_idx]:
            if mat[mid+1][max_idx] > mat[mid][max_idx]:
            # if max_rval > max_val:
                l = mid + 1
            else:
                r = mid
        return [l, max(range(n), key=lambda i: mat[l][i])]

s = Solution()