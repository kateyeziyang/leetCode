from typing import List, Optional
import heapq, math
from collections import defaultdict, deque, Counter
from bisect import bisect_left

class Solution:
    def minTransfers(self, transactions: List[List[int]]) -> int:
        m = defaultdict(int)
        for a,b,money in transactions:
            m[a]-=money
            m[b]+=money
        debt = m.values()

        def dfs(s):
            while s<len(debt) and debt[s]==0:
                s+=1
            if s==len(debt): return 0

            r = float("inf")
            prev = 0
            for i in range(s+1,len(debt)):
                if debt[i]!=prev and debt[i]*debt[s]<0:
                    debt[i]+=debt[s]
                    r=min(r,1+dfs(s+1))
                    debt[i]-=debt[s]
                    prev = debt[i]
            return r
        return dfs(0)


s = Solution()