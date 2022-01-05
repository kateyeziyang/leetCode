from typing import List, Optional
import heapq, math
from collections import defaultdict, deque
from bisect import bisect_left

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def nextDot(i,j):
            for c in range(j+1,9):
                if board[i][c] == ".":
                    return i,c
            for r in range(i+1,9):
                for c in range(9):
                    if board[r][c] == ".":
                        return r,c
            return False
        def placeNum(i,j):
            nonlocal board
            num = 0
            while num < 9:
                if rows[i][num] or cols[j][num] or boxes[i//3][j//3][num]: 
                    num += 1
                    continue
                board[i][j] = str(num+1)
                rows[i][num],cols[j][num],boxes[i//3][j//3][num] = True,True,True
                found = nextDot(i,j)
                if not found or placeNum(found[0],found[1]): 
                    return True
                rows[i][num],cols[j][num],boxes[i//3][j//3][num] = False,False,False
                num += 1
            board[i][j] = "."
            return False
        rows,cols,boxes = [[False]*9 for _ in range(9)],[[False]*9 for _ in range(9)],[[[False]*9 for _ in range(3)] for _ in range(3)]
        for i in range(9):
            for j in range(9):
                if board[i][j] != ".":
                    num = int(board[i][j])
                    rows[i][num-1] = True
                    cols[j][num-1] = True
                    boxes[i//3][j//3][num-1] = True
        found = nextDot(0,-1)
        if found:
            placeNum(found[0],found[1])
        return

# class Solution:
#     def solveSudoku(self, board: List[List[str]]) -> None:
#         """
#         Do not return anything, modify board in-place instead.
#         """
#         def nextDot(i,j):
#             for r in range(i,9):
#                 for c in range(9):
#                     if r==i and c<=j:
#                         continue
#                     if board[r][c] == ".":
#                         return r,c
#             return False

#         def placeNum(i,j):
#             nonlocal board
#             num = 1
#             candidate = str(num)
#             while num < 10:
#                 if candidate not in board[i]:
#                     abort = False
#                     for k in range(9):
#                         if candidate == board[k][j]:
#                             abort = True
#                             break
#                     if abort: continue
#                     basei,basej = i//3,j//3
#                     for r in range(basei*3,basei*3+3):
#                         for c in range(basej*3,basej*3+3):
#                             if candidate == board[r][c]:
#                                 abort = True
#                                 break
#                     if not abort:
#                         board[i][j] = candidate
#                         found = nextDot(i,j)
#                         if not found: return True
#                         if placeNum(found[0],found[1]):
#                             return True
#                 num += 1
#                 candidate = str(num)
#             return False
#         found = nextDot(0,0)
#         if found:
#             placeNum(found[0],found[1])
#         return

s = Solution()
# board = [["5","3","4","6","7","8","9","1","2"],["6","7","2","1","9","5","3","4","8"],["1","9","8","3","4","2","5","6","7"],["8","5","9","7","6","1","4","2","3"],["4","2","6","8","5","3","7","9","1"],["7","1","3","9","2","4","8","5","6"],["9","6","1","5","3","7","2","8","."],["2","8",".","4","1","9","6","3","5"],[".",".","5","2","8","6","1","7","9"]]
# assert board == [["5","3","4","6","7","8","9","1","2"],["6","7","2","1","9","5","3","4","8"],["1","9","8","3","4","2","5","6","7"],["8","5","9","7","6","1","4","2","3"],["4","2","6","8","5","3","7","9","1"],["7","1","3","9","2","4","8","5","6"],["9","6","1","5","3","7","2","8","4"],["2","8","7","4","1","9","6","3","5"],["3","4","5","2","8","6","1","7","9"]]
# board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
# s.solveSudoku(board)
# assert board == [["5","3","4","6","7","8","9","1","2"],["6","7","2","1","9","5","3","4","8"],["1","9","8","3","4","2","5","6","7"],["8","5","9","7","6","1","4","2","3"],["4","2","6","8","5","3","7","9","1"],["7","1","3","9","2","4","8","5","6"],["9","6","1","5","3","7","2","8","4"],["2","8","7","4","1","9","6","3","5"],["3","4","5","2","8","6","1","7","9"]]
board = [[".",".","9","7","4","8",".",".","."],["7",".",".",".",".",".",".",".","."],[".","2",".","1",".","9",".",".","."],[".",".","7",".",".",".","2","4","."],[".","6","4",".","1",".","5","9","."],[".","9","8",".",".",".","3",".","."],[".",".",".","8",".","3",".","2","."],[".",".",".",".",".",".",".",".","6"],[".",".",".","2","7","5","9",".","."]]
s.solveSudoku(board)
assert board == [["5","1","9","7","4","8","6","3","2"],["7","8","3","6","5","2","4","1","9"],["4","2","6","1","3","9","8","7","5"],["3","5","7","9","8","6","2","4","1"],["2","6","4","3","1","7","5","9","8"],["1","9","8","5","2","4","3","6","7"],["9","7","5","8","6","3","1","2","4"],["8","3","2","4","9","1","7","5","6"],["6","4","1","2","7","5","9","8","3"]]