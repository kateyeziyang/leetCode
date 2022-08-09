from typing import List, Optional
import heapq, math, random
from collections import defaultdict, deque, Counter
from bisect import bisect_left

class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        rows = [0]*3
        cols = [0]*3
        diag, anti_diag = 0, 0

        turns = 0
        d = {0:1, 1:-1}
        w = {0:'A', 1:'B'}
        for x,y in moves:
            r = turns%2
            rows[x] += d[r]
            cols[y] += d[r]
            if x==y:
                diag += d[r]
            if x+y==2:
                anti_diag += d[r]
            l = rows + cols + [diag,anti_diag]
            for num in l:
                if num == 3 or num == -3:
                    return w[r]
            turns += 1
        return 'Draw' if len(moves)==9 else 'Pending'

s = Solution()
s.tictactoe([[0,0],[1,1],[0,1],[0,2],[1,0],[2,0]])