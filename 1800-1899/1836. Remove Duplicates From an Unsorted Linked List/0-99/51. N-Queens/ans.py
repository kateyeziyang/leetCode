from typing import List, Optional
import heapq, math
from collections import defaultdict, deque
from bisect import bisect_left

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        placed = set()
        colTaken = [False]*n
        ans = []
        def placeOK(r,c):
            for x,y in placed:
                if abs(x-r)==abs(y-c):
                    return False
            return True

        def helper(curRow):
            if curRow >= n:
                tmp = [["."]*n for i in range(n)]
                for x,y in placed:
                    tmp[x][y]="Q"
                ans.append(["".join(arr) for arr in tmp])

            for col in range(n):
                if not colTaken[col] and placeOK(curRow,col):
                    placed.add((curRow,col))
                    colTaken[col] = True
                    helper(curRow+1)
                    placed.discard((curRow,col))
                    colTaken[col] = False

        for col in range(n):
            placed.add((0,col))
            colTaken[col] = True
            helper(1)
            placed.discard((0,col))
            colTaken[col] = False
        return ans

s = Solution()
print(s.solveNQueens(4))