from typing import List, Optional
import heapq, math, random
from collections import defaultdict, deque, Counter
from bisect import bisect_left

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows==1 or numRows>=len(s): return s
        mod = 2*numRows-2
        ans = []
        for i in range(numRows):
            for j in range(i,len(s),mod):
                ans.append(s[j])
                another = j+mod-2*i
                if i!=0 and i!= numRows-1:
                    ans.append(s[another:another+1])
        return "".join(ans)

s = Solution()
print(s.convert(s = "PAYPALISHIRING", numRows = 3))