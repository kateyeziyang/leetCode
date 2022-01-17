from typing import List, Optional
import heapq, math
from collections import defaultdict, deque, Counter
from bisect import bisect_left

class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        def dfs(i,j):
            if board[i][j]!="E":
                return
            numMines = 0
            for roff,coff in [[1,0],[0,1],[-1,0],[0,-1],[1,1],[1,-1],[-1,1],[-1,-1]]:
                ni,nj = i+roff,j+coff
                if 0<=ni<m and 0<=nj<n and board[ni][nj]=="M":
                    numMines += 1
            if not numMines:
                board[i][j] = "B"
                for roff,coff in [[1,0],[0,1],[-1,0],[0,-1],[1,1],[1,-1],[-1,1],[-1,-1]]:
                    ni,nj = i+roff,j+coff
                    if 0<=ni<m and 0<=nj<n:
                        dfs(ni,nj)
                return
            board[i][j] = str(numMines)
        m,n = len(board),len(board[0])
        i,j = click
        if board[i][j]=="M":
            board[i][j] = "X"
            return board
        dfs(i,j)
        return board

s = Solution()