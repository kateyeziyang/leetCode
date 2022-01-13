from typing import List, Optional
import heapq, math
from collections import defaultdict, deque, Counter
from bisect import bisect_left

class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        num = 0
        i = 0
        j = 0
        while i<len(word) and j<len(abbr):
            if abbr[j].isdigit():
                val = int(abbr[j])
                if not num and not val:
                    return False
                num = num*10 + val
                j += 1
            else:
                if num:
                    i += num
                    num = 0
                if i>=len(word) or word[i]!=abbr[j]:
                    return False
                i,j = i+1,j+1
        if j!=len(abbr):
            return False
        return i+num==len(word)

s = Solution()