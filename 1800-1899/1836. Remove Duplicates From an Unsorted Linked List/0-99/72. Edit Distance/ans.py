from os import curdir
from typing import List, Optional
import heapq, math, random
from collections import defaultdict, deque, Counter
from bisect import bisect_left
import unittest

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m,n=len(word1),len(word2)
        if not m: return n
        if not n: return m
        # dp[i][j]: edit distance between word1[i:] and word2[j:]
        dp = [[0]*(n+1) for _ in range(m+1)]
        # dp[-2][-1],dp[-1][-2] = 1,1
        for i in range(m-1,-1,-1):
            dp[i][-1] = m-i
        for j in range(n-1,-1,-1):
            dp[-1][j] = n-j
        for i in range(m-1,-1,-1):
            for j in range(n-1,-1,-1):
                # 1. word1[i] match/replace word2[j]
                curDist = (word1[i]!=word2[j])+dp[i+1][j+1]
                # 2. word1[i] char is added, word1[i+1:] match word2[j:]
                curDist = min(curDist,1+dp[i+1][j])
                # 3. word2[j] char is deleted, word1[i:] match word2[j+1:]
                curDist = min(curDist,1+dp[i][j+1])
                dp[i][j] = curDist
        return dp[0][0]

class Test(unittest.TestCase):
    def test_basic(self):
        s = Solution()
        testcases = [["","a",1],["","ab",2],["a","",1],["","",0]]
        for a,b,c in testcases:
            self.assertEqual(s.minDistance(a,b),c,"word1:{} word2:{} expected:{}".format(a,b,c))

    def test_complex(self):
        s = Solution()
        testcases = [["a","ab",1],["a","aa",1],["aa","ab",1],["abc","ac",1],["qwer","qwwerr",2],
        ["intention","execution",5],["horse","ros",3]]
        for a,b,c in testcases:
            self.assertEqual(s.minDistance(a,b),c,"word1:{} word2:{} expected:{}".format(a,b,c))

unittest.main()