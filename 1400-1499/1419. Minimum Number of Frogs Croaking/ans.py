from typing import List, Optional
import heapq, math, random
from collections import defaultdict, deque, Counter
from bisect import bisect_left

class Solution:
    def minNumberOfFrogs(self, croakOfFrogs: str) -> int:
        prev = {'c':'#','r':'c','o':'r','a':'o','k':'a'}
        count = {'#':float('inf'),'c':0,'r':0,'o':0,'a':0,'k':0}
        
        curFrogs, maxFrogs = 0,0
        for c in croakOfFrogs:
            if count[prev[c]] <= count[c]: return -1
            count[c] += 1
            if c=='k': curFrogs -= 1
            if c=='c':
                curFrogs += 1
                maxFrogs = max(maxFrogs, curFrogs)
        countC = count['c']
        for k in 'roak':
            if count[k] != countC: return -1
        return maxFrogs

s = Solution()