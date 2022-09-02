from typing import List, Optional
import heapq, math, random
from collections import defaultdict, deque, Counter
from bisect import bisect_left

def solution(inputString):
    stack = []
    n = len(inputString)
    teleports = [0] * n
    
    for i,c in enumerate(inputString):
        if c=='(':
            stack.append(i)
        elif c==')':
            il = stack.pop()
            teleports[il] = i
            teleports[i] = il
    
    result = []
    
    i = 0
    step = 1
    while i<n:
        c = inputString[i]
        if c=='(' or c==')':
            i = teleports[i]
            step *= -1
        else:
            result.append(c)
        i += step
    return ''.join(result)

s = Solution()