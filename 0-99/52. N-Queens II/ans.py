from typing import List, Optional
import heapq, math, random
from collections import defaultdict, deque, Counter
from bisect import bisect_left

# class Solution:
#     def totalNQueens(self, n: int) -> int:
#         ans = 0
#         board = [[False]*n for _ in range(n)]

#         def backtrack(remainingN, r):
#             nonlocal ans

#             if remainingN == 0:
#                 ans += 1
#                 return
#             for c in range(n):
#                 if not any(board[r]) and not any(row[c] for row in board):
#                     hasQueen = False
#                     for roff,coff in [[1,1],[1,-1],[-1,1],[-1,-1]]:
#                         newr, newc = r+roff, c+coff
#                         while 0<=newr<n and 0<=newc<n:
#                             if board[newr][newc]:
#                                 hasQueen = True
#                                 break
#                             newr, newc = newr+roff, newc+coff
#                         if hasQueen: break
#                     if not hasQueen:
#                         board[r][c] = True
#                         backtrack(remainingN-1, r+1)
#                         board[r][c] = False

#         backtrack(n, 0)
#         return ans

class Solution:
    def totalNQueens(self, n: int) -> int:
        ans = 0
        cols = [False]*n
        diags, opDiags = [False]*(2*n-1), [False]*(2*n-1)

        def backtrack(remainingN, r):
            nonlocal ans

            if remainingN == 0:
                ans += 1
                return
            for c in range(n):
                if not cols[c] and not diags[r-c] and not opDiags[r+c]:
                    cols[c], diags[r-c], opDiags[r+c] = True, True, True
                    backtrack(remainingN-1, r+1)
                    cols[c], diags[r-c], opDiags[r+c] = False, False, False

        backtrack(n, 0)
        return ans

s = Solution().totalNQueens
assert s(1)==1
assert s(3)==0
assert s(4)==2