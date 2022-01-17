from typing import List, Optional
import heapq, math, random
from collections import defaultdict, deque, Counter
from bisect import bisect_left

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows==1: return [[1]]
        if numRows==2: return [[1],[1,1]]
        ans = [[1],[1,1]]
        for i in range(3,numRows+1):
            ans.append([1]*i)
            for j in range(1,i-1):
                ans[-1][j]=ans[-2][j-1]+ans[-2][j]
        return ans

s = Solution()
print(s.generate(5))