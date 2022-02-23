from typing import List
import heapq
from collections import defaultdict, deque

"""
Use this!
https://leetcode.com/problems/word-search/solution/
for rowOffset, colOffset in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            ret = self.backtrack(row + rowOffset, col + colOffset, suffix[1:])
"""

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m,n = len(board),len(board[0])
        l = len(word)
        def wrapper(r,c,visited,idx):
            if idx >= l:
                return True
            if r+1 < m and board[r+1][c]==word[idx] and not visited[r+1][c]:
                
                visited[r+1][c] = True
                if wrapper(r+1,c,visited,idx+1):
                    return True
                visited[r+1][c] = False
            if r-1 >=0 and board[r-1][c]==word[idx] and not visited[r-1][c]:
                
                visited[r-1][c] = True
                if wrapper(r-1,c,visited,idx+1):
                    return True
                visited[r-1][c] = False
            if c+1 < n and board[r][c+1]==word[idx] and not visited[r][c+1]:
                
                visited[r][c+1] = True
                if wrapper(r,c+1,visited,idx+1):
                    return True
                visited[r][c+1] = False
            if c-1 >=0 and board[r][c-1]==word[idx] and not visited[r][c-1]:
                
                visited[r][c-1] = True
                if wrapper(r,c-1,visited,idx+1):
                    return True
                visited[r][c-1] = False
            return False

        letterMap = defaultdict(list)
        for i in range(m):
            for j in range(n):
                letterMap[board[i][j]].append((i,j))
        for loc in letterMap[word[0]]:
            r,c = loc
            visited = [[False]*n for i in range(m)]
            visited[r][c] = True
            if wrapper(r,c,visited,1):
                return True
        return False

s = Solution()
assert s.exist(board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED")==True
assert s.exist(board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB")==False
assert s.exist([["C","A","A"],["A","A","A"],["B","C","D"]],"AAB")==True
assert s.exist([["A","B","C","E"],["S","F","E","S"],["A","D","E","E"]],"ABCESEEEFS")==True