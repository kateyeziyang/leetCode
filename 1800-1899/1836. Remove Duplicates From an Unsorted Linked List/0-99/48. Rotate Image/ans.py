from typing import List, Optional
import heapq, math, random
from collections import defaultdict, deque, Counter
from bisect import bisect_left

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m,n = len(matrix),len(matrix[0])
        for i in range((m+1)//2):
            for j in range(i,n-i-1):
                saved = matrix[i][j]
                curi,curj = i,j
                for _ in range(3):
                    newi,newj = n-1-curj,curi
                    matrix[curi][curj] = matrix[newi][newj]
                    curi,curj = newi,newj
                matrix[curi][curj] = saved
        return matrix

s = Solution()
print(s.rotate([[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]))